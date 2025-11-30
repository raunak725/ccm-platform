import React, { useEffect, useState } from "react";
import "./App.css";

interface Control {
  id: number;
  name: string;
  description: string;
  status: string;
}

function App() {
  const [controls, setControls] = useState<Control[]>([]);

  useEffect(() => {
    fetch("https://ccm-platform.onrender.com/controls/")
      .then((res) => res.json())
      .then((data) => setControls(data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="App">
      <h1>Continuous Controls Monitoring</h1>
      <table border={1} cellPadding={8}>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Description</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {controls.map((c) => (
            <tr key={c.id}>
              <td>{c.id}</td>
              <td>{c.name}</td>
              <td>{c.description}</td>
              <td style={{ color: c.status === "pass" ? "green" : "red" }}>{c.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;