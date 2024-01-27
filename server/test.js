const moveServo = async (pin, angle) => {
    await fetch('http://127.0.0.1:5000/move_servo', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'pin': pin,
            'angle': angle
        })
    }).then(function(response) {
        response.json().then(function(data) {
            console.log(data);
        })
    })
}

const main = async () => {
    // await moveServo(3, 60);
    // await moveServo(9, 90);

    // return 
    for(let i = 0; i < 180; i++) {
        await moveServo(3, i);
    }
    return
    for(let i = 40; i < 120; i++) {
        await moveServo(9, i);
    }
    

}



main();

// fetch('http://127.0.0.1:5000/get_emotion', {
//     method: 'GET',
//     headers: {
//         'Content-Type': 'application/json'
//     }
// }).then(function(response) {
//     response.json().then(function(data) {
//         console.log(data);
//     })
// })