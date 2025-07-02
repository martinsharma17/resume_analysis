import streamlit as st
import os
import tempfile
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.badges import badge
from streamlit_extras.let_it_rain import rain

from parsers.resume_parser import parse_resume
from parsers.jd_parser import extract_skills_from_jd
from matching.matcher import calculate_match
from suggestions.suggester import suggest_missing_skills

# --- Sidebar ---
st.sidebar.image("https://img.icons8.com/color/96/000000/resume.png", width=80)
st.sidebar.title("Smart Resume Analyzer")
st.sidebar.markdown("""
**Project:** Smart Resume Analyzer for Job Matching\
**By:** Your Name

---

- Upload your resume (PDF/DOCX)
- Paste a job description
- Get instant match analysis!

[GitHub](https://github.com/) | [LinkedIn](https://linkedin.com/)
""")

# --- Main UI ---
st.markdown("""
<style>
.big-font { font-size:32px !important; font-weight: bold; }
.result-box { background: #f0f6ff; border-radius: 10px; padding: 20px; margin-bottom: 20px; }
.skill-chip { display: inline-block; background: #e0e0e0; border-radius: 20px; padding: 5px 15px; margin: 2px; font-size: 15px; }
.missing-skill { background: #ffe0e0; color: #b00020; }
.footer { text-align: center; color: #888; font-size: 14px; margin-top: 40px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-font">🔍 Smart Resume Analyzer for Job Matching</div>', unsafe_allow_html=True)
st.write(":rocket: Instantly see how well your resume matches a job description!")

add_vertical_space(1)

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("1️⃣ Upload Resume")
    resume_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])

with col2:
    st.subheader("2️⃣ Paste Job Description")
    jd_text = st.text_area("Paste the Job Description here", height=180)

add_vertical_space(1)

analyze_btn = st.button("✨ Analyze Match", use_container_width=True)

if analyze_btn and resume_file and jd_text:
    with st.spinner("Analyzing your resume and job description..."):
        with tempfile.NamedTemporaryFile(delete=False, suffix="." + resume_file.name.split('.')[-1]) as tmp_file:
            tmp_file.write(resume_file.read())
            tmp_path = tmp_file.name

        file_type = resume_file.name.split('.')[-1].lower()
        resume_text, resume_skills = parse_resume(tmp_path, file_type, [s.strip().lower() for s in open("data/skills_list.txt")])
        jd_skills = extract_skills_from_jd(jd_text, [s.strip().lower() for s in open("data/skills_list.txt")])
        match_score = calculate_match(resume_skills, jd_skills)
        missing_skills = suggest_missing_skills(resume_skills, jd_skills)
        os.remove(tmp_path)

    rain(emoji="🎉", font_size=30, falling_speed=5, animation_length="infinite")

    st.markdown(f'<div class="result-box"><h3>📊 Match Score: <span style="color:#1976d2">{match_score}%</span></h3></div>', unsafe_allow_html=True)

    st.markdown('<div class="result-box"><b>✅ Your Skills:</b><br>' +
        ' '.join([f'<span class="skill-chip">{s}</span>' for s in resume_skills]) + '</div>', unsafe_allow_html=True)

    st.markdown('<div class="result-box"><b>📋 JD Skills:</b><br>' +
        ' '.join([f'<span class="skill-chip">{s}</span>' for s in jd_skills]) + '</div>', unsafe_allow_html=True)

    if missing_skills:
        st.markdown('<div class="result-box"><b>⚠️ Missing Skills:</b><br>' +
            ' '.join([f'<span class="skill-chip missing-skill">{s}</span>' for s in missing_skills]) + '</div>', unsafe_allow_html=True)
    else:
        st.success("🎯 No missing skills! You're a great match!")

    badge(type="github", name="Smart Resume Analyzer")

st.markdown('<div class="footer">© 2024 Smart Resume Analyzer | Built with ❤️ using Streamlit</div>', unsafe_allow_html=True) 