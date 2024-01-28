import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';


import { GoogleOAuthProvider } from '@react-oauth/google';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <GoogleOAuthProvider clientId="576204146886-b7ouu72ge1i8fnco49v5gi23tb3le7fn.apps.googleusercontent.com">
        <App />
    </GoogleOAuthProvider>
);
