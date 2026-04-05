<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://telegram.org"></script>
    <style>
        body { background: #1a1a1a; color: gold; font-family: sans-serif; text-align: center; margin: 0; }
        .header { background: #000; padding: 20px; border-bottom: 2px solid gold; font-size: 20px; }
        .wheel-area { padding: 40px; font-size: 50px; background: #222; margin: 10px; border-radius: 50%; border: 5px solid #444; }
        .timer { color: red; font-weight: bold; }
        .bet-buttons { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; padding: 10px; }
        button { background: #333; color: white; border: 1px solid gold; padding: 15px; border-radius: 10px; }
        .nav { position: fixed; bottom: 0; width: 100%; display: flex; background: #000; }
        .nav div { flex: 1; padding: 20px; border-top: 1px solid gold; }
        #numbers { display: grid; grid-template-columns: repeat(6, 1fr); gap: 5px; padding: 10px; }
    </style>
</head>
<body>

<div class="header">Баланс: <span id="balance">Загрузка...</span>$</div>

<div id="game-page">
    <div class="timer" id="timer">Ставки: 20с</div>
    <div class="wheel-area" id="result">?</div>
    <div id="status">Выберите ставку</div>
    
    <div class="bet-buttons">
        <button onclick="setBet('red')" style="background: red">КРАСНОЕ</button>
        <button onclick="setBet('black')" style="background: black">ЧЕРНОЕ</button>
    </div>
    <div id="numbers"></div>
</div>

<div id="profile-page" style="display:none; padding: 20px;">
    <h2>Профиль</h2>
    <p>Ваш ID: <span id="my-id"></span></p>
    <button onclick="alert('Отправьте ID админу для пополнения')">ПОПОЛНИТЬ</button>
</div>

<div class="nav">
    <div onclick="showPage('game')">ИГРЫ</div>
    <div onclick="showPage('profile')">ПРОФИЛЬ</div>
</div>

<script>
    const tg = window.Telegram.WebApp;
    const userId = tg.initDataUnsafe.user?.id || 12345; // Тестовый ID
    let balance = 0;
    let currentBet = null;
    let timeLeft = 20;

    // Загрузка баланса с сервера
    async def loadBalance() {
        let response = await fetch(`/get_balance?user_id=${userId}`);
        let data = await response.json();
        balance = data.balance;
        document.getElementById('balance').innerText = balance;
        document.getElementById('my-id').innerText = userId;
    }

    function setBet(type) {
        if (timeLeft < 3) return;
        currentBet = type;
        document.getElementById('status').innerText = "Ставка: " + type;
    }

    // Логика игры
    setInterval(() => {
        if (timeLeft > 0) {
            timeLeft--;
            document.getElementById('timer').innerText = `Ставки: ${timeLeft}с`;
        } else {
            spin();
            timeLeft = 20;
        }
    }, 1000);

    async function spin() {
        const res = Math.floor(Math.random() * 37);
        document.getElementById('result').innerText = res;
        
        let winAmount = 0;
        if (currentBet === 'red' && [1,3,5].includes(res)) winAmount = 100; // Пример
        else if (currentBet === 'black' && [2,4,6].includes(res)) winAmount = 100;
        else if (currentBet === res) winAmount = 3500;
        else if (currentBet) winAmount = -100;

        if (winAmount !== 0) {
            await fetch('/update_balance', {
                method: 'POST',
                body: JSON.stringify({user_id: userId, amount: winAmount})
            });
            loadBalance();
        }
        currentBet = null;
        document.getElementById('status').innerText = winAmount > 0 ? "ПОБЕДА!" : "ПРОИГРЫШ";
    }

    function showPage(p) {
        document.getElementById('game-page').style.display = p === 'game' ? 'block' : 'none';
        document.getElementById('profile-page').style.display = p === 'profile' ? 'block' : 'none';
    }

    loadBalance();
    tg.expand();
</script>
</body>
</html>
