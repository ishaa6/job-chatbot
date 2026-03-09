COMMON_SKILLS = [
    "python",
    "sql",
    "excel",
    "tableau",
    "power bi",
    "aws",
    "docker",
    "kubernetes",
    "machine learning",
    "deep learning",
    "pandas",
    "numpy",
    "statistics",
    "data analysis",
    "react",
    "javascript",
    "java",
    "cloud",
    "api",
    "backend",
    "frontend"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in COMMON_SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills

