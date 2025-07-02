import React from 'react';
import Upload from './components/Upload';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Auto Notes Summarizer</h1>
        <p>Upload a PDF or paste your notes to get an instant summary.</p>
      </header>
      <main>
        <Upload />
      </main>
    </div>
  );
}

export default App;
