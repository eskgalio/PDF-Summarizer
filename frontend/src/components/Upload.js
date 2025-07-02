import React, { useState } from 'react';
import { summarizeText, summarizePDF } from '../api';

const Upload = () => {
  const [text, setText] = useState('');
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleTextChange = (e) => {
    setText(e.target.value);
    setFile(null);
  };

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setText('');
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSummary('');
    setError('');
    setLoading(true);
    try {
      let result;
      if (file) {
        result = await summarizePDF(file);
      } else if (text.trim()) {
        result = await summarizeText(text);
      } else {
        setError('Please enter text or upload a PDF.');
        setLoading(false);
        return;
      }
      setSummary(result);
    } catch (err) {
      setError('Failed to summarize.');
    }
    setLoading(false);
  };

  return (
    <div className="upload-container">
      <form onSubmit={handleSubmit}>
        <textarea
          placeholder="Paste your notes here..."
          value={text}
          onChange={handleTextChange}
          rows={6}
          disabled={!!file}
        />
        <div>or</div>
        <input
          type="file"
          accept="application/pdf"
          onChange={handleFileChange}
          disabled={!!text}
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Summarizing...' : 'Summarize'}
        </button>
      </form>
      {error && <div className="error">{error}</div>}
      {summary && (
        <div className="summary">
          <h3>Summary</h3>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
};

export default Upload; 