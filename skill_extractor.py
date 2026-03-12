COMMON_SKILLS = [
"python","sql","aws","gcp","azure","docker","kubernetes",
"pandas","numpy","spark","hadoop","airflow",
"tensorflow","pytorch","machine learning",
"excel","tableau","power bi",
"react","javascript","java","c++","golang"
]

DEFAULT_SKILLS = {
    "data scientist": ["python","machine learning","sql","pandas","statistics"],
    "data analyst": ["sql","excel","python","power bi","statistics"],
    "software engineer": ["python","java","javascript","git","docker","aws"],
    "machine learning engineer": ["python","pytorch","tensorflow","docker","kubernetes","mlops"]
}

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in COMMON_SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills

