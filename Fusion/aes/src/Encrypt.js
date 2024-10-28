import React, { useState } from 'react';
import './App.css';
import { ECB_S } from './AES';
import { Buffer } from 'buffer';

function Encrypt() {
  const [inputValue, setInputValue] = useState('');
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
    console.log('key',modifiedKey)
  setKeyValue(modifiedKey);
    let t = ECB_S(inputValue, modifiedKey); // Используем модифицированный ключ
    let outStream = [];
    for (let i = 0; i < t.length; i++) {
      let hexString = Buffer.from(new Uint8Array(t[i])).toString('hex');
      outStream.push(hexString);
    }
    outStream.flat();
    let string = outStream.toString(); // Преобразуем в строку
    let result = string.replace(/,/g, ''); // Удаляем запятые
  
    console.log(result); // "Hello world this is JavaScript"
    setOutputValue(result);
  };
  

  return (
    <div className="App">
      <div className="container">
        <h1 className="title">AES Шифрование</h1>
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
            placeholder="Введите текст"
          />
        </div>
        <button className="convert-button" onClick={handleOutputChange}>
          Зашифровать
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

export default Encrypt;
