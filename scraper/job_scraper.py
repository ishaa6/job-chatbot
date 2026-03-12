import requests

def scrape_jobs():

    url = "https://remoteok.com/api"

    response = requests.get(url)

    data = response.json()

    jobs = []

    for job in data[1:]:

        jobs.append({
            "title": job.get("position",""),
            "company": job.get("company",""),
            "location": job.get("location","Remote"),
            "tags": job.get("tags",[])
        })

    return jobs