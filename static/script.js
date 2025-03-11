document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("roleDisplay").textContent = localStorage.getItem("userRole");
});

function generateCode() {
    const language = document.getElementById("language").value;
    const question = document.getElementById("question").value;
    const output = document.getElementById("output");

    // Call Flask API
    fetch("/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ question: question, language: language })
    })
    .then(response => response.json())
    .then(data => {
        if (data.answer) {
            output.textContent = data.answer;  // Display generated code
        } else {
            output.textContent = "Error: " + data.error;
        }
    })
    .catch(error => {
        output.textContent = "Error: Could not connect to server.";
    });
}
