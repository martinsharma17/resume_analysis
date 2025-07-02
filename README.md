# Smart Resume Analyzer for Job Matching

## 🚀 Project Overview

Smart Resume Analyzer is a Python-based web application that helps job seekers and recruiters by automatically analyzing resumes and matching them with job descriptions. It extracts skills from both resumes and job descriptions, calculates a match percentage, and suggests missing skills to improve job fit.

---

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

## ❓ Interview Questions & Answers

### 1. **What problem does this project solve?**
**Answer:** It automates the process of matching resumes to job descriptions, saving time for recruiters and helping job seekers understand how well they fit a role and what skills they may be missing.

### 2. **How does the system extract skills from resumes and job descriptions?**
**Answer:** It uses spaCy (NLP library) to tokenize the text and matches tokens against a predefined list of skills (from `skills_list.txt`).

### 3. **How is the match percentage calculated?**
**Answer:** The system uses `TfidfVectorizer` to vectorize the extracted skills from both the resume and the job description, then computes the cosine similarity between these vectors to get a match score (as a percentage).

### 4. **Why did you choose Streamlit for the UI?**
**Answer:** Streamlit allows rapid development of interactive data apps using only Python, with no need for HTML/CSS/JS. It automatically launches in the browser and is ideal for prototyping ML/NLP projects.

### 5. **How would you improve or scale this system?**
**Answer:**
- Add a database to store job descriptions and user profiles
- Integrate with external APIs (e.g., Coursera, Udemy) to recommend courses for missing skills
- Use more advanced NLP (e.g., entity recognition, BERT embeddings)
- Deploy as a cloud service for multi-user access

### 6. **What are the limitations of this approach?**
**Answer:**
- Relies on the quality and coverage of the predefined skills list
- Simple keyword matching may miss context or synonyms
- Does not analyze experience depth or soft skills in detail

### 7. **How would you handle synonyms or related skills?**
**Answer:**
- Expand the skills list to include synonyms
- Use word embeddings or semantic similarity to match related skills

### 8. **How secure is the system for user data?**
**Answer:**
- For local use, files are processed and deleted immediately after analysis
- For production, would need to implement secure file handling and possibly encryption

---

## ➕ More Interview Questions & Answers

### 9. **How does the system handle errors, such as unsupported file types or corrupt files?**
**Answer:** The system checks the file extension and only processes PDF or DOCX files. If an unsupported file type is uploaded, it raises a clear error. For corrupt or unreadable files, the parsing functions are wrapped in try-except blocks (recommended for production) to catch and display user-friendly error messages.

### 10. **What are the limitations of using simple keyword matching for skill extraction?**
**Answer:** Simple keyword matching may miss multi-word skills (e.g., "machine learning"), ignore synonyms, or fail to recognize context. It also cannot distinguish between skills mentioned as experience versus those mentioned as interests or in unrelated contexts. More advanced NLP (like entity recognition or contextual embeddings) can address these issues.

### 11. **How would you scale this system for multiple users or large organizations?**
**Answer:** For scalability, deploy the app on a cloud platform (e.g., AWS, Azure, GCP) with a backend server and database. Use containerization (Docker) for portability. Implement user authentication, store resumes/JDs securely, and use asynchronous processing for large files or batch analysis.

### 12. **What alternative approaches could be used for skill extraction?**
**Answer:**
- Named Entity Recognition (NER) models trained on resume/job data
- Pre-trained language models (BERT, RoBERTa) for semantic skill extraction
- Using third-party APIs or ontologies (e.g., ESCO, O*NET) for standardized skill sets

### 13. **How would you deploy this system for real-world use?**
**Answer:**
- Containerize the app with Docker
- Deploy on a cloud service (Heroku, AWS EC2, Azure App Service)
- Set up HTTPS for secure data transfer
- Add logging, monitoring, and error reporting
- Optionally, use a CI/CD pipeline for automated deployment

### 14. **How would you evaluate the accuracy of your skill extraction and matching?**
**Answer:**
- Use labeled datasets of resumes and job descriptions with ground-truth skills
- Measure precision, recall, and F1-score for skill extraction
- For matching, compare system scores with human recruiter assessments

### 15. **How would you handle resumes or JDs in languages other than English?**
**Answer:**
- Use spaCy or other NLP models trained for the target language
- Maintain separate skills lists for each language
- Detect language automatically and route to the appropriate parser/model

### 16. **How would you ensure data privacy and compliance (e.g., GDPR)?**
**Answer:**
- Do not store resumes or personal data longer than necessary
- Provide clear privacy policies and user consent forms
- Use encryption for data in transit and at rest
- Allow users to delete their data on request

### 17. **What would you do if the skills list is missing important or new skills?**
**Answer:**
- Regularly update the skills list based on industry trends
- Allow users or admins to suggest new skills
- Use unsupervised NLP to discover frequently mentioned but unmapped skills

### 18. **How would you add support for parsing other file formats (e.g., TXT, HTML)?**
**Answer:**
- Implement additional parsing functions for each file type
- Detect file type on upload and route to the correct parser
- Ensure consistent text extraction for downstream NLP processing

---

## 📫 Contact
For questions or suggestions, open an issue or contact the maintainer. 