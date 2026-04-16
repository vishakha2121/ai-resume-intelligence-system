import { useState, useEffect } from 'react';
import axios from 'axios';
import BiasReport from '../components/Results/BiasReport';
import BehavioralInsights from '../components/Results/BehavioralInsights';
import InterviewQuestions from '../components/Results/InterviewQuestions';
import ExplainabilityCard from '../components/Results/ExplainabilityCard';
import Loader from '../components/Common/Loader';

export default function Analyze() {
  const [resumeId, setResumeId] = useState(null);
  const [jdId, setJdId] = useState(null);
  const [bias, setBias] = useState(null);
  const [behavior, setBehavior] = useState(null);
  const [questions, setQuestions] = useState([]);
  const [explanation, setExplanation] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const storedResumeId = localStorage.getItem('resumeId');
    const storedJdId = localStorage.getItem('jdId');
    if (!storedResumeId || !storedJdId) {
      alert('Please upload files on Dashboard first');
      setLoading(false);
      return;
    }
    setResumeId(storedResumeId);
    setJdId(storedJdId);
    const fetchData = async () => {
      try {
        const [biasRes, behaviorRes, questionsRes, explainRes] = await Promise.all([
          axios.get(`http://localhost:8000/api/bias/detect/${storedResumeId}`),
          axios.get(`http://localhost:8000/api/behavior/predict/${storedResumeId}?github_username=testuser`),
          axios.get(`http://localhost:8000/api/questions/generate/${storedResumeId}/${storedJdId}`),
          axios.get(`http://localhost:8000/api/scoring/explain/${storedResumeId}/${storedJdId}`)
        ]);
        setBias(biasRes.data);
        setBehavior(behaviorRes.data);
        setQuestions(questionsRes.data.questions);
        setExplanation(explainRes.data);
      } catch (err) {
        console.error(err);
        alert('Failed to fetch analysis data');
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  if (loading) return <Loader />;
  if (!resumeId || !jdId) return <div className="container mx-auto p-6">Please go to Dashboard and upload files first.</div>;
  return (
    <div className="container mx-auto p-6">
      <h1 className="text-3xl font-bold mb-6">🔍 Deep Analysis</h1>
      {bias && <BiasReport data={bias} />}
      {behavior && <BehavioralInsights data={behavior} />}
      {questions && <InterviewQuestions questions={questions} />}
      {explanation && <ExplainabilityCard explanation={explanation} />}
    </div>
  );
}