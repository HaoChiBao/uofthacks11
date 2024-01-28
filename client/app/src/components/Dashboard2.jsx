import * as React from "react";
import "./Dashboard.css";
import Chat from "./Chat";

import { VideoRoom } from './VideoRoom';

const eventsList = [
    { title: "Western Voice!", date: "2024-02-03", description: "CSA's Flagship Event" },
    { title: "Art Exhibition", date: "2024-03-15", description: "Explore diverse art pieces from local artists" },
    { title: "Food Festival", date: "2024-04-01", description: "A culinary adventure with delicious cuisines" },
    // Add more events as needed
];

const firebaseConfig = {
    apiKey: "AIzaSyA5_6MeslRHd-zTd2xiqYKUpsajf4GmxQY",
    authDomain: "uofthacks11-3aaad.firebaseapp.com",
    databaseURL: "https://uofthacks11-3aaad-default-rtdb.firebaseio.com/",
    projectId: "uofthacks11-3aaad",
    storageBucket: "uofthacks11-3aaad.appspot.com",
    messagingSenderId: "638732020721",
    appId: "1:638732020721:web:69cdc8ef8d4f6f2d953250"
};

const directionON = async (e) => {
    if (!e) return;

    console.log(e.target.className)
    const direction = e.target.className
    // return

    try {
        const response = await fetch(`${firebaseConfig.databaseURL}/control.json`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ direction: direction }),
        }).then((response) => response.json()).then((data) => {
            console.log('Success:', data);
        }).catch((error) => {
            console.error('Error:', error);
        })
    } catch (e) {
        console.log(e)
    }
};
const directionOFF = async (direction) => {
    try {
        const response = await fetch(`${firebaseConfig.databaseURL}/control.json`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ direction: 'stop' }),
        }).then((response) => response.json()).then((data) => {
            console.log('Success:', data);
        }).catch((error) => {

        })
    } catch (e) {
        console.log(e)
    }
}

export default function Dashboard2({ token }) {
    return (
        <div className="over-arch">
            <div className="col1">

                <h1>Furby's Dashcam</h1>

                <VideoRoom />

                <div className="controls">
                    <button className="left" onMouseDown={directionON} onMouseUp={directionOFF}>left</button>
                    <div className="vertical">
                        <button className="up" onMouseDown={directionON} onMouseUp={directionOFF}>up</button>
                        <button className="down" onMouseDown={directionON} onMouseUp={directionOFF}>down</button>
                    </div>
                    <button className="right" onMouseDown={directionON} onMouseUp={directionOFF}>right</button>
                </div>

            </div>
            <div className="col2">
                <div>
                    <h1>Chat With Furby</h1>

                    <Chat />
                </div>

            </div>

        </div>
    );
}