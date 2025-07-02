from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .summarizer import generate_summary, summarize_long_text
from .pdf_utils import extract_text_from_pdf

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/summarize-text/")
def summarize_text(text: str = Form(...)):
    if not text.strip():
        raise HTTPException(status_code=400, detail="Text is empty.")
    summary = generate_summary(text)
    return {"summary": summary}

@app.post("/summarize-pdf/")
def summarize_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="File is not a PDF.")
    pdf_text = extract_text_from_pdf(file.file)
    if not pdf_text.strip():
        raise HTTPException(status_code=400, detail="No extractable text in PDF.")
    try:
        summary = summarize_long_text(pdf_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Summarization failed: {str(e)}")
    return {"summary": summary} 