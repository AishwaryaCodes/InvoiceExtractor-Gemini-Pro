# 🧾 Multi-Language Invoice Extractor using Gemini 1.5 Pro Vision

An intelligent Streamlit-based web app that uses Google Gemini 1.5 Pro Vision to analyze invoice images and answer user questions in natural language.

---

## 🚀 Features

- 🖼️ Upload invoice images (JPG, JPEG, PNG)
- 💬 Ask custom questions (e.g., "What's the total amount?")
- 🌍 Supports multi-language invoice understanding
- 🧠 Powered by Google's Gemini 1.5 Pro Vision (Multimodal Foundation Model)

---

## 🛠 Tech Stack

- [Streamlit](https://streamlit.io/)
- [Google Generative AI SDK](https://ai.google.dev/)
- [Gemini 1.5 Pro](https://deepmind.google/technologies/gemini/)
- [Pillow (PIL)](https://pillow.readthedocs.io/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 📂 Folder Structure

- invoice-extractor/
  - app.py
  - .env                 ← Not committed (contains API key)
  - requirements.txt     ← Python dependencies
  - .gitignore           ← Excludes files like `.env`, `venv/`, etc.
  - README.md            ← Project documentation

---

## 📦 Installation

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/invoice-extractor.git
cd invoice-extractor

# Windows
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

GOOGLE_API_KEY=your_gemini_api_key_here

streamlit run app.py
```

