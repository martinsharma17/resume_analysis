# Smart Resume Analyzer for Job Matching

## 🚀 Project Overview

Smart Resume Analyzer is a Python-based web application that helps job seekers and recruiters by automatically analyzing resumes and matching them with job descriptions. It extracts skills from both resumes and job descriptions, calculates a match percentage, and suggests missing skills to improve job fit.

Live: https://resumeanalysisbymartinsharma.streamlit.app/


## 🛠️ How the System Works

1. **Resume Upload**: User uploads a PDF or DOCX resume.
2. **Resume Parsing**: The system extracts text and skills from the resume using NLP.
3. **Job Description Input**: User pastes a job description into the app.
4. **JD Parsing**: The system extracts required skills from the job description.
5. **Matching Engine**: Compares resume skills with JD skills using TF-IDF and cosine similarity to compute a match score.
6. **Suggestions**: Lists missing skills and suggests improvements.
7. **Results Display**: Shows match percentage, extracted skills, and missing skills in an attractive UI.

---

## 🔄 System Flow

1. **User Interface (Streamlit Web App)**
    - Upload resume
    - Paste job description
    - Click "Analyze Match"
2. **Resume Parser**
    - Extracts text from PDF/DOCX
    - Extracts skills using spaCy NLP and a predefined skills list
3. **JD Parser**
    - Extracts skills from job description text
4. **Matching Engine**
    - Vectorizes skills using TfidfVectorizer
    - Calculates similarity score
5. **Suggestions Engine**
    - Identifies missing skills
6. **Results**
    - Displays match score, skills, and suggestions

**Visual Flow:**

```
[User Uploads Resume & JD] 
        | 
        v
[Resume Parser] <--- [skills_list.txt] ---> [JD Parser]
        |                        |
        v                        v
   [Extracted Skills]      [Extracted JD Skills]
        |                        |
        +----------+-------------+
                   |
                   v
           [Matching Engine]
                   |
                   v
           [Suggestions Engine]
                   |
                   v
              [Results UI]
```

---

## ⚙️ Setup & Usage

1. **Clone the repository**
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   pip install streamlit-extras
   ```
3. **Run the app:**
   ```sh
   streamlit run app.py
   ```
4. **Open in your browser** (Streamlit will do this automatically)

---

## 🧑‍💻 Example Usage

- Upload your resume (PDF/DOCX)
- Paste a job description
- Click "✨ Analyze Match"
- View your match score, extracted skills, and missing skills

---

## ❓  for prototyping ML/NLP projects.


