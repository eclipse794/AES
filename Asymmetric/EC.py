import hashlib
import os

# Определим параметры кривой secp256k1 (это пример, параметры реальной кривой можно найти в открытых источниках)
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F  # Простое число (модуль)
a = 0x0  # Коэффициент a кривой
b = 0x7  # Коэффициент b кривой
Gx = 0x79BE667EF9DCBBAC55A62B18ED0E7145A4F6CBBF40939D541D68B5321CBF9C6  # x-координата базовой точки G
Gy = 0x48528E3D3986E57B7CCF0C57563F6C818A592C59CC7083E97C94E6F5E5D07E6  # y-координата базовой точки G
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141  # Порядок группы (порядок G)

# Функция для умножения точки на скаляр (умножение точки на число по модулю p)
def point_add(p1, p2):
    """Операция сложения двух точек на эллиптической кривой."""
    if p1 == (0, 0):
        return p2
    if p2 == (0, 0):
        return p1
    x1, y1 = p1
    x2, y2 = p2

    if x1 == x2 and y1 == y2:  # Удвоение точки
        m = (3 * x1**2 + a) * pow(2 * y1, -1, p) % p
    else:
        m = (y2 - y1) * pow(x2 - x1, -1, p) % p

    x3 = (m**2 - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)

def scalar_multiply(k, P):
    """Умножение точки на скаляр с использованием алгоритма двойного и сложения."""
    result = (0, 0)  # Точка на кривой, которая представляет "бесконечность"
    addend = P

    while k:
        if k & 1:
            result = point_add(result, addend)
        addend = point_add(addend, addend)
        k >>= 1
    return result

# Функция для подписи сообщения
def sign_message(private_key, message):
    """Подписывает сообщение с использованием приватного ключа."""
    # Хешируем сообщение (например, с помощью SHA-256)
    message_hash = int(hashlib.sha256(message.encode('utf-8')).hexdigest(), 16)

    # Генерируем случайное число k (оно должно быть случайным для каждой подписи)
    k = os.urandom(32)
    k = int.from_bytes(k, byteorder='big') % (n - 1)

    # Вычисляем точку k*G
    R = scalar_multiply(k, (Gx, Gy))
    r = R[0] % n
    if r == 0:
        return sign_message(private_key, message)  # Перегенерировать, если r == 0

    # Вычисляем s
    s = (pow(k, -1, n) * (message_hash + private_key * r)) % n
    if s == 0:
        return sign_message(private_key, message)  # Перегенерировать, если s == 0

    return (r, s)

# Функция для отправки сообщения на сервер (простой пример с использованием сокетов)
import socket

def send_to_server(message, signature):
    """Отправить подписанное сообщение на сервер."""
    # Пример простого сокет-сервера
    server_address = ('localhost', 5000)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(server_address)
        s.sendall(f"Message: {message}\nSignature: {signature}\n".encode())

# Пример использования
private_key = 0x1D2C3F4B5A6E7D8F9A0B1C2D3E4F5A6B7C8D9E0F123456789ABCDEF01234567
message = "Hello, this is a secure message."

# Подписываем сообщение
signature = sign_message(private_key, message)

# Отправляем на сервер
send_to_server(message, signature)
