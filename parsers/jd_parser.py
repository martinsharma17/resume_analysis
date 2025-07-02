import spacy

def extract_skills_from_jd(jd_text, skills_list):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(jd_text)
    found_skills = set()
    for token in doc:
        if token.text.lower() in skills_list:
            found_skills.add(token.text.lower())
    return list(found_skills) 