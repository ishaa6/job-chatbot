from collections import Counter

def top_companies(jobs, top_n=5):
    companies = [job["company"] for job in jobs]
    company_counter = Counter(companies)
    return company_counter.most_common(top_n)