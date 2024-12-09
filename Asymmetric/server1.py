import random
import hashlib
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from my_sha256 import SHA256
from AES256 import ecb_encrypt, ecb_decrypt
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


def generate_keys():
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

    # Отправка открытого ключа на сервер
    keys = {'e': e, 'n': n, 'd':d, 'p':p, 'q':q}
    return keys



app = Flask(__name__)
CORS(app)
conn = sqlite3.connect('keys.db', check_same_thread=False)
cursor = conn.cursor()
# Создание таблицы для хранения симметричных ключей и их хэшей
cursor.execute('''CREATE TABLE IF NOT EXISTS symmetric_keys (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symmetric_key TEXT
)''')

conn.commit()
# Функция для вычисления SHA-1 хэша

@app.route('/generate_key', methods=['POST'])
def generate_key():
    data = request.get_json()
    if not data or 'publicKey' not in data:
        return jsonify({'message': 'Ошибка: неверные данные'}), 400

    e = int(data['publicKey']['e'])
    n = int(data['publicKey']['n'])

    # Генерация случайного 128-битного симметричного ключа
    symmetric_key = random.randint(0, 10**40)
    symmetric_key %= n
    sha = SHA256()
    result = sha.calculate_hash(str(symmetric_key).encode())
    # Вставка симметричного ключа и хэша в базу данных
    cursor.execute('INSERT INTO symmetric_keys (symmetric_key) VALUES (?)', (result,))
    conn.commit()
    last_id = cursor.lastrowid

    # Шифрование симметричного ключа с помощью открытого ключа (e, n)
    cipher = pow(symmetric_key, e, n)
    sign=generate_keys()
    global Sign
    Sign=sign
    shas = SHA256()
    resultat = shas.calculate_hash('Hello there'.encode())
    message_hash_int = int(resultat, 16)
    print(f"int hash server: {message_hash_int}")
    supersign=mod_exp(message_hash_int, 24824399046515177368432885834593572191497196886512769131460632250759874452387303254024717252159367364408059816873862079190423461434304286312520475457524237622978251071851683312453808604934110224820953461287831052266887704579581955964783574720872811006132151357839513642455662544863788347759326761714402739339, 92091660169167419559197440624591832530579526883219323557199340404563973391435874521361542335510593648022814023752338463760330462534462316740321385576203289116752289585767802651661529586265786884017770196169402312110716890780234237152155461164865986703398761239992107537330115813034830250372521369969141441367)
    return jsonify({
        'message': 'Ключ успешно получен',
        'id': last_id,
        'public': {
            'origin': symmetric_key,  # Случайное 128-битное число
            'chipher': cipher,  # Зашифрованное число
            'sha256': result# Хэш SHA-1
        },
        'server_sign':{
            'n':sign['n'],
            'e':sign['e']
        },
        'Agreed':{
            'message':'Hello there',
            'hash':supersign
        }
    })


@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    encrypted_message = data.get('encryptedMessage')
    idCL = data.get('id')
    sign=data.get('signature')
    gg=mod_exp(sign, Sign['d'], Sign['n'])
    print('echo', mod_exp(sign, Sign['d'], Sign['n']))
    sha_sign = hex(gg)[2:]
    print('hash original',sha_sign)

    if not encrypted_message or not idCL:
        return jsonify({"status": "error", "message": "Неверные данные"}), 400

    # Поиск симметричного ключа в базе данных по id
    cursor.execute('SELECT symmetric_key FROM symmetric_keys WHERE id = ?', (idCL,))
    result = cursor.fetchone()

    if result is None:
        return jsonify({"status": "error", "message": "Ключ с таким ID не найден"}), 404

    symmetric_key = result[0]  # Получаем хэш симметричного ключа

    print("Получено зашифрованное сообщение:", encrypted_message)
    string_list = [''.join([chr(b) for b in byte_list]) for byte_list in encrypted_message]
    print(''.join(string_list))
    # Расшифровка сообщения с использованием симметричного ключа
    decrypted_message = ecb_decrypt(encrypted_message, symmetric_key)
    ''.join(decrypted_message)
    decrypted_message[0] = decrypted_message[0].rstrip('0')
    sha = SHA256()
    result = sha.calculate_hash(str(decrypted_message[0]).encode())
    print(decrypted_message)
    print('Стартовый хэш:', result)
    print("Расшифровка:", decrypted_message)
    if sha_sign in result:
        print("Пользователь идентифицирован")
    else:
        print("Пользователь не идентифицирован")
    return jsonify({"status": "success", "message": "Сообщение успешно расшифровано", "decrypted_message": decrypted_message})


if __name__ == '__main__':
    app.run(debug=True)
