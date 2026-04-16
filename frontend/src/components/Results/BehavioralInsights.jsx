import { Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, ResponsiveContainer, Tooltip } from 'recharts';

export default function BehavioralInsights({ data }) {
  const chartData = [
    { trait: 'Openness', value: data.personality.openness * 100 },
    { trait: 'Conscientiousness', value: data.personality.conscientiousness * 100 },
    { trait: 'Extraversion', value: data.personality.extraversion * 100 },
    { trait: 'Agreeableness', value: data.personality.agreeableness * 100 },
    { trait: 'Neuroticism', value: data.personality.neuroticism * 100 },
  ];
  return (
    <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow mt-4">
      <h3 className="text-lg font-semibold mb-2">🧠 Behavioral Prediction</h3>
      <p>Job Hopping Risk: <strong>{Math.round(data.job_hopping_risk * 100)}%</strong></p>
      <ResponsiveContainer width="100%" height={300}>
        <RadarChart data={chartData}>
          <PolarGrid />
          <PolarAngleAxis dataKey="trait" />
          <PolarRadiusAxis domain={[0, 100]} />
          <Radar dataKey="value" stroke="#8884d8" fill="#8884d8" fillOpacity={0.6} />
          <Tooltip />
        </RadarChart>
      </ResponsiveContainer>
    </div>
  );
}