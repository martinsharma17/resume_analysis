import docx
import PyPDF2
import spacy

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_skills(text, skills_list):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    found_skills = set()
    for token in doc:
        if token.text.lower() in skills_list:
            found_skills.add(token.text.lower())
    return list(found_skills)

def parse_resume(file_path, file_type, skills_list):
    if file_type == "pdf":
        text = extract_text_from_pdf(file_path)
    elif file_type == "docx":
        text = extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file type")
    skills = extract_skills(text, skills_list)
    return text, skills 