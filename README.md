# Auto Notes Summarizer

Auto Notes Summarizer is a modern, open-source web application that allows users to upload PDF files or paste text notes and receive high-quality, AI-generated summaries or bullet points. Built with FastAPI, HuggingFace Transformers, and React, it is designed for students, professionals, and researchers who want to quickly distill large documents or notes into concise, actionable insights.

---

## 🚀 Features
- **PDF & Text Summarization:** Upload PDF files or paste text to generate summaries.
- **State-of-the-Art NLP:** Uses Pegasus-XSum, a leading open-source model for abstractive summarization.
- **Chunked Processing:** Handles large documents by splitting them into manageable pieces.
- **Modern UI:** Clean, responsive React frontend.
- **No Paid APIs:** 100% free and open-source, runs locally.
- **Robust Error Handling:** Graceful handling of large files and edge cases.
- **Extensible:** Modular codebase for easy customization and extension.

---

## 🛠️ Tech Stack
- **Backend:** Python, FastAPI, HuggingFace Transformers (Pegasus-XSum), PyPDF2
- **Frontend:** React, Axios
- **Testing:** Python unittest

---

## 🏗️ Architecture

```
[ React Frontend ]  <----HTTP---->  [ FastAPI Backend ]  <---->  [ HuggingFace Transformers ]
        |                                 |                          |
   User uploads PDF/text           Handles API requests        Loads Pegasus-XSum model
   or requests summary             Extracts PDF text           Summarizes text in chunks
                                   Returns summary
```

---

## ⚡ Quickstart

### Backend Setup
```bash
cd backend
python -m venv venv
# Activate the venv:
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
pip install -r app/requirements.txt
uvicorn app.main:app --reload
```

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

---

## 🖥️ Usage
1. Open [http://localhost:3000](http://localhost:3000) in your browser.
2. Upload a PDF or paste your notes.
3. Click **Summarize** to receive a detailed summary.

---

## 🧪 Testing
Run backend unit tests:
```bash
cd backend
python -m unittest discover tests
```

---

## 🤝 Contributing
Contributions are welcome! Please open issues or pull requests for improvements, bug fixes, or new features.

---

## 🙏 Acknowledgments
- [HuggingFace Transformers](https://huggingface.co/transformers/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [React](https://react.dev/)
- [PyPDF2](https://pypdf2.readthedocs.io/)
- [Pegasus-XSum Model](https://huggingface.co/google/pegasus-xsum)

---

## ⭐ Star this repo if you find it useful! 