import { useLocation, Link } from "react-router-dom";

function Report() {

  const location = useLocation();

  const report = location.state?.report;
  const aiFeedback = location.state?.ai_feedback;

  if (!report) {
    return (
      <h2
        style={{
          color: "white",
          textAlign: "center",
          marginTop: "100px"
        }}
      >
        No Report Available
      </h2>
    );
  }

  return (

    <div
      style={{
        width: "75%",
        margin: "40px auto",
        color: "white"
      }}
    >

      <h1
        style={{
          textAlign: "center",
          marginBottom: "30px"
        }}
      >
        🎯 Final Interview Report
      </h1>

      <div
        style={{
          background: "#202020",
          padding: "25px",
          borderRadius: "12px",
          boxShadow: "0px 0px 12px rgba(255,255,255,0.08)"
        }}
      >

        <h2>📊 Overall Score</h2>
        <h3>{report.average_score} / 10</h3>

        <hr />

        <h2>❓ Questions Attempted</h2>
        <h3>{report.questions_attempted}</h3>

        <hr />

        <h2>🏆 Verdict</h2>
        <h3>{report.verdict}</h3>

        <hr />

        <h2>🎯 Recommended Level</h2>
        <h3>{report.recommended_level}</h3>

        <hr />

        <h2>📈 Interview Readiness</h2>
        <h3>{report.interview_readiness}</h3>

        <hr />

        <h2>💪 Strength</h2>
        <p>{report.strength}</p>

        <hr />

        <h2>📌 Weakness</h2>
        <p>{report.weakness}</p>

      </div>

      <br />

      <div
        style={{
          background: "#202020",
          padding: "25px",
          borderRadius: "12px",
          whiteSpace: "pre-wrap",
          boxShadow: "0px 0px 12px rgba(255,255,255,0.08)"
        }}
      >

        <h2>🤖 AI Feedback</h2>

        <p>{aiFeedback}</p>

      </div>

      <br />

      <div
        style={{
          textAlign: "center"
        }}
      >

        <Link to="/history">

          <button
            style={{
              padding: "14px 28px",
              background: "#2563eb",
              color: "white",
              border: "none",
              borderRadius: "10px",
              cursor: "pointer",
              fontSize: "17px",
              fontWeight: "bold"
            }}
          >
            📜 View Interview History
          </button>

        </Link>

      </div>

    </div>

  );

}

export default Report;