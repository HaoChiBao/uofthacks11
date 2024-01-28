import * as React from "react";
import "./Dashboard.css";
import Chat from "./Chat";



export default function Dashboard({ token }) {
    return (
        <div className="over-arch">
            <div className="col1">
                <h1>Welcome to your FurMe Dashboard!</h1>
                <div className="content-box">
                    <ul className="dashboard-list">
                        <li>View your upcoming events</li>
                        <li>Create your to-dos</li>
                        <li>Listen to Spotify</li>
                        <li>Check the Weather</li>
                        <li>Observe your desk</li>
                    </ul>

                </div>
                <div>
                    <h1>Furby's Favourite Jams</h1>

                    <iframe
                        style={{ borderRadius: '12px', border: 'none' }}
                        src="https://open.spotify.com/embed/playlist/1WlOv6eswLOHWXIiBzYGu4?utm_source=generator"
                        width="100%"
                        height="180px"
                        border="none"
                        background-color="transparent"
                        allowfullscreen=""
                        allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
                        loading="lazy"
                    ></iframe>

                </div>

            </div>
            <div className="col2">
                <div>
                    <h1>Chat With Furby</h1>

                    <Chat />
                </div>
                <div>

                </div>
            </div>

        </div>
    );
}