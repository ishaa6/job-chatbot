import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from job_scraper import scrape_jobs
from analyzer import analyze_jobs
from career_advisor import suggest_skills
from utils import extract_role


st.title("AI Career Advisor")

user_input = st.chat_input("Ask about a career")

if user_input:

    st.chat_message("user").write(user_input)

    role = extract_role(user_input)

    if role is None:
        st.chat_message("assistant").write(
            "Sorry, I couldn't detect the job role. Try asking about software engineer, data scientist, etc."
        )
        st.stop()

    jobs = scrape_jobs()

    filtered_jobs = [
        job for job in jobs
        if role in job["title"].lower()
    ]

    st.chat_message("assistant").write(
        f"Analyzing {len(filtered_jobs)} jobs for **{role}**"
    )

    skills = analyze_jobs(filtered_jobs)

    top_skills = skills.most_common(5)

    st.subheader("Top Skills")

    for skill, count in top_skills:
        st.write(f"{skill}".title())

    suggestions = suggest_skills(skills)

    st.subheader("Recommended Skills")

    for skill in suggestions:
        st.write(f"{skill}".title())

    st.subheader("Skill Demand Chart")

    df = pd.DataFrame(top_skills, columns=["Skill", "Count"])

    fig, ax = plt.subplots()

    ax.bar(df["Skill"], df["Count"])

    st.pyplot(fig)