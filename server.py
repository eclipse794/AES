import random
import hashlib
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from my_sha256 import SHA256
from AES import ecb_encrypt, ecb_decrypt
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

def calculate_sha1(number):
    # Преобразование числа в строку, затем в байты
    number_str = str(number)
    number_bytes = number_str.encode('utf-8')  # Преобразование строки в байты
    sha1_hash = hashlib.sha1()
    sha1_hash.update(number_bytes)
    return sha1_hash.hexdigest()

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

    # Хеширование симметричного ключа
    sha1_hash = calculate_sha1(symmetric_key)

    # Вставка симметричного ключа и хэша в базу данных
    cursor.execute('INSERT INTO symmetric_keys (symmetric_key) VALUES (?)', (sha1_hash,))
    conn.commit()
    last_id = cursor.lastrowid

    # Шифрование симметричного ключа с помощью открытого ключа (e, n)
    cipher = pow(symmetric_key, e, n)

    return jsonify({
        'message': 'Ключ успешно получен',
        'id': last_id,
        'public': {
            'origin': symmetric_key,  # Случайное 128-битное число
            'chipher': cipher,  # Зашифрованное число
            'sha1': sha1_hash ,
            'sha256': result# Хэш SHA-1
        }
    })


@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    encrypted_message = data.get('encryptedMessage')
    idCL = data.get('id')

    if not encrypted_message or not idCL:
        return jsonify({"status": "error", "message": "Неверные данные"}), 400

    # Поиск симметричного ключа в базе данных по id
    cursor.execute('SELECT symmetric_key FROM symmetric_keys WHERE id = ?', (idCL,))
    result = cursor.fetchone()

    if result is None:
        return jsonify({"status": "error", "message": "Ключ с таким ID не найден"}), 404

    symmetric_key = result[0]  # Получаем хэш симметричного ключа

    print("Получено зашифрованное сообщение:", encrypted_message)
    
    # Расшифровка сообщения с использованием симметричного ключа
    decrypted_message = ecb_decrypt(encrypted_message, symmetric_key)
    
    return jsonify({"status": "success", "message": "Сообщение успешно расшифровано", "decrypted_message": decrypted_message})


if __name__ == '__main__':
    app.run(debug=True)
