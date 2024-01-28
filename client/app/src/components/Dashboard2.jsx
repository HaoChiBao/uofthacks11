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


export default function Dashboard2({ token }) {
    return (
        <div className="over-arch">
            <div className="col1">

                <h1>Furby's Dashcam</h1>

                <VideoRoom />

                <div className="controls">
                    <button className="left">left</button>
                    <div className="vertical">
                        <button className="up">up</button>
                        <button className="down">down</button>
                    </div>
                    <button className="right">right</button>
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