import React from "react";
import Plot from "react-plotly.js";

export default function Dashboard({ data }: { data: any }) {
  if (!data || !data.sales_data) return <p>Ask a question to see dashboard data.</p>;
  const categories = data.sales_data.map((row: any) => row.category);
  const sales = data.sales_data.map((row: any) => row.total_sales);

  return (
    <div style={{ marginTop: 24 }}>
      <h2>Dynamic Dashboard</h2>
      <Plot
        data={[
          {
            type: "bar",
            x: categories,
            y: sales,
            marker: { color: "#2a9d8f" },
            name: "Sales",
          },
        ]}
        layout={{
          title: "Sales by Product Category",
          xaxis: { title: "Category" },
          yaxis: { title: "Sales" },
          height: 400,
        }}
        style={{ width: "100%" }}
      />
      <table style={{ width: "100%", borderCollapse: "collapse", marginTop: 24 }}>
        <thead>
          <tr>
            <th style={{ border: "1px solid #ccc" }}>Category</th>
            <th style={{ border: "1px solid #ccc" }}>Sales</th>
          </tr>
        </thead>
        <tbody>
          {data.sales_data.map((row: any, i: number) => (
            <tr key={i}>
              <td style={{ border: "1px solid #ccc" }}>{row.category}</td>
              <td style={{ border: "1px solid #ccc" }}>{row.total_sales}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <div style={{ marginTop: 16, background: "#f6f6f6", padding: 12, borderRadius: 6 }}>
        <b>Agent Insights:</b>
        <div>{data.summary}</div>
      </div>
    </div>
  );
}