import { VideoRoom } from './components/VideoRoom';
import { useState, React } from 'react';
import { useGoogleLogin, GoogleLogin } from '@react-oauth/google';
import './App.css';
import Star from './components/Star';
import Login from './components/Login';
import Header from './components/Header';
import Dashboard from './components/Dashboard';

function App() {
    const [joined, setJoined] = useState(false);
    const [login, setLogin] = useState(false);
    const [token, setToken] = useState(null);

    const handleLoginSuccess = () => {

        setLogin(true);
    };

    return (
        <div className="App">
            <Header />
            <div className='content'>

                {!login && (
                    <Login onLoginSuccess={handleLoginSuccess} />
                )}

                {!joined && login && (
                    <>
                        <Dashboard token={token} />
                        <button className='content-button ' onClick={() => setJoined(true)}>Watch Surveillance</button>
                    </>
                )}

                {joined && <VideoRoom />}

            </div>

            <Star height="60vh" bottom="0" right="400px" />
            <Star height="55vh" bottom="250px" right="-550px" rotate="-130" />
        </div>
    );
}

export default App;