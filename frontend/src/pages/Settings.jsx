import { useState } from 'react';

export default function Settings() {
  const [apiKey, setApiKey] = useState(localStorage.getItem('gemini_api_key') || '');
  const saveKey = () => {
    localStorage.setItem('gemini_api_key', apiKey);
    alert('API Key saved (demo only)');
  };
  return (
    <div className="container mx-auto p-6">
      <h1 className="text-3xl font-bold mb-6">⚙️ Settings</h1>
      <div className="bg-white dark:bg-gray-800 p-4 rounded shadow">
        <label className="block mb-2">Gemini API Key (for demo)</label>
        <input type="password" value={apiKey} onChange={(e) => setApiKey(e.target.value)} className="w-full p-2 border rounded dark:bg-gray-700" />
        <button onClick={saveKey} className="mt-4 bg-indigo-600 text-white px-4 py-2 rounded">Save</button>
        <p className="text-xs text-gray-500 mt-2">This is only stored in browser localStorage for practice.</p>
      </div>
    </div>
  );
}