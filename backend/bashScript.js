const { exec } = require('child_process');

 exec('sh downloadYoutube.sh "https://www.youtube.com/watch?v=zU9y354XAgM&ab_channel=TimerTopia"',
        (error, stdout, stderr) => {
            console.log(stdout);
            console.log(stderr);
            if (error !== null) {
                console.log(`exec error: ${error}`);
            }
});