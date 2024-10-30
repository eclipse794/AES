sBox = [
    [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
    [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
    [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
    [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
    [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
    [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
    [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
    [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
    [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
    [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
    [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
    [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
    [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
    [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
    [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
    [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16],
]

invSBox = [
    [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
    [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
    [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
    [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
    [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
    [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
    [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
    [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
    [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
    [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
    [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
    [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
    [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
    [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
    [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
    [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]
]
def text_to_bytes(text):
    bytes_arr = []
    for char in text:
        char_code = ord(char)  # Получаем код символа
        bytes_arr.append(char_code & 0xff)  # Преобразуем код символа в байт (младший байт)
    return bytes_arr


def hex_to_bytes(hex_str):
    bytes_arr = []
    for i in range(0, len(hex_str), 2):
        byte = int(hex_str[i:i+2], 16)
        bytes_arr.append(byte)
    return bytes_arr


def change_sbox(number):
    one = number // 16
    two = number % 16
    return sBox[one][two]


def inv_change_sbox(number):
    one = number // 16
    two = number % 16
    return invSBox[one][two]

def double(number):
    byte = number & 0xff
    result = byte << 1
    if byte & 0x80:
        result ^= 0x11b
    return result & 0xff


def triple(number):
    return double(number) ^ number


def bull9(number):
    one = double(number)  # 2 * number
    two = double(one)     # 4 * number
    three = double(two)   # 8 * number
    return three ^ number  # 8 * number ^ number


def bull11(number):
    one = double(number)  # 2 * number
    two = double(one)     # 4 * number
    three = double(two)   # 8 * number
    return one ^ three ^ number  # 2 * number ^ 8 * number ^ number


def bull13(number):
    one = double(number)  # 2 * number
    two = double(one)     # 4 * number
    three = double(two)   # 8 * number
    return two ^ three ^ number  # 4 * number ^ 8 * number ^ number


def bull14(number):
    one = double(number)  # 2 * number
    two = double(one)     # 4 * number
    three = double(two)   # 8 * number
    return one ^ two ^ three  # 2 * number ^ 4 * number ^ 8 * number


def mix_column(column):
    result = [0] * 16
    for i in range(0, 16, 4):
        result[i] = double(column[i]) ^ triple(column[i + 1]) ^ column[i + 2] ^ column[i + 3]
        result[i + 1] = column[i] ^ double(column[i + 1]) ^ triple(column[i + 2]) ^ column[i + 3]
        result[i + 2] = column[i] ^ column[i + 1] ^ double(column[i + 2]) ^ triple(column[i + 3])
        result[i + 3] = triple(column[i]) ^ column[i + 1] ^ column[i + 2] ^ double(column[i + 3])
    return result

def inv_mix_column(column):
    result = [0] * 16
    for i in range(0, 16, 4):
        result[i] = bull14(column[i]) ^ bull11(column[i + 1]) ^ bull13(column[i + 2]) ^ bull9(column[i + 3])
        result[i + 1] = bull9(column[i]) ^ bull14(column[i + 1]) ^ bull11(column[i + 2]) ^ bull13(column[i + 3])
        result[i + 2] = bull13(column[i]) ^ bull9(column[i + 1]) ^ bull14(column[i + 2]) ^ bull11(column[i + 3])
        result[i + 3] = bull11(column[i]) ^ bull13(column[i + 1]) ^ bull9(column[i + 2]) ^ bull14(column[i + 3])
    return result



def key_expansion_256(key):
    init_vector = [1, 2, 4, 8, 16, 32, 64]
    
    # Преобразуем ключ в массив байтов
    key_bytes = hex_to_bytes(key)
    keys = []
    keys.append([])
    keys[0]=key_bytes
    hex_matrix = [hex(value)[2:].upper().zfill(2) for value in keys[0]]
    # print(hex_matrix)
    for t in range(7):
        hex_bytes = [f"{byte:02x}" for byte in key_bytes]  # Преобразуем в hex-строки

        # Создаем массив для сдвигов
        change_arr = [key_bytes[28], key_bytes[29], key_bytes[30], key_bytes[31]]

        # Сдвигаем массив
        edge = change_arr[0]
        change_arr = change_arr[1:] + [edge]

        # Применяем S-Box
        new_arr = [change_sbox(x) for x in change_arr]


        # XOR с init_vector[t] и ограничиваем до байта
        new_arr[0] ^= init_vector[t]
        new_arr[0] %= 256

        # Создаем новую матрицу ключей
        result_matrix = []
        for i in range(4):
            for j in range(4):
                temp = key_bytes[4 * i + j] ^ new_arr[j]
                new_arr[j] = temp
                result_matrix.append(temp)
        nextInit=[result_matrix[12],result_matrix[13],result_matrix[14],result_matrix[15]]
        new_arr = [change_sbox(x) for x in nextInit]
        for i in range(4):
            for j in range(4):
                temp = key_bytes[16+4 * i + j] ^ new_arr[j]
                new_arr[j] = temp
                result_matrix.append(temp)

        key_bytes = result_matrix  # Обновляем ключи для следующей итерации
        hex_matrix = [hex(value)[2:].upper().zfill(2) for value in result_matrix]
        keys.append(result_matrix)
        # print(hex_matrix)
    
    return keys


def aes_encrypt_256(plaintext, key):
    byte_text = plaintext
    # Генерация ключей
    import time
    start_time = time.time()
    
    arrays=key_expansion_256(key)
    # print('fg', arrays)
    keys = []

    # Проходим по каждому внутреннему массиву
    for array in arrays:
        # Находим середину
        mid = len(array) // 2
        
        # Делим массив на две половины и добавляем их в новый список
        keys.append(array[:mid])  # Первая половина
        keys.append(array[mid:])  # Вторая половина    
    # print('f',keys)
    res = [keys[0][i] ^ byte_text[i] for i in range(16)]
    hex_matrix = [hex(value)[2:].upper().zfill(2) for value in res]
    print(hex_matrix)
    for j in range(14):
        hex_matrix = [hex(value)[2:].upper().zfill(2) for value in keys[j+1]]
        # print('keys',hex_matrix)
        # Замена через S-Box
        res = [change_sbox(byte) for byte in res]
        # Первый сдвиг (ShiftRows)
        first = res[1]
        for i in range(1, 10, 4):
            res[i] = res[i + 4]
        res[13] = first
        # Второй сдвиг (ShiftRows)
        one, two = res[2], res[6]
        for i in range(2, 9, 4):
            res[i] = res[i + 8]
        res[10], res[14] = one, two
        res[13] = first
        
        # Третий сдвиг (ShiftRows)
        mind = res[15]
        for l in range(15, 6, -4):
            res[l] = res[l - 4]
        res[3] = mind
        
        # Добавление матрицы (MixColumns)
        if j != 13:
            new_matrix = mix_column(res)
        else:
            new_matrix = res
        hex_matrix = [hex(value)[2:].upper().zfill(2) for value in keys[j+1]]
        # print('keys',hex_matrix)
        hex_matrix = [hex(value)[2:].upper().zfill(2) for value in new_matrix]
        # print('plain',hex_matrix)
        # Добавляем раундовый ключ
        res = [new_matrix[i] ^ keys[j+1][i] for i in range(16)]
        hex_matrix = [hex(value)[2:].upper().zfill(2) for value in res]
        # print(hex_matrix)
        # print('round', j, hex_matrix)
    
    return res



def aes_decrypt_256(ciphertext, key):
    res = ciphertext
    
    arrays=key_expansion_256(key)
    # print('fg', arrays)
    keys = []

    # Проходим по каждому внутреннему массиву
    for array in arrays:
        # Находим середину
        mid = len(array) // 2
        
        # Делим массив на две половины и добавляем их в новый список
        keys.append(array[:mid])  # Первая половина
        keys.append(array[mid:])  # Вторая половина     
    

    for j in range(14):
        # XOR с ключом раунда
        hex_matrix = [hex(value)[2:].upper().zfill(2) for value in keys[14 - j]]
        # print('hi',hex_matrix)
        res = [res[i] ^ keys[14 - j][i] for i in range(16)]
        
        if j != 0:
            res = inv_mix_column(res)
        
        # Первый обратный сдвиг (ShiftRows)
        last = res[13]
        for i in range(13, 1, -4):
            res[i] = res[i - 4]
        res[1] = last
        
        # Второй обратный сдвиг (ShiftRows)
        temp1, temp2 = res[2], res[6]
        for i in range(2, 10, 4):
            res[i] = res[i + 8]
        res[10], res[14] = temp1, temp2
        
        # Третий обратный сдвиг (ShiftRows)
        temp = res[3]
        for i in range(3, 15, 4):
            res[i] = res[i + 4]
        res[15] = temp
        
        # Замена через обратный S-Box
        res = [inv_change_sbox(byte) for byte in res]
        hex_matrix = [hex(value)[2:].upper().zfill(2) for value in res]
        # print('res',hex_matrix)
    
    # XOR с первым ключом
    res = [keys[0][i] ^ res[i] for i in range(16)]
    hex_matrix = [hex(value)[2:].upper().zfill(2) for value in res]
    # print('res',hex_matrix)
    return res


def ecb_encrypt(plaintext, key):
    blocks = []
    crypto = []
    
    # Разделение текста на блоки по 16 символов
    for i in range(0, len(plaintext), 16):
        blocks.append(plaintext[i:i + 16])
    
    # Дополнение последнего блока нулями, если он меньше 16 символов
    last_block = blocks[-1]
    if len(last_block) < 16:
        last_block = last_block.ljust(16, '0')  # Добавляем нули
        blocks[-1] = last_block
    
    
    # Шифрование каждого блока
    for block in blocks:
        crypto.append(aes_encrypt_256(text_to_bytes(block), key))
    
    return crypto


def ecb_decrypt(ciphertext, key):
    crypto = []
    
    # Расшифровка каждого блока
    for block in ciphertext:
        decrypted_block = aes_decrypt_256(block, key)
        crypto.append(bytes(decrypted_block).decode('utf-8', errors='ignore'))
    
    print('itog',crypto)
    return crypto

# b=aes_encrypt_256(text_to_bytes('Hello world00000'),'2b7e151628aed2a6abf7158809cf4f3c2b7e151628aed2a6abf7158809cf4f3c')
# aes_decrypt_256(b,'2b7e151628aed2a6abf7158809cf4f3c2b7e151628aed2a6abf7158809cf4f3c')
#key_expansion_256('2b7e151628aed2a6abf7158809cf4f3c2b7e151628aed2a6abf7158809cf4f3c')
# Пример использования
# key_up = '2b7e151628aed2a6abf7158809cf4f3c2b7e151628aed2a6abf7158809cf4f3c'
# text = "Hello. I am fine."
# encrypted = ecb_encrypt(text, key_up)
# ecb_decrypt(encrypted, key_up)