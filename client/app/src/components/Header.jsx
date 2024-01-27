import * as React from "react";
import "./Header.css";

export default function Header() {
    return (
        <div className="header-container">
            <div className="label">
                FurMe
            </div>

            <div className="profile">
                <div className="label">Profile</div>
            </div>
        </div>
    );
}