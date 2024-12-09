import random
import math
import requests
import json
import hashlib
from AES256 import ecb_encrypt
from my_sha256 import SHA256
# Функция для проверки, является ли число простым
def is_prime(n, k=40):  # k — количество раундов, увеличено для 1000-битных чисел
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Представим n-1 в виде 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Тестируем k раз
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)  # a^d % n
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


# Функция для возведения в степень по модулю
def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

# Функция для генерации случайного числа в заданном диапазоне
def get_random_number(min_val, max_val):
    return random.randint(min_val, max_val)

# Функция для расширенного алгоритма Евклида
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

# Функция для нахождения обратного элемента по модулю
def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise Exception("Обратный элемент не существует")
    return x % m

# Функция для случайного выбора e
def get_random_e(phi):
    e = 0
    while True:
        e = get_random_number(2, phi - 1)
        if extended_gcd(e, phi)[0] == 1:
            break
    return e

# Функция для отправки зашифрованного сообщения на сервер
def send_encrypted_message(message, symmetric_key_bytes, myID, supersign):
    encrypted_message = ecb_encrypt(message,symmetric_key_bytes)
    print('Начальный хэш сообщения:', supersign)
    try:
        response = requests.post('http://localhost:5000/send_message', json={'encryptedMessage': encrypted_message, 'signature': supersign, 'id': myID})
        if response.status_code == 200:
            print("Сообщение успешно отправлено")
        else:
            print("Ошибка при отправке сообщения")
    except Exception as e:
        print("Ошибка:", str(e))

# Основная функция для генерации ключей и взаимодействия с сервером
def generate_keys_and_send():
    # Генерация случайных простых чисел p и q
    p = 0
    while not is_prime(p):
        p = get_random_number(2**511, 2**512 - 1)

    q = 0
    while not is_prime(q) or p == q:
        q = get_random_number(2**511, 2**512 - 1)

    n = p * q
    phi = (p - 1) * (q - 1)
    e = get_random_e(phi)  # Случайный выбор e
    d = mod_inverse(e, phi)  # Приватный ключ

    print(f"Сгенерированные простые числа p: {p}, q: {q}")
    print(f"Открытый ключ (e, n): ({e}, {n})")
    print(f"Приватный ключ (d, n): ({d}, {n})")

    # Отправка открытого ключа на сервер
    public_key = {'e': e, 'n': n}
    try:
        response = requests.post('http://localhost:5000/generate_key', json={'publicKey': public_key})
        if response.status_code != 200:
            print("Ошибка при отправке ключа")
        else:
            result = response.json()
            podp=result['Agreed']['hash']
            Mass=result['Agreed']['message']
            shas = SHA256()
            resultat = shas.calculate_hash(Mass.encode())
            Idpodp=mod_exp(podp,44304114243519824536190674373649699331052442148865374737998814738026331661551740074648950463632797844755409640695099753875251227274518334132643669396507830569064902430447365928169899770478563520652377560006877080607152192498206108880950530916638954076748434940318201328885961533574254474849852873031761454659,92091660169167419559197440624591832530579526883219323557199340404563973391435874521361542335510593648022814023752338463760330462534462316740321385576203289116752289585767802651661529586265786884017770196169402312110716890780234237152155461164865986703398761239992107537330115813034830250372521369969141441367)
            sha_sign = hex(Idpodp)[2:]
            if resultat in sha_sign:
                print('Сервер идентифицирован\n')
            else:
                print('Где сервер?')
            cipher = result['public']['chipher']
            decrypted = mod_exp(cipher, d, n)
            sha = SHA256()
            sha_256 = sha.calculate_hash(str(decrypted).encode())

            # Возможность отправки зашифрованного сообщения
            while True:
                user_input = input("Введите зашифрованное сообщение для отправки (или 'exit' для выхода): ")
                if user_input.lower() == 'exit':
                    break
                sha_mess = SHA256()
                sha_sign = sha_mess.calculate_hash(str(user_input).encode())
                message_hash_int = int(sha_sign, 16)
                print(f"int hash: {message_hash_int}")
                supersign=mod_exp(message_hash_int, result['server_sign']['e'], result['server_sign']['n'])
                send_encrypted_message(user_input, sha_256, result['id'], supersign)

    except Exception as e:
        print("Ошибка:", str(e))

if __name__ == "__main__":
    generate_keys_and_send()
