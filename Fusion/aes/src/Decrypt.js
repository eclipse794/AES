import React, { useState } from 'react';
import './App.css';
import { ECB_D } from './AES';

export function Decrypt() {
  const [inputValue, setInputValue] = useState('a24004370088cb841e2b8722e31c7f4f');
  const [keyValue, setKeyValue] = useState('2b7e151628aed2a6abf7158809cf4f3c'); // Значение по умолчанию
  const [outputValue, setOutputValue] = useState('');

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleKeyChange = (event) => {
    setKeyValue(event.target.value);
  };

  const handleOutputChange = () => {
    let modifiedKey = keyValue;
  
    if (keyValue.length < 32) {
      modifiedKey = keyValue.padEnd(32, 'a'); // Дополняем "a" до 32 символов
    } else if (keyValue.length > 32) {
      modifiedKey = keyValue.substring(0, 32); // Обрезаем до 32 символов
    }
    setKeyValue(modifiedKey);
  
    let t = ECB_D(inputValue, modifiedKey); // Используем модифицированный ключ
    for (let i = 0; i < t.length; i++) {
      for (let j = 0; j < 16; j++) {
        t[i][j] = String.fromCharCode(t[i][j]);
      }
    }
    t = t.flat();
  
    // Преобразование в строку
    t = t.join('');
    let indexOfZero = t.indexOf(0);
    if (indexOfZero !== -1) {
      t = t.slice(0, indexOfZero); // Ноль также будет удален
    }
    setOutputValue(t);
  };
  
  return (
    <div className="App">
      <div className="container">
        <h1 className="title">AES Расшифрование</h1>
        <div className="input-group">
          <label htmlFor="key">Ключ:</label>
          <input
            id="key"
            type="text"
            className="input-field"
            value={keyValue}
            onChange={handleKeyChange}
            placeholder="Введите ключ"
          />
        </div>
        <div className="input-group">
          <label htmlFor="input">Ввод:</label>
          <textarea
            id="input"
            className="input-field"
            value={inputValue}
            onChange={handleInputChange}
            placeholder="Введите hex"
          />
        </div>
        <button className="convert-button" onClick={handleOutputChange}>
          Расшифровать
        </button>
        <div className="output-group">
          <label htmlFor="output">Вывод:</label>
          <textarea
            id="output"
            className="output-field"
            value={outputValue}
            readOnly
          />
        </div>
      </div>
    </div>
  );
}
