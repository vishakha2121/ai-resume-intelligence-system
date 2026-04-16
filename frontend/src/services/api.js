import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
  headers: { 'Content-Type': 'application/json' }
});

export const uploadResume = (file) => {
  const formData = new FormData();
  formData.append('file', file);
  return api.post('/api/resume/upload', formData);
};

export const uploadJD = (file) => {
  const formData = new FormData();
  formData.append('file', file);
  return api.post('/api/jd/upload', formData);
};

export const getMatch = (resumeId, jdId) => api.post(`/api/jd/match/${resumeId}/${jdId}`);
export const getBias = (resumeId) => api.get(`/api/bias/detect/${resumeId}`);
export const getBehavior = (resumeId, githubUser) => api.get(`/api/behavior/predict/${resumeId}?github_username=${githubUser || ''}`);
export const getQuestions = (resumeId, jdId) => api.get(`/api/questions/generate/${resumeId}/${jdId}`);
export const getExplanation = (resumeId, jdId) => api.get(`/api/scoring/explain/${resumeId}/${jdId}`);

export default api;