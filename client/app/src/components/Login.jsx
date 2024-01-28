// Login.jsx
import React, { useState } from 'react';
import './Login.css';
import FurbyImage from '../imgs/furby.png';
import { useGoogleLogin, GoogleLogin } from '@react-oauth/google';

// import { useGoogleLogin } from '@react-oauth/google';



const Login = ({ onLoginSuccess }) => {
    const [password, setPassword] = useState('');

    const handleLogin = () => {
        // Replace this with your password checking logic
        const hardCodedPassword = 'Glasvin123';

        if (password === hardCodedPassword) {
            // Call the parent component's onLoginSuccess callback
            onLoginSuccess(true);
        } else {
            console.log('Password is incorrect');
        }
    };

    return (
        <div className='container'>
            <img src={FurbyImage} className='Furby' alt="Furby" />

            <input
                type="password"
                className="login-text"
                placeholder="Enter your password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />

            <button className="login-button" onClick={handleLogin}>
                Login
            </button>
        </div>
    );
};

export default Login;