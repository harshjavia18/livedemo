from flask import Flask, render_template, request, jsonify
import subprocess
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/main")
def main_page():
    return render_template("main.html")

@app.route("/generate", methods=["POST"])
def generate_code():
    try:
        data = request.json
        question = data.get("question", "")
        language = data.get("language", "")

        # Construct the prompt for DeepSeek Coder
        prompt = f"Write a {language} function to {question}"

        # Call the DeepSeek Coder 1.3B model using Ollama
        command = f'ollama run deepseek-coder:1.3b "{prompt}"'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Debugging: Print the raw model output
        print("Model Output:", result.stdout)

        return jsonify({"answer": result.stdout.strip()})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
