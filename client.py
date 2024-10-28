import random
import math
import requests
import json
import hashlib
def calculate_sha1(data):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(data)
    return sha1_hash.hexdigest()
# Функция для проверки, является ли число простым
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
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

# Основная функция для генерации ключей и взаимодействия с сервером
def generate_keys_and_send():
    # Генерация случайных простых чисел p и q
    p = 0
    while not is_prime(p):
        p = get_random_number(1, 100000000000000000)
    
    q = 0
    while not is_prime(q) or p == q:
        q = get_random_number(1, 1000000000000000)
    
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
            print("Ответ сервера:", result)
            cipher = result['public']['chipher']
            decrypted = mod_exp(cipher, d, n)
            print(f"Зашифрованное число: {cipher}")
            print(f"Расшифрованное число: {decrypted}")
            symmetric_key_bytes = decrypted.to_bytes(16, 'big')  # 16 байт = 128 бит
            sha1_hash = calculate_sha1(symmetric_key_bytes)
            print('Hash',sha1_hash)
    except Exception as e:
        print("Ошибка:", str(e))

if __name__ == "__main__":
    generate_keys_and_send()
