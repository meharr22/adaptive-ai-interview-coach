import { BrowserRouter, Routes, Route } from "react-router-dom";
import Interview from "./pages/Interview";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import UploadResume from "./pages/UploadResume";
import Report from "./pages/Report";
import History from "./pages/History";


function App() {
  return (
    <BrowserRouter>

      <Routes>

        <Route
          path="/"
          element={<Login />}
        />

        <Route
          path="/dashboard"
          element={<Dashboard />}
        />
        <Route
    path="/history"
    element={<History />}
/>
        <Route
          path="/upload"
          element={<UploadResume />}
/>
        <Route
  path="/interview"
  element={<Interview />}
/>
     <Route
  path="/report"
  element={<Report />}
/>
      </Routes>
    

    </BrowserRouter>
  );
}

export default App;