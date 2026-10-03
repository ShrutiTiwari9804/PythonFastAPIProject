import { useEffect, useState } from "react";

function App() {

  const [data, setData] = useState(null);

  useEffect(() => {

    fetch("http://127.0.0.1:8000/")
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error("Error fetching data:", error));

  }, []);

  return (
    <div style={{ padding: "20px" }}>

      <h1>My FastAPI + React App</h1>

      <p>Frontend is connected to the backend.</p>

      <h2>Response from FastAPI:</h2>

      {data && (
        <pre>
          {JSON.stringify(data, null, 2)}
        </pre>
      )}

    </div>
  );
}

export default App;
