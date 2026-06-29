import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function UploadResume() {
  const navigate = useNavigate();
  const [file, setFile] = useState(null);
  const [role, setRole] = useState("");
  const [company, setCompany] = useState("");
  const [result, setResult] = useState(null);

  const handleUpload = async () => {

    const formData = new FormData();

    formData.append("file", file);

    try {

      const response = await axios.post(
        `http://127.0.0.1:8000/upload-resume?target_role=${role}&company=${company}`,
        formData
      );

      setResult(response.data);

    } catch (error) {

      console.log(error);

      alert("Upload Failed");

    }

  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        padding: "40px",
        color: "white"
      }}
    >

      <h1>Resume Analyzer</h1>

      <input
        style={{
          width: "300px",
          padding: "10px",
          marginBottom: "15px",
          backgroundColor: "white",
          color: "black"
        }}
        type="text"
        placeholder="Target Role"
        value={role}
        onChange={(e) => setRole(e.target.value)}
      />

      <input
        style={{
          width: "300px",
          padding: "10px",
          marginBottom: "15px",
          backgroundColor: "white",
          color: "black"
        }}
        type="text"
        placeholder="Company"
        value={company}
        onChange={(e) => setCompany(e.target.value)}
      />

      <input
        style={{
          marginBottom: "15px"
        }}
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button
        style={{
          padding: "10px 20px",
          cursor: "pointer"
        }}
        onClick={handleUpload}
      >
        Analyze Resume
      </button>

      {result && (
  <div
    style={{
      marginTop: "30px",
      width: "80%",
      textAlign: "left",
      border: "1px solid gray",
      borderRadius: "10px",
      padding: "20px"
    }}
  >

    <h2>📊 Readiness Score</h2>
    <h3>{result.readiness_score}%</h3>

    <hr />

    <h2>💻 Your Skills</h2>

    <ul>
      {result.skills.map((skill, index) => (
        <li key={index}>✅ {skill}</li>
      ))}
    </ul>

    <hr />

    <h2>📚 Missing Skills</h2>

    <ul>
      {result.missing_skills.map((skill, index) => (
        <li key={index}>❌ {skill}</li>
      ))}
    </ul>

    <hr />

    <h2>🎯 Interview Difficulty</h2>
    <h3>{result.difficulty}</h3>

    <hr />

    <h2>🗺️ Learning Roadmap</h2>

    <ol>
      {result.roadmap.map((item, index) => (
        <li key={index}>{item}</li>
      ))}
    </ol>

    <br />

   <button
  onClick={() =>
    navigate("/interview", {
      state: {
        questions: result.questions,
        role: result.target_role
      }
    })
  }
>
  🚀 Start Interview
</button>

  </div>
)}

    </div>
  );
}

export default UploadResume;