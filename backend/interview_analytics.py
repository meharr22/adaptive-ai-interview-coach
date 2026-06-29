def generate_interview_report(session):

    avg = (
        sum(session["scores"])
        /
        len(session["scores"])
    )

    if avg >= 8:
        verdict = "Excellent"
        level = "Hard"
        readiness = "90%"
        strength = "Strong Technical Understanding"
        weakness = "Minor Optimization Areas"

    elif avg >= 6:
        verdict = "Good"
        level = "Medium"
        readiness = "75%"
        strength = "Fundamental Concepts"
        weakness = "Advanced Concepts"

    else:
        verdict = "Needs Improvement"
        level = "Easy"
        readiness = "50%"
        strength = "Basic Understanding"
        weakness = "Core Technical Concepts"

    return {

        "questions_attempted":
        session["questions_attempted"],

        "average_score":
        round(avg, 2),

        "verdict":
        verdict,

        "recommended_level":
        level,

        "interview_readiness":
        readiness,

        "strength":
        strength,

        "weakness":
        weakness
    }