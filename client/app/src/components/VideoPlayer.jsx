import React, { useEffect, useRef } from 'react'

import './VideoPlayer.css';

export const VideoPlayer = ({ user }) => {

    const ref = useRef();

    useEffect(() => {
        user.videoTrack.play(ref.current)
    }, []);

    return (
        <div className='video-player'>
            <div
                ref={ref}
                style={{ width: '40vw', height: '44vh', borderRadius: '50px' }}
            ></div>
        </div>
    )
}