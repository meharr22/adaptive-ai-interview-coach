from readiness_Score import calculate_readiness

skills = [
    "python",
    "tensorflow",
    "sql"
]

print(
    calculate_readiness(
        "AI Engineer",
        skills
    )
)