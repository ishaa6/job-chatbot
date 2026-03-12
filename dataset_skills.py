import pandas as pd

df = pd.read_csv("dataset.csv")


def get_dataset_skills(role):

    role = role.lower()

    ROLE_INDUSTRY = {
        "data scientist": "AI",
        "machine learning engineer": "AI",
        "ai engineer": "AI",
        "software engineer": "Software",
        "data analyst": "Data",
        "blockchain developer": "Blockchain"
    }

    industry = ROLE_INDUSTRY.get(role)

    if industry is None:
        return []

    filtered = df[df["industry"].str.lower() == industry.lower()]

    skills = []

    for row in filtered["skills_required"].dropna():

        parts = row.split(",")

        for skill in parts:
            skills.append(skill.strip().lower())

    return skills