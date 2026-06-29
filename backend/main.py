from fastapi import FastAPI, UploadFile, File
from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from gap_detector import find_skill_gap
from gemini_generator import generate_ai_questions
import tempfile
from interview_analytics import (
    generate_interview_report
)
from readiness_Score import calculate_readiness
from adaptive_engine import get_question_level
from answer_evaluator import evaluate_answer
from roadmap_generator import generate_roadmap
from adaptive_interview import (
    get_next_difficulty,
    get_score_from_evaluation
)
from auth import (
    hash_password,
    verify_password,
    create_token
)

from database import (
    create_user,
    get_user
)
from interview_session import (
    create_session,
    update_session,
    get_session,
    save_history_to_db,
    get_history_from_db
)
from ai_analytics import generate_ai_report
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend Running"}
@app.post("/upload-resume")
async def upload_resume(
    target_role: str,
    company: str,
    file: UploadFile = File(...)):
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    content = await file.read()
    temp_file.write(content)
    temp_file.close()
    text = extract_text_from_pdf(temp_file.name)
    skills = extract_skills(text)
    missing = find_skill_gap(
    skills,
    target_role)
    readiness_score = calculate_readiness(
    target_role,
    skills)
    difficulty = get_question_level(
    readiness_score)
    questions = generate_ai_questions(
    target_role,
    skills,
    missing,
    difficulty,
    company
)
    roadmap = generate_roadmap(
    missing
)
    return {
    "target_role": target_role,
    "company": company,
    "skills": skills,
    "missing_skills": missing,
    "readiness_score": readiness_score,
    "difficulty": difficulty,
    "roadmap": roadmap,
    "questions": questions
}

@app.post("/evaluate-answer")
async def evaluate_interview_answer(
    question: str,
    answer: str
):
    result = evaluate_answer(
        question,
        answer
    )

    return {
        "evaluation": result
    }
@app.post("/adaptive-interview")
async def adaptive_interview(
    question: str,
    answer: str
):

    evaluation = evaluate_answer(
        question,
        answer
    )

    score = get_score_from_evaluation(
        evaluation
    )

    next_level = get_next_difficulty(
        score
    )
    
    next_question = generate_ai_questions(
    "AI Engineer",
    [],
    [],
    next_level,
    "Generic"
)
    return {
    "evaluation": evaluation,
    "score": score,
    "next_difficulty": next_level,
    "next_question": next_question
}
@app.post("/start-interview")
async def start_interview():

    session_id = create_session()

    return {
        "session_id": session_id
    }
@app.post("/update-session")
async def update_interview(
    session_id: str,
    score: int
):

    avg = update_session(
        session_id,
        score
    )

    return {
        "average_score": avg,
        "session": get_session(
            session_id
        )
    }
@app.get("/interview-report")
async def interview_report(
    session_id: str
):

    session = get_session(
        session_id
    )

    if session is None:
        return {
            "error": "Session not found"
        }

    report = generate_interview_report(
        session
    )

   
    save_history_to_db(
    session_id,
    report
)
    ai_feedback = generate_ai_report(
    report
)
    
    return {
    "report": report,
    "ai_feedback": ai_feedback
}

@app.get("/db-history")
async def db_history():

    return {
        "history": get_history_from_db()
    }

@app.post("/register")
async def register(
    username: str,
    password: str
):

    hashed = hash_password(
        password
    )

    create_user(
        username,
        hashed
    )

    return {
        "message":
        "User Registered"
    }

@app.post("/login")
async def login(
    username: str,
    password: str
):

    user = get_user(
        username
    )

    if not user:
        return {
            "error":
            "User not found"
        }

    if not verify_password(
        password,
        user[2]
    ):
        return {
            "error":
            "Invalid Password"
        }

    token = create_token(
        username
    )

    return {
        "access_token":
        token
    }