import { VideoRoom } from './components/VideoRoom';
// import {useState} from React
import { useState, React, useRef } from 'react';
import './App.css';
import Star from './components/Star';
import Login from './components/Login';

import Header from './components/Header';

function App() {
    const [joined, setJoined] = useState(false);

    const [login, setLogin] = useState(false);

    const handleLogin = () => {
        setLogin(true);
    };

    return (

        <div className="App">

            <Header />

            <div className='content'>

                {!login && (
                    <Login onLogin={handleLogin} />
                )}

                {!joined && login && (
                    <button onClick={() => setJoined(true)}>Watch Survillence</button>

                )}

                {joined && <VideoRoom />}
            </div>

            <Star height="60vh" bottom="0" right="400px" />

            <Star height="55vh" bottom="250px" right="-550px" rotate="-130" />

        </div>
    );
}

export default App;