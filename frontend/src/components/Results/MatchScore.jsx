import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip } from 'recharts';

export default function MatchScore({ score, explanation }) {
  const data = [
    { name: 'Match', value: score },
    { name: 'Gap', value: 1 - score }
  ];
  const COLORS = ['#10b981', '#e5e7eb'];
  return (
    <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow">
      <h3 className="text-lg font-semibold mb-2">Match Score</h3>
      <div className="w-48 h-48 mx-auto">
        <ResponsiveContainer>
          <PieChart>
            <Pie data={data} cx="50%" cy="50%" innerRadius={60} outerRadius={80} dataKey="value" stroke="none">
              {data.map((entry, idx) => <Cell key={idx} fill={COLORS[idx]} />)}
            </Pie>
            <Tooltip />
          </PieChart>
        </ResponsiveContainer>
      </div>
      <p className="text-center text-2xl font-bold mt-2">{Math.round(score * 100)}%</p>
      {explanation && <p className="text-sm text-gray-600 dark:text-gray-300 mt-2">{explanation}</p>}
    </div>
  );
}