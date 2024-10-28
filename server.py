import random
import hashlib
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Функция для вычисления SHA-1 хэша
def calculate_sha1(data):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(data)
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
    symmetric_key%=n

    # Преобразование симметричного ключа в байты для вычисления хэша
    symmetric_key_bytes = symmetric_key.to_bytes(16, 'big')  # 16 байт = 128 бит


    sha1_hash = calculate_sha1(symmetric_key_bytes)

    # Шифрование симметричного ключа с использованием открытого ключа
    cipher = pow(symmetric_key, e, n)

    return jsonify({
        'message': 'Ключ успешно получен',
        'public': {
            'origin': symmetric_key,  # Случайное 128-битное число
            'chipher': cipher,  # Зашифрованное число
            'sha1': sha1_hash  # Хэш SHA-1
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
