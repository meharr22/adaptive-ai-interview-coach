def get_question_level(readiness_score):

    if readiness_score < 40:
        return "Easy"

    elif readiness_score < 70:
        return "Medium"

    else:
        return "Hard"