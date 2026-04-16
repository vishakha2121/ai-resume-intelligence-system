import { Link } from 'react-router-dom';
import { useState } from 'react';

export default function Navbar() {
  const [isDark, setIsDark] = useState(false);
  const toggleTheme = () => {
    setIsDark(!isDark);
    document.documentElement.classList.toggle('dark');
  };
  return (
    <nav className="bg-indigo-600 dark:bg-indigo-800 text-white p-4 shadow-md">
      <div className="container mx-auto flex justify-between items-center">
        <Link to="/" className="text-xl font-bold flex items-center gap-2">
          <img src="/src/assets/logo.svg" alt="Logo" className="h-8 w-8" />
          AI Resume Intel
        </Link>
        <div className="space-x-4">
          <Link to="/" className="hover:text-indigo-200">Dashboard</Link>
          <Link to="/analyze" className="hover:text-indigo-200">Analyze</Link>
          <Link to="/history" className="hover:text-indigo-200">History</Link>
          <Link to="/settings" className="hover:text-indigo-200">Settings</Link>
          <button onClick={toggleTheme} className="ml-4 bg-indigo-500 px-2 py-1 rounded">
            {isDark ? '☀️' : '🌙'}
          </button>
        </div>
      </div>
    </nav>
  );
}