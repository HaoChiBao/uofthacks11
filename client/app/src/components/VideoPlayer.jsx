import React, { useEffect, useRef } from 'react'

import './VideoPlayer.css';

export const VideoPlayer = ({ user, zIndex }) => {

    const ref = useRef();

    useEffect(() => {
        user.videoTrack.play(ref.current)
    }, []);

    return (
        <div className='video-player'>
            <div
                ref={ref}
                style={{ width: '32vw', height: '40vh', borderRadius: '50px', zIndex: zIndex }}
            ></div>
        </div>
    )
}