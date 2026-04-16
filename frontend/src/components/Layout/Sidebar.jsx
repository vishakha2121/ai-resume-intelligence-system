import { NavLink } from 'react-router-dom';

export default function Sidebar() {
  return (
    <aside className="w-64 bg-gray-100 dark:bg-gray-800 p-4 hidden md:block">
      <ul className="space-y-2">
        <li><NavLink to="/" className="block p-2 rounded hover:bg-gray-200 dark:hover:bg-gray-700">🏠 Dashboard</NavLink></li>
        <li><NavLink to="/analyze" className="block p-2 rounded hover:bg-gray-200 dark:hover:bg-gray-700">📊 Analyze</NavLink></li>
        <li><NavLink to="/history" className="block p-2 rounded hover:bg-gray-200 dark:hover:bg-gray-700">📜 History</NavLink></li>
        <li><NavLink to="/settings" className="block p-2 rounded hover:bg-gray-200 dark:hover:bg-gray-700">⚙️ Settings</NavLink></li>
      </ul>
    </aside>
  );
}