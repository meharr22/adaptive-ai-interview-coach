SKILLS = [
    "python",
    "c++",
    "c",
    "javascript",
    "tensorflow",
    "keras",
    "numpy",
    "pandas",
    "matplotlib",
    "sql",
    "mongodb",
    "react",
    "html",
    "css",
    "machine learning",
    "deep learning",
    "nlp",
    "opencv",
    "aws",
    "flask",
    "fastapi",
    "matlab"
]

def extract_skills(text):

    text = text.lower()

    found = []

    for skill in SKILLS:
        if skill in text:
            found.append(skill)

    return found