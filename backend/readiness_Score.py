ROLE_SKILLS = {
    "AI Engineer": [
        "python",
        "machine learning",
        "tensorflow",
        "pytorch",
        "deep learning",
        "sql",
        "docker"
    ]
}

def calculate_readiness(role, skills):

    required = ROLE_SKILLS.get(role, [])

    matched = 0

    for skill in skills:
        if skill.lower() in required:
            matched += 1

    score = int((matched / len(required)) * 100)

    return score