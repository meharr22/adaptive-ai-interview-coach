import { useState } from "react";
import axios from "axios";
import { useLocation, useNavigate } from "react-router-dom";
import { useEffect } from "react";

function Interview() {

  const location = useLocation();
  const navigate = useNavigate();
  const questions = location.state?.questions || [];

  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answer, setAnswer] = useState("");
  const [evaluation, setEvaluation] = useState("");
  const [loading, setLoading] = useState(false);
const [sessionId, setSessionId] = useState("");
useEffect(() => {

  const startInterview = async () => {

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/start-interview"
      );

      setSessionId(
        response.data.session_id
      );

      console.log(
        "Session Started:",
        response.data.session_id
      );

    } catch (error) {

      console.log(error);

    }

  };

  startInterview();

}, []);
  const handleSubmit = async () => {

    setLoading(true);

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/evaluate-answer",
        null,
        {
          params: {
            question: questions[currentQuestion],
            answer: answer
          }
        }
      );
const evaluationText = response.data.evaluation;

setEvaluation(evaluationText);

// Extract score from evaluation (e.g. 8/10)
const match = evaluationText.match(/(\d+)\/10/);

let score = 5;

if (match) {
  score = parseInt(match[1]);
}

// Save score in backend session
await axios.post(
  "http://127.0.0.1:8000/update-session",
  null,
  {
    params: {
      session_id: sessionId,
      score: score
    }
  }
);

console.log("Score Saved:", score);

    } catch (error) {

      console.log(error);
      alert("Evaluation Failed");

    }

    setLoading(false);

  };

  const handleNext = async () => {

  if (currentQuestion === questions.length - 1) {

    try {

      const response = await axios.get(
        "http://127.0.0.1:8000/interview-report",
        {
          params: {
            session_id: sessionId
          }
        }
      );

      navigate("/report", {
        state: response.data
      });

    } catch (error) {

      console.log(error);
      alert("Report Generation Failed");

    }

  } else {

    setCurrentQuestion(currentQuestion + 1);
    setAnswer("");
    setEvaluation("");

  }

};

  return (

    <div
      style={{
        color: "white",
        width: "70%",
        margin: "40px auto",
        textAlign: "center"
      }}
    >

      <h1>AI Interview</h1>

      {/* Progress Bar */}

      <div
        style={{
          width: "100%",
          height: "12px",
          background: "#444",
          borderRadius: "20px",
          marginBottom: "30px"
        }}
      >
        <div
          style={{
            width: `${((currentQuestion + 1) / questions.length) * 100}%`,
            height: "100%",
            background: "#4CAF50",
            borderRadius: "20px",
            transition: "0.5s"
          }}
        ></div>
      </div>

      <h2>
        Question {currentQuestion + 1} / {questions.length}
      </h2>

      {/* Question Card */}

      <div
        style={{
          background: "#2c2c2c",
          padding: "20px",
          borderRadius: "12px",
          marginBottom: "25px",
          fontSize: "22px",
          fontWeight: "bold"
        }}
      >
        {questions[currentQuestion]}
      </div>

      {/* Answer Box */}

      <textarea
        rows="8"
        placeholder="Type your answer here..."
        value={answer}
        onChange={(e) => setAnswer(e.target.value)}
        style={{
          width: "100%",
          padding: "15px",
          fontSize: "17px",
          borderRadius: "10px",
          resize: "none"
        }}
      />

      <br />

      {/* Submit Button */}

      <button
        disabled={loading}
        onClick={handleSubmit}
        style={{
          marginTop: "20px",
          padding: "12px 30px",
          background: "#2563eb",
          color: "white",
          border: "none",
          borderRadius: "8px",
          cursor: "pointer",
          fontSize: "16px"
        }}
      >
        {loading ? "Evaluating..." : "Submit Answer"}
      </button>

      {/* Evaluation */}

      {evaluation && (

        <>

          <hr
            style={{
              marginTop: "40px",
              marginBottom: "30px"
            }}
          />

          <h2>AI Evaluation</h2>

          <div
            style={{
              background: "#202020",
              padding: "20px",
              borderRadius: "10px",
              whiteSpace: "pre-wrap",
              textAlign: "left",
              marginTop: "20px"
            }}
          >
            {evaluation}
          </div>

          <br />

    
          <button
  onClick={handleNext}
  style={{
    marginTop: "20px",
    padding: "12px 30px",
    background: "#16a34a",
    color: "white",
    border: "none",
    borderRadius: "8px",
    cursor: "pointer",
    fontSize: "16px"
  }}
>
  {currentQuestion === questions.length - 1
    ? "📊 Generate Final Report"
    : "Next Question →"}
</button>

        </>

      )}

    </div>

  );

}

export default Interview;