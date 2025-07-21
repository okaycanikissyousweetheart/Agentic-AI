import React, { useState } from "react";

type Message = { sender: "user" | "agent", text: string };

export default function ChatInterface({ onAgentResult }: { onAgentResult: (result: any) => void }) {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim() || loading) return;
    setMessages(msgs => [...msgs, { sender: "user", text: input }]);
    setLoading(true);
    const resp = await fetch("/api/agent", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: input })
    });
    const data = await resp.json();
    setMessages(msgs => [...msgs, { sender: "agent", text: data.summary }]);
    setInput("");
    setLoading(false);
    onAgentResult(data);
  };

  return (
    <div style={{ maxWidth: 500, margin: "auto" }}>
      <div style={{ background: "#eee", padding: 8, minHeight: 200 }}>
        {messages.map((m, i) => (
          <div key={i} style={{ textAlign: m.sender === "user" ? "right" : "left" }}>
            <b>{m.sender === "user" ? "You" : "Agent"}:</b> {m.text}
          </div>
        ))}
      </div>
      <div style={{ display: "flex", marginTop: 8 }}>
        <input
          value={input}
          disabled={loading}
          onChange={e => setInput(e.target.value)}
          style={{ flex: 1, padding: 4 }}
          onKeyDown={e => { if (e.key === "Enter") sendMessage(); }}
        />
        <button onClick={sendMessage} disabled={loading}>Send</button>
      </div>
    </div>
  );
}