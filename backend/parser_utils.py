from docx import Document
from pypdf import PdfReader
import io

def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    "Extract text from PDF bytes"
    reader = PdfReader(io.BytesIO(pdf_bytes))
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_text_from_docx(docx_bytes: bytes) -> str:
    "Extract text from DOCX bytes"
    document = Document(io.BytesIO(docx_bytes))
    text = ""
    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"
    return text

def parse_document(file_bytes: bytes, file_type: str) -> str:
    """Parses document bytes based on file type and returns extracted text."""
    if file_type == "application/pdf":
        return extract_text_from_pdf(file_bytes)
    elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return extract_text_from_docx(file_bytes)
    elif file_type == "application/msword": # For .doc files, basic text extraction might be limited
        # You might need a more robust library or external tool for .doc files
        # For hackathon, we might just return raw bytes or indicate unsupported
        return f"Unsupported .doc file type for full parsing. Raw bytes length: {len(file_bytes)}"
    else:
        return "Unsupported file type"