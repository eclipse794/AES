import React, { useState } from 'react';
import './App.css';
import { Decrypt } from './Decrypt';
import Encrypt from './Encrypt';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faArrowLeft, faArrowRight } from '@fortawesome/free-solid-svg-icons';

function App() {
  const [deen, setDeen] = useState(false);

  return (
    <div>
      <div className="App">
        <div className="component-container">
          {deen ? <Encrypt /> : <Decrypt />}
        </div>
      </div>
      <button 
        className="my-button left-button" 
        title='Режим шифрования' 
        onClick={() => setDeen(!deen)}
      >
        <FontAwesomeIcon icon={faArrowLeft} />
      </button>
      <button 
        className="my-button right-button" 
        title='Режим дешифрования' 
        onClick={() => setDeen(!deen)}
      >
        <FontAwesomeIcon icon={faArrowRight} />
      </button>
    </div>
  );
}

export default App;
