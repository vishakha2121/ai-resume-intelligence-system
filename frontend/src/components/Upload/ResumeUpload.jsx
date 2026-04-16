import { useDropzone } from 'react-dropzone';
import { useState } from 'react';
import axios from 'axios';

export default function ResumeUpload({ onUpload }) {
  const [uploading, setUploading] = useState(false);
  const onDrop = async (acceptedFiles) => {
    const file = acceptedFiles[0];
    if (!file) return;
    setUploading(true);
    const formData = new FormData();
    formData.append('file', file);
    try {
      const res = await axios.post('http://localhost:8000/api/resume/upload', formData);
      onUpload(res.data);
    } catch (err) {
      console.error(err);
      alert('Upload failed');
    } finally {
      setUploading(false);
    }
  };
  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop, accept: { 'application/pdf': ['.pdf'], 'application/vnd.openxmlformats-officedocument.wordprocessingml.document': ['.docx'] } });
  return (
    <div {...getRootProps()} className="border-2 border-dashed border-gray-300 dark:border-gray-600 p-8 rounded-lg text-center cursor-pointer hover:border-indigo-500 transition">
      <input {...getInputProps()} />
      {uploading ? <p>Uploading...</p> : isDragActive ? <p>Drop the resume here...</p> : <p>Drag & drop resume (PDF/DOCX) or click to select</p>}
    </div>
  );
}