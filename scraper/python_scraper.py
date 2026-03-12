import requests
from bs4 import BeautifulSoup


def scrape_python_jobs():

    url = "https://www.python.org/jobs/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    listings = soup.select(".list-recent-jobs li")

    for job in listings:

        title = job.select_one("h2 a")
        company = job.select_one(".listing-company-name")
        location = job.select_one(".listing-location")

        if title:

            jobs.append({
                "title": title.text.strip(),
                "company": company.text.strip() if company else "Unknown",
                "location": location.text.strip() if location else "Unknown",
                "tags": []
            })

    return jobs