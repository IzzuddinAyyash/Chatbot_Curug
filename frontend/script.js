document.getElementById("send-button").addEventListener("click", function() {
    let userInput = document.getElementById("user-input").value;
    if (userInput.trim()) {
        appendMessage("Anda: " + userInput, "user");
        getBotResponse(userInput);
        document.getElementById("user-input").value = "";
    }
});

function appendMessage(message, sender) {
    const chatOutput = document.getElementById("chat-output");
    const messageElement = document.createElement("div");
    messageElement.textContent = message;
    messageElement.className = sender;
    chatOutput.appendChild(messageElement);
    chatOutput.scrollTop = chatOutput.scrollHeight;
}

function getBotResponse(userInput) {
    fetch('http://localhost:5000/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_input: userInput })
    })
    .then(response => response.json())
    .then(data => {
        appendMessage("CurugBot: " + data.bot_response, "bot");
    })
    .catch(error => {
        console.error('Error:', error);
        appendMessage("CurugBot: Maaf, terjadi kesalahan.", "bot");
    });
}
