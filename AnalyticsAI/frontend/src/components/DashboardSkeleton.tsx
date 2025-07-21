import React from "react";

export default function DashboardSkeleton({ data }: { data: any }) {
  return (
    <div style={{ marginTop: 24 }}>
      <h2>Dynamic Dashboard</h2>
      {data && data.data ? (
        <table style={{ width: "100%", borderCollapse: "collapse" }}>
          <thead>
            <tr>
              <th style={{ border: "1px solid #ccc" }}>Category</th>
              <th style={{ border: "1px solid #ccc" }}>Sales</th>
            </tr>
          </thead>
          <tbody>
            {data.data.map((row: any, i: number) => (
              <tr key={i}>
                <td style={{ border: "1px solid #ccc" }}>{row.category}</td>
                <td style={{ border: "1px solid #ccc" }}>{row.total_sales}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>Ask a question to see dashboard data.</p>
      )}
    </div>
  );
}