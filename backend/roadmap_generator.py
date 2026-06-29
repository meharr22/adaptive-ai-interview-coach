ROADMAP = {

    "docker":
    "Learn Docker Basics",

    "pytorch":
    "Build a CNN using PyTorch",

    "tensorflow":
    "Master TensorFlow Fundamentals",

    "deep learning":
    "Study CNN, RNN and Transformers",

    "sql":
    "Practice SQL Queries",

    "machine learning":
    "Revise ML Algorithms",

    "mlops":
    "Learn MLOps and Model Deployment"
}


def generate_roadmap(missing_skills):

    roadmap = []

    for skill in missing_skills:

        skill = skill.lower()

        if skill in ROADMAP:
            roadmap.append(
                ROADMAP[skill]
            )

    return roadmap