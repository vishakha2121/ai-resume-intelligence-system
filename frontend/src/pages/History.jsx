import { useState, useEffect } from 'react';
import axios from 'axios';

export default function History() {
  const [history, setHistory] = useState([]);
  useEffect(() => {
    // Fetch past evaluations from backend (you need to implement this endpoint)
    // For demo, we use dummy data
    setHistory([
      { id: 1, resume: "John_Resume.pdf", jd: "Software_Engineer_JD.pdf", score: 0.85, date: "2025-01-15" },
      { id: 2, resume: "Jane_Resume.pdf", jd: "Data_Scientist_JD.pdf", score: 0.92, date: "2025-01-14" }
    ]);
  }, []);
  return (
    <div className="container mx-auto p-6">
      <h1 className="text-3xl font-bold mb-6">📜 History</h1>
      <div className="overflow-x-auto">
        <table className="min-w-full bg-white dark:bg-gray-800 rounded-lg shadow">
          <thead className="bg-gray-100 dark:bg-gray-700">
            <tr><th className="p-2 text-left">Resume</th><th>Job Description</th><th>Match Score</th><th>Date</th></tr>
          </thead>
          <tbody>
            {history.map(item => (
              <tr key={item.id} className="border-t">
                <td className="p-2">{item.resume}</td><td>{item.jd}</td><td>{Math.round(item.score*100)}%</td><td>{item.date}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}