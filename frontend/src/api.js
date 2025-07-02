import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const summarizeText = async (text) => {
  const formData = new FormData();
  formData.append('text', text);
  const response = await axios.post(`${API_URL}/summarize-text/`, formData);
  return response.data.summary;
};

export const summarizePDF = async (file) => {
  const formData = new FormData();
  formData.append('file', file);
  const response = await axios.post(`${API_URL}/summarize-pdf/`, formData);
  return response.data.summary;
}; 