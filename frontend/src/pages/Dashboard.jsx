import { useNavigate } from "react-router-dom";

function Dashboard() {

  const navigate = useNavigate();

  return (
    <div>

      <h1>Dashboard</h1>

      <button
        onClick={() => navigate("/upload")}
      >
        Upload Resume
      </button>

      <br /><br />

      <button>
        Start Interview
      </button>

      <br /><br />

      <button>
        Interview History
      </button>

      <br /><br />

      <button>
        Analytics
      </button>

    </div>
  );
}

export default Dashboard;