<?php
// Установите заголовки для CORS
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST, GET, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type");
function hexStringToNumber($hexString) {
    $decimalNumber = '0';
    $length = strlen($hexString);
    
    for ($i = 0; $i < $length; $i++) {
        // Преобразуем каждый символ шестнадцатеричной строки в число
        $decimalNumber = bcmul($decimalNumber, '16'); // Умножаем на основание (16)
        $decimalNumber = bcadd($decimalNumber, hexdec($hexString[$i])); // Добавляем текущее значение
    }

    return $decimalNumber;
}

// Преобразуем шестнадцатеричную строку в большое целое число через конкатенацию байтов
function hexToNumber($hexString) {
    $decimalString = '';

    // Проходим по каждому байту (по два символа за раз)
    for ($i = 0; $i < strlen($hexString); $i += 2) {
        // Берем два символа (байт) и преобразуем их в десятичное число
        $byte = substr($hexString, $i, 2);
        $decimalByte = str_pad(hexdec($byte), 3, '0', STR_PAD_LEFT); // Дополняем до 3 цифр
        $decimalString .= $decimalByte; // Конкатенируем в строку
    }

    // Возвращаем полученное большое число как строку
    return $decimalString;
}

// Пример использования

// Функция для возведения в степень по модулю
function modExp($base, $exp, $mod) {
    $result = 1;
    $base = $base % $mod;
    while ($exp > 0) {
        if ($exp % 2 == 1) {
            $result = ($result * $base) % $mod;
        }
        $exp = intval($exp / 2);
        $base = ($base * $base) % $mod;
    }
    return $result;
}

if ($_SERVER['REQUEST_METHOD'] == 'OPTIONS') {
    http_response_code(200);
    exit;
}

// Получение данных
$data = json_decode(file_get_contents('php://input'), true);

if (!$data) {
    echo json_encode(['message' => 'Ошибка: неверные данные']);
    exit;
}

if (isset($data['publicKey']['e']) && isset($data['publicKey']['n'])) {
    $e = (int)$data['publicKey']['e'];
    $n = (int)$data['publicKey']['n'];

    // Генерация симметричного ключа
    $symmetricKey = '2'; // 16 байт = 128 бит
    //$ex=hexStringToNumber($symmetricKey);
	$ex=bcmod(bcpow($symmetricKey, (string)$e), (string)$n);
    echo json_encode([
        'message' => 'Ключ успешно получен',
        'public' => [
            'origin' =>$symmetricKey,
            'chipher' =>$ex
        ]
    ]);
} else {
    echo json_encode(['message' => 'Ошибка: неверные данные']);
}
?>
