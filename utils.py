from difflib import get_close_matches

def extract_role(user_input):

    roles = [
        "software engineer",
        "data analyst",
        "data scientist",
        "data engineer",
        "machine learning engineer"
    ]

    text = user_input.lower()

    for role in roles:
        if role in text:
            return role

    words = text.split()

    for word in words:
        match = get_close_matches(word, roles, n=1, cutoff=0.6)
        if match:
            return match[0]

    return None