import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

from scraper.job_scraper import scrape_jobs
from scraper.python_scraper import scrape_python_jobs
from scraper.hn_scraper import scrape_hn_jobs

from analyzer import analyze_jobs
from utils import extract_role
from dataset_skills import get_dataset_skills
from skill_extractor import DEFAULT_SKILLS


st.set_page_config(page_title="AI Career Advisor", layout="wide")

st.title("AI Career Advisor")
st.caption("Discover skills and job opportunities for your desired tech career")

user_input = st.chat_input("Ask about a career")


if user_input:

    st.chat_message("user").write(user_input)

    role = extract_role(user_input)

    if role is None:
        st.chat_message("assistant").write(
            "Sorry, I couldn't detect the job role."
        )
        st.stop()

    # -----------------------------
    # SCRAPE JOBS
    # -----------------------------

    with st.spinner("Collecting job data..."):

        jobs_remote = scrape_jobs()
        jobs_python = scrape_python_jobs()
        jobs_hn = scrape_hn_jobs()

        jobs = jobs_remote + jobs_python + jobs_hn

    # Job metrics
    col1, col2, col3 = st.columns(3)

    col1.metric("RemoteOK Jobs", len(jobs_remote))
    col2.metric("Python.org Jobs", len(jobs_python))
    col3.metric("HN Jobs", len(jobs_hn))


    # -----------------------------
    # FILTER JOBS
    # -----------------------------

    role_words = role.lower().split()

    filtered_jobs = [
        job for job in jobs
        if any(word in job["title"].lower() for word in role_words)
    ]

    if len(filtered_jobs) == 0:

        st.warning(f"No jobs found for **{role}**")
        st.stop()

    st.success(f"Analyzing **{len(filtered_jobs)} jobs** for **{role.title()}**")


    # -----------------------------
    # SKILL ANALYSIS
    # -----------------------------

    skills_scraped = analyze_jobs(filtered_jobs)

    dataset_skills = get_dataset_skills(role)

    dataset_counter = Counter(set(dataset_skills))

    skills = skills_scraped + dataset_counter


    # -----------------------------
    # RECOMMENDED SKILLS
    # -----------------------------

    recommended = DEFAULT_SKILLS.get(
        role.lower(),
        ["python","sql","aws","docker","git"]
    )


    if len(skills) < 3:

        st.info("Using standard skill recommendations.")

        recommended = list(set(recommended + [skill for skill,_ in skills.most_common()]))

        chart_skills = [(skill,1) for skill in recommended[:8]]

    else:

        recommended = [skill for skill,_ in skills.most_common(10)]

        chart_skills = skills.most_common(8)


    # -----------------------------
    # SKILLS + CHART LAYOUT
    # -----------------------------

    col1, col2 = st.columns([1,2])


    # -------- Recommended skills

    with col1:

        st.subheader("Recommended Skills")

        for skill in recommended:

            st.markdown(
                f"""
                <div style="
                padding:6px 12px;
                margin:5px 0;
                border-radius:8px;
                background:#eef2ff;
                display:inline-block;">
                {skill.title()}
                </div>
                """,
                unsafe_allow_html=True
            )


    # -------- Skill chart

    with col2:

        st.subheader("Skill Demand Chart")

        df = pd.DataFrame(chart_skills, columns=["Skill","Count"])

        df["Skill"] = df["Skill"].str.title()

        total = df["Count"].sum()

        df["Importance"] = (df["Count"]/total)*100


        fig, ax = plt.subplots()

        ax.bar(df["Skill"], df["Importance"], color="#6366F1")

        ax.set_ylabel("Relative Importance (%)")

        ax.set_xlabel("Skills")

        ax.set_title(f"Skill Importance for {role.title()}")

        plt.xticks(rotation=30)

        st.pyplot(fig)


    # -----------------------------
    # JOB LIST
    # -----------------------------

    st.divider()

    st.subheader("Job Opportunities")


    job_container = st.container(height=450)


    with job_container:

        for job in filtered_jobs[:30]:

            title = job.get("title", "Unknown Job")
            company = job.get("company", "Unknown Company")
            location = job.get("location") or "Remote"
            link = job.get("url")

            with st.container():

                col1, col2 = st.columns([4,1])

                with col1:

                    st.markdown(f"**{title}**")

                    st.caption(f"🏢 {company}  |  📍 {location}")

                with col2:

                    if link:
                        st.link_button("View", link)

                st.divider()