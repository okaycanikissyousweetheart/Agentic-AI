import React, { useState } from "react";
import ChatInterface from "./components/ChatInterface";
import Dashboard from "./components/Dashboard";

function App() {
  const [agentResult, setAgentResult] = useState<any>(null);

  return (
    <div>
      <h1>AnalyticsAI</h1>
      <p>
        Welcome to the Agentic Analytics Platform.<br />
        Ask questions, explore data, and automate insights!
      </p>
      <ChatInterface onAgentResult={setAgentResult} />
      <Dashboard data={agentResult} />
    </div>
  );
}

export default App;