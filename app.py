from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from groq import Groq

app = Flask(__name__)

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY .env file mein nahi mili.")

client = Groq(api_key=api_key)

MODEL = "qwen/qwen3.8-27b"


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ans_query():
    try:
        # Read FormData from index.html
        question = request.form.get("question", "").strip()

        if not question:
            return jsonify({"error": "Please enter a question."}), 400

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "Act like a helpful personal assistant."
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            max_tokens=512
        )

        answer = response.choices[0].message.content.strip()
        return jsonify({"response": answer}), 200

    except Exception:
        app.logger.exception("Error in /ask route")
        return jsonify({
            "error": "Unable to generate an answer. Check the Flask terminal."
        }), 500


@app.route("/summarize", methods=["POST"])
def summarize_email():
    try:
        # Read FormData from index.html
        email_text = request.form.get("email", "").strip()

        if not email_text:
            return jsonify({"error": "Please enter the email text."}), 400

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Act like an expert email assistant. "
                        "Summarize the email in 2-3 sentences, "
                        "including its main purpose and important action items."
                    )
                },
                {
                    "role": "user",
                    "content": email_text
                }
            ],
            max_tokens=512
        )

        summary = response.choices[0].message.content.strip()
        return jsonify({"response": summary}), 200

    except Exception:
        app.logger.exception("Error in /summarize route")
        return jsonify({
            "error": "Unable to summarize the email. Check the Flask terminal."
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
