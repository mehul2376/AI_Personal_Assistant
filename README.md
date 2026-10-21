# AI Personal Assistant 🤖

An AI-powered personal assistant built using Python, Flask, and the Groq API. It helps users get answers to questions and summarize emails through a simple web interface.

## ✨ Features

- **Ask Anything:** Get AI-generated answers to general questions.
- **Email Summarization:** Summarize lengthy emails into 2–3 sentences.
- **Simple Web Interface:** Built with HTML, CSS, and JavaScript.
- **Secure API Key Management:** Uses environment variables to protect API credentials.
- **Loading Indicators:** Displays processing status while generating responses.

## 🛠️ Tech Stack

- **Language:** Python
- **Backend:** Flask
- **AI API:** Groq API
- **Model:** `qwen/qwen3.8-27b`
- **Frontend:** HTML, CSS, JavaScript
- **Environment Variables:** python-dotenv

## 📁 Project Structure

```text
AI_Personal_Assistant/
├── app.py
├── .env
├── .gitignore
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/mehul2376/AI_Personal_Assistant.git
cd AI_Personal_Assistant
```

### 2. Install dependencies

```bash
pip install flask groq python-dotenv
```

### 3. Configure the API key

Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace `your_groq_api_key_here` with your own Groq API key.

Get an API key from the [Groq Console](https://console.groq.com/keys).

### 4. Run the application

```bash
python app.py
```

Open this URL in your browser:

```text
http://127.0.0.1:5000/
```

## 🚀 How to Use

1. Open the application in your browser.
2. Enter a question in the **Ask Anything** section.
3. Click **Ask** to receive an AI-generated answer.
4. Paste an email into the **Summarize Email** section.
5. Click **Summarize** to get a concise summary.

## 🔐 Security

- Keep your API key in the `.env` file.
- Never commit `.env` or expose API keys in source code or notebooks.
- Add `.env` to `.gitignore`.

## 👨‍💻 Author

**Mehul Kumar**

GitHub: [mehul2376](https://github.com/mehul2376)

## 📄 License

This project is available for learning and educational purposes. Add a license file if you intend to distribute it under a specific open-source license.
