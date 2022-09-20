const buttonAll = document.querySelector('#lotto-btn-all')
const button = document.querySelector('#lotto-btn');

buttonAll.addEventListener('click', function () {
    const count = prompt('한 번에 구매할 로또의 개수를 입력하세요! (5 이하)');
    const result = document.querySelector('#result');

    if ((parseInt(result.childNodes.length) + parseInt(count)) > 5) {
        const result = document.querySelector('#result');

        for (let k = 0; k < count; k++) {
            result.removeChild(result.lastChild);
        }

        for (let i = 0; i < count; i++) {
            const ballContainer = document.createElement('div');
            ballContainer.classList.add('ball-container');

            const numbers = _.sampleSize(_.range(1, 46), 6)
            numbers.sort((a, b) => (a - b));

            for (let j = 0; j < numbers.length; j++) {
                const ball = document.createElement('div');

                ball.classList.add('ball');
                ball.innerText = numbers[j];

                switch (parseInt((numbers[j] - 1) / 10)) {
                    case 0:
                        ball.classList.add('ball-color-1');
                        break
                    case 1:
                        ball.classList.add('ball-color-2');
                        break
                    case 2:
                        ball.classList.add('ball-color-3');
                        break
                    case 3:
                        ball.classList.add('ball-color-4');
                        break
                    case 4:
                        ball.classList.add('ball-color-5');
                        break
                }

                ballContainer.appendChild(ball);
            }
            result.prepend(ballContainer);
        }
    }
    else {
        for (let i = 0; i < count; i++) {
            const ballContainer = document.createElement('div');
            ballContainer.classList.add('ball-container');

            const numbers = _.sampleSize(_.range(1, 46), 6)
            numbers.sort((a, b) => (a - b));

            for (let j = 0; j < numbers.length; j++) {
                const ball = document.createElement('div');

                ball.classList.add('ball');
                ball.innerText = numbers[j];

                switch (parseInt((numbers[j] - 1) / 10)) {
                    case 0:
                        ball.classList.add('ball-color-1');
                        break
                    case 1:
                        ball.classList.add('ball-color-2');
                        break
                    case 2:
                        ball.classList.add('ball-color-3');
                        break
                    case 3:
                        ball.classList.add('ball-color-4');
                        break
                    case 4:
                        ball.classList.add('ball-color-5');
                        break
                }

                ballContainer.appendChild(ball);
            }
            result.prepend(ballContainer);
        }
    }
})

button.addEventListener('click', function () {
    const ballContainer = document.createElement('div');
    ballContainer.classList.add('ball-container');

    const numbers = _.sampleSize(_.range(1, 46), 6)
    numbers.sort((a, b) => (a - b));

    for (let i = 0; i < numbers.length; i++) {
        const ball = document.createElement('div');

        ball.classList.add('ball');
        ball.innerText = numbers[i];

        switch (parseInt((numbers[i] - 1) / 10)) {
            case 0:
                ball.classList.add('ball-color-1');
                break
            case 1:
                ball.classList.add('ball-color-2');
                break
            case 2:
                ball.classList.add('ball-color-3');
                break
            case 3:
                ball.classList.add('ball-color-4');
                break
            case 4:
                ball.classList.add('ball-color-5');
                break
        }

        ballContainer.appendChild(ball);
    }
    const result = document.querySelector('#result');

    result.insertBefore(ballContainer, result.firstChild);

    if (result.childNodes.length > 5) {
        const result = document.querySelector('#result');
        result.removeChild(result.lastChild);
    }
})