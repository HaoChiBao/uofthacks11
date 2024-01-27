// Login.jsx
import React from 'react';
import './Login.css';
import FurbyImage from '../imgs/furby.png';

export default function Login({ onLogin }) {
    return (
        <div className='container'>
            <img src={FurbyImage} className='Furby' alt="Furby" />
            <button onClick={onLogin} className='login-button'>
                Login with Google
            </button>
        </div>
    );
}