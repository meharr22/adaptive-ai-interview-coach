# Adaptive AI Interview Coach

An AI-powered interview preparation platform that analyzes resumes, identifies skill gaps, calculates interview readiness, generates company-specific interview questions, and provides personalized learning roadmaps.

## Features

### Resume Analysis

* Upload Resume (PDF)
* Extract Skills Automatically
* Skill Gap Detection

### AI Interview Preparation

* Generate Personalized Interview Questions
* Company-Specific Question Generation
* Adaptive Difficulty Levels (Easy / Medium / Hard)

### Readiness Assessment

* Readiness Score Calculation
* Skill Coverage Analysis

### Personalized Roadmap

* Identify Missing Skills
* Recommend Learning Path
* Generate Improvement Plan

---

## Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn

### AI / NLP

* Google Gemini API
* Resume Parsing
* Skill Matching

### Utilities

* PyPDF2
* Python Dotenv

---

## Project Architecture

Resume Upload

↓

Resume Parsing

↓

Skill Extraction

↓

Skill Gap Detection

↓

Readiness Score

↓

Adaptive Interview Question Generation

↓

Personalized Learning Roadmap

---

## Current Features

* Resume Parsing
* Skill Extraction
* Skill Gap Detection
* Readiness Score Engine
* Personalized Roadmap Generator
* Company-Specific Question Generation
* Adaptive Difficulty Engine

---

## Future Enhancements

* AI Answer Evaluation
* Dynamic Adaptive Interview Sessions
* Interview History Tracking
* Analytics Dashboard
* React Frontend
* Cloud Deployment

---

## Installation

Clone Repository

```bash
git clone https://github.com/meharr22/adaptive-ai-interview-coach.git
```

Move to Backend

```bash
cd adaptive-ai-interview-coach/backend
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Create .env File

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run Server

```bash
python -m uvicorn main:app --reload
```

Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

## Author

Mehar Arora

Electronics and Computer Engineering

Thapar Institute of Engineering and Technology
