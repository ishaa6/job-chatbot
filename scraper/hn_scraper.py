import requests
from bs4 import BeautifulSoup


def scrape_hn_jobs():

    url = "https://news.ycombinator.com/jobs"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    rows = soup.select("tr.athing")

    for row in rows:

        title_tag = row.select_one(".titleline a")

        if title_tag:

            jobs.append({
                "title": title_tag.text.strip(),
                "company": "HN Company",
                "location": "Remote/Unknown",
                "tags": []
            })

    return jobs