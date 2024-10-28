import React, { useState } from 'react';

function isPrime(n) {
    if (n <= 1) {
        return false;
    }
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            return false;
        }
    }
    return true;
}
function Up(base, exponent, modulus) {
    console.log(base, exponent, modulus)
    base = base % modulus;
    let result = 1;
  
    while (exponent > 0) {
      if (exponent % 2 === 1) {
        result = (result * base) % modulus;
      }
      base = (base * base) % modulus;
      exponent = Math.floor(exponent / 2);
    }
  
    return result;
  }
function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Функция для нахождения расширенного НОД
function extendedGCD(a, b) {
    if (b === 0) {
        return [a, 1, 0];
    }
    const [gcd, x1, y1] = extendedGCD(b, a % b);
    const x = y1;
    const y = x1 - Math.floor(a / b) * y1;
    return [gcd, x, y];
}

// Функция для нахождения обратного элемента
function modInverse(a, m) {
    const [gcd, x, y] = extendedGCD(a, m);
    if (gcd !== 1) {
        throw new Error("Обратный элемент не существует");
    }
    return (x % m + m) % m;
}

// Функция для случайного выбора e
function getRandomE(phi) {
    let e;
    do {
        e = getRandomNumber(2, phi - 1);
    } while (extendedGCD(e, phi)[0] !== 1); // Убедимся, что e и phi взаимно просты
    return e;
}

const App = () => {
    const [p, setP] = useState(0);
    const [q, setQ] = useState(0);
    const [publicKey, setPublicKey] = useState('');
    const [privateKey, setPrivateKey] = useState('');
    const [loading, setLoading] = useState(false);
    const handleGenerateKeys = async () => {
      setLoading(true);
      let pValue = 0;
      while (!isPrime(pValue)) {
          pValue = getRandomNumber(1, 1000); // Уменьшил диапазон для простоты
      }
      let qValue = 0;
      while (!isPrime(qValue) || pValue === qValue) { // Убедимся, что p и q разные
          qValue = getRandomNumber(1, 10000000);
      }
  
      const n = pValue * qValue;
      const phi = (pValue - 1) * (qValue - 1);
      const e = getRandomE(phi); // Случайный выбор e
      const d = modInverse(e, phi);
  
      setP(pValue);
      setQ(qValue);
      setPublicKey(`(${e}, ${n})`); // Открытый ключ: (e, n)
      setPrivateKey(`(${d}, ${n})`); // Закрытый ключ: (d, n)
  
      // Отправка открытого ключа на сервер
      try {
          const response = await fetch('http://localhost:5000/generate_key', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify({ publicKey: { e, n } }),
          });
  
          if (!response.ok) {
              throw new Error('Ошибка при отправке ключа');
          }
  
          const result = await response.json();
          console.log('Ответ сервера:', result);
          console.log(Up(result.public.chipher, d, n))
      } catch (error) {
          console.error('Ошибка:', error);
      }
  
      setLoading(false);
  };
  
    return (
        <div>
            <h1>Генератор ключей RSA</h1>
            <button onClick={handleGenerateKeys} disabled={loading}>
                {loading ? 'Генерация...' : 'Сгенерировать ключи'}
            </button>
            <h2>Случайные простые числа:</h2>
            <p>p: {p}</p>
            <p>q: {q}</p>
            <h2>Публичный ключ:</h2>
            <p>{publicKey}</p>
            <h2>Приватный ключ:</h2>
            <p>{privateKey}</p>
        </div>
    );
};

export default App;
