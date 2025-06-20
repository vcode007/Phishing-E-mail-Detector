# Phishing - E-mail - Detector
A lightweight web app to detect phishing emails using Hugging Face’s zero-shot BART model.

## 🚀 Features

- ✅ Paste any email message and detect if it's **Phishing** or **Legitimate**
- 🔍 Uses `facebook/bart-large-mnli` (zero-shot model) from Hugging Face
- 🌐 Clean and responsive **Tailwind UI** 
- 🧹 Simple Flask backend
- 📊 Can be upgraded with fine-tuned models

## 🛠 Tech Stack
- Frontend: HTML, Tailwind CSS (CDN), Jinja templating
- Backend: Python, Flask
- NLP Model: Hugging Face Transformers (facebook/bart-large-mnli)
- Machine Learning Framework: PyTorch (used by the Transformers model)
- Data: Phishing Email Dataset from Kaggle
- Deployment: Localhost (Flask dev server) — can be extended to Render or Hugging Face Spaces
- Environment: Virtualenv (Python venv)

  
## 📷 Screenshot

![Screenshot 2025-06-20 213257](https://github.com/user-attachments/assets/830c1109-880f-4ff8-8336-7e9623714db3)
