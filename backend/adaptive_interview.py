import re

def get_next_difficulty(score):

    if score >= 8:
        return "Hard"

    elif score >= 5:
        return "Medium"

    else:
        return "Easy"


def get_score_from_evaluation(evaluation):

    match = re.search(
    r"(\d+)/10",
    evaluation
)

    if match:
        return int(match.group(1))

    return 5