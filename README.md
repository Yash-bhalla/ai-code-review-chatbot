# 🧠 AI Code Review Chatbot (Screenshot-Based)

An AI-powered chatbot that reviews programming code directly from **screenshots**.  
Users can upload an image of their code and interact with the chatbot to receive **errors, improvements, and corrected code** in a beginner-friendly manner.

---

## 📌 Problem Statement

Beginner programmers often struggle with:
- Understanding syntax and logical errors
- Copying or formatting code correctly
- Getting instant feedback or mentorship

Most existing code review tools require text-based input and assume prior experience.

---

## 💡 Solution Overview

This project provides a **chatbot-style AI code reviewer** that:
- Accepts **screenshots of code**
- Understands code visually using a vision-enabled AI model
- Reviews code like a human mentor
- Allows **follow-up questions through chat**

Users do not need to type or format code manually.

---

## ✨ Key Features

- 📸 Screenshot-based code input  
- 💬 Chatbot-style interaction  
- 🧠 Error detection and logic review  
- 🧑‍🏫 Beginner-friendly explanations  
- 🌐 Web-based interface  
- 🔐 Secure API-based AI access  

---

## 🧩 Technology Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** FastAPI (Python)  
- **AI Model:** Vision-enabled LLM via OpenRouter  
- **Deployment:** Render  


---
## 📁 Repository Structure
ai-code-review-chatbot
│   main.py
│   requirements.txt
│
├───templates
│       index.html
│
└───static
        style.css
        
---

## 🧩 Technology Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** FastAPI (Python)  
- **AI Model:** Vision-enabled LLM via OpenRouter  
- **Deployment:** Render

  ---


 ## 🧩 Prerequisites

- Python 3.10 or higher 
- Git  
- OpenRouter API Key

  ---
  
 ## 🔑 Environment Setup

- Generate API key from https://openrouter.ai/keys

- Set environment variable OPENROUTER_API_KEY

- Windows (PowerShell):
- setx OPENROUTER_API_KEY "your_api_key_here"

- Linux / macOS:
- export OPENROUTER_API_KEY="your_api_key_here"
- Restart terminal after setting the key.

---
## ▶️ Local Setup & Run

- Install dependencies
pip install -r requirements.txt

- Start application
uvicorn main:app --reload

- Open browser
http://127.0.0.1:8000

---
## 🧪 How to Use

- Upload a screenshot of your code

- Click Send

- Receive:

- Detected issues

- Bad practices

- Improved code

- Explanation

- Ask follow-up questions via chat

---
## 🌍 Deployment (Render)

- Build Command:
- pip install -r requirements.txt

- Start Command:
- uvicorn main:app --host 0.0.0.0 --port 10000

- Environment Variable:
- OPENROUTER_API_KEY

## 🔮 Future Enhancements

- Multi-language support

- Error severity classification

- Line-by-line explanation mode

- IDE integration

- Voice-based interaction

## 🏁 Conclusion

- The AI Code Review Chatbot reduces common learning barriers by allowing beginners to analyze code directly from screenshots. By combining vision-based AI with a chatbot interface, the system delivers fast, accessible, and meaningful feedback for effective learning.

















