import { createContext, useContext, useState } from 'react';

const AppContext = createContext();

export const useApp = () => useContext(AppContext);

export function AppProvider({ children }) {
  const [resumeId, setResumeId] = useState(null);
  const [jdId, setJdId] = useState(null);
  const [matchResult, setMatchResult] = useState(null);
  return (
    <AppContext.Provider value={{ resumeId, setResumeId, jdId, setJdId, matchResult, setMatchResult }}>
      {children}
    </AppContext.Provider>
  );
}