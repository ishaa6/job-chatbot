from job_scraper import scrape_jobs
from analyzer import analyze_jobs
from career_advisor import suggest_skills
from market_insights import top_companies


def chatbot():

    print("\nAI Career Advisor\n")

    jobs = scrape_jobs()
    role = input("Enter a job role: ")

    print("\nFetching jobs...\n")

    filtered_jobs = [
        job for job in jobs
        if role in job["title"].lower()
    ]

    if not filtered_jobs:
        print("No jobs found.")
        return

    print(f"Jobs Found: {len(jobs)}\n")

    companies = top_companies(jobs)

    print("TOP COMPANIES HIRING\n")

    for company, count in companies:
        print(company)

    skills = analyze_jobs(filtered_jobs)

    print("\nTOP SKILLS\n")

    for skill, count in skills.most_common(5):
        print(skill)

    suggestions = suggest_skills(skills)

    print("\nRECOMMENDED SKILLS TO LEARN\n")

    for skill in suggestions:
        print(skill)


chatbot()