const main = async () => {
    for(let i = 0; i < 180; i++) {

        await fetch('http://127.0.0.1:5000/move_servo', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                'pin': 9,
                'angle': i
            })
        }).then(function(response) {
            response.json().then(function(data) {
                console.log(data);
            })
        })
    }
}

main();
