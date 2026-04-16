import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import ResumeUpload from '../components/Upload/ResumeUpload';
import JDUpload from '../components/Upload/JDUpload';
import MatchScore from '../components/Results/MatchScore';
import axios from 'axios';
import Loader from '../components/Common/Loader';

export default function Dashboard() {
  const navigate = useNavigate();
  const [resumeId, setResumeId] = useState(null);
  const [jdId, setJdId] = useState(null);
  const [match, setMatch] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleMatch = async () => {
    if (!resumeId || !jdId) return alert('Please upload both files first');
    setLoading(true);
    try {
      const res = await axios.post(`http://localhost:8000/api/jd/match/${resumeId}/${jdId}`);
      setMatch(res.data);
      // Store IDs for analyze page
      localStorage.setItem('resumeId', resumeId);
      localStorage.setItem('jdId', jdId);
    } catch (err) {
      console.error(err);
      alert('Matching failed');
    } finally {
      setLoading(false);
    }
  };

  const goToAnalyze = () => {
    if (resumeId && jdId) navigate('/analyze');
    else alert('Please upload both files first');
  };

  return (
    <div className="container mx-auto p-6">
      <h1 className="text-3xl font-bold mb-6">📄 Resume-JD Matching</h1>
      <div className="grid md:grid-cols-2 gap-6">
        <div><h2 className="text-xl font-semibold mb-2">Upload Resume</h2><ResumeUpload onUpload={(data) => setResumeId(data.resume_id)} /></div>
        <div><h2 className="text-xl font-semibold mb-2">Upload Job Description</h2><JDUpload onUpload={(data) => setJdId(data.jd_id)} /></div>
      </div>
      {resumeId && jdId && (
        <div className="mt-6 space-x-4">
          <button onClick={handleMatch} className="bg-indigo-600 text-white px-4 py-2 rounded hover:bg-indigo-700">Get Match Score</button>
          <button onClick={goToAnalyze} className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700">Go to Analyze</button>
        </div>
      )}
      {loading && <Loader />}
      {match && <MatchScore score={match.match_score} explanation={match.explanation} />}
    </div>
  );
}