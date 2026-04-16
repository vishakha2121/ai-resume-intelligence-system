export default function ExplainabilityCard({ explanation }) {
  // If no explanation is provided, render nothing
  if (!explanation) return null;

  // Extract the string explanation – handle both object and string inputs
  let explanationText = "";
  if (typeof explanation === "string") {
    explanationText = explanation;
  } else if (typeof explanation === "object") {
    // Get the text_explanation property (string) – fallback to empty string
    explanationText = explanation.text_explanation || explanation.explanation || "";
  }

  // If after extraction the text is still empty, show a default message
  if (!explanationText) {
    explanationText = "No explanation available.";
  }

  return (
    <div className="bg-blue-50 dark:bg-gray-800 p-4 rounded-lg shadow mt-4">
      <h3 className="text-lg font-semibold mb-2">🔍 Why this score?</h3>
      <p className="text-sm">{explanationText}</p>
      {explanation && typeof explanation === "object" && explanation.similarity !== undefined && (
        <p className="text-xs text-gray-500 mt-2">
          Similarity: {(explanation.similarity * 100).toFixed(1)}%
        </p>
      )}
    </div>
  );
}