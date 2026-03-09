from collections import Counter
from skill_extractor import extract_skills


def analyze_jobs(jobs):

    skill_counter = Counter()

    for job in jobs:

        text = job["title"] + " " + " ".join(job.get("tags", []))
        skills = extract_skills(text)
        skill_counter.update(skills)

    return skill_counter