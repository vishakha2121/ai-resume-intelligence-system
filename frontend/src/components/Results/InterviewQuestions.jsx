export default function InterviewQuestions({ questions }) {
  if (!questions.length) return <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow mt-4">No questions generated yet.</div>;
  return (
    <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow mt-4">
      <h3 className="text-lg font-semibold mb-2">🎤 Generated Interview Questions</h3>
      <ul className="list-disc pl-5 space-y-2">
        {questions.map((q, idx) => (
          <li key={idx}>
            <span className="font-medium capitalize">{q.type}</span> ({q.difficulty}): {q.text}
          </li>
        ))}
      </ul>
    </div>
  );
}