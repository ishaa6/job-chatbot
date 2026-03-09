from skill_extractor import COMMON_SKILLS

def suggest_skills(skill_counter):

    ranked_skills = skill_counter.most_common()

    core_skills = [skill for skill, _ in ranked_skills[:3]]

    recommendations = [skill for skill, _ in ranked_skills[3:8]]

    return core_skills, recommendations