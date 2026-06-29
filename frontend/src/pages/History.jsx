import { useEffect, useState } from "react";
import axios from "axios";

function History() {

  const [history, setHistory] = useState([]);

  useEffect(() => {

    const loadHistory = async () => {

      try {

        const response = await axios.get(
          "http://127.0.0.1:8000/db-history"
        );

        setHistory(response.data.history);

      } catch (error) {

        console.log(error);

      }

    };

    loadHistory();

  }, []);

  return (

    <div
      style={{
        width: "80%",
        margin: "40px auto",
        color: "white"
      }}
    >

      <h1>📜 Interview History</h1>

      <table
        style={{
          width: "100%",
          borderCollapse: "collapse",
          marginTop: "30px"
        }}
      >

        <thead>

          <tr>

            <th>ID</th>

            <th>Session</th>

            <th>Average Score</th>

            <th>Verdict</th>

          </tr>

        </thead>

        <tbody>

          {history.map((item, index) => (

            <tr key={index}>

              <td>{item[0]}</td>

              <td>{item[1]}</td>

              <td>{item[2]}</td>

              <td>{item[3]}</td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>

  );

}

export default History;