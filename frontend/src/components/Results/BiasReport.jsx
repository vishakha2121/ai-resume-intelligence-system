export default function BiasReport({ data }) {
  return (
    <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow mt-4">
      <h3 className="text-lg font-semibold mb-2">⚖️ Bias Detection Report</h3>
      <table className="w-full text-left">
        <tbody>
          <tr className="border-b"><td className="py-1">Gender Bias</td><td>{data.gender_bias.toFixed(2)}</td></tr>
          <tr className="border-b"><td className="py-1">Age Bias</td><td>{data.age_bias.toFixed(2)}</td></tr>
          <tr className="border-b"><td className="py-1">Race Bias</td><td>{data.race_bias.toFixed(2)}</td></tr>
          <tr className="border-b"><td className="py-1">Overall Flag</td><td>{data.overall_flag ? '⚠️ Bias Detected' : '✅ No Bias'}</td></tr>
        </tbody>
      </table>
      <p className="text-sm text-gray-500 mt-2">Details: {data.details}</p>
    </div>
  );
}