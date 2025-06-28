import React, { useState } from 'react';
import axios from 'axios';
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

function App() {
  const [query, setQuery] = useState('');
  const [remarks, setRemarks] = useState('');
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    setResponse(null);
    try {
      const res = await axios.post('http://127.0.0.1:8000/query', {
        query,
        remarks,
      });
      setResponse(res.data);
    } catch (err) {
      console.error(err);
      alert('Something went wrong.');
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: 30 }}>
      <h2>Natural Language Query System</h2>
      <input
        type="text"
        placeholder="Ask your question..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        style={{ padding: 10, width: '60%' }}
      />
      <br /><br />
      <textarea
        placeholder="Remarks (optional)..."
        value={remarks}
        onChange={(e) => setRemarks(e.target.value)}
        style={{ padding: 10, width: '60%', height: 80 }}
      />
      <br /><br />
      <button onClick={handleSubmit} style={{ padding: 10 }}>
        Ask
      </button>

      <div style={{ marginTop: 40 }}>
        {loading && <p>Loading...</p>}

        {!loading && response?.type === 'text' && <p>{response.data}</p>}

        {!loading && response?.type === 'table' && (
          <table border="1" cellPadding="10">
            <thead>
              <tr>
                {Object.keys(response.data[0]).map((head, idx) => (
                  <th key={idx}>{head}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {response.data.map((row, idx) => (
                <tr key={idx}>
                  {Object.values(row).map((val, i) => (
                    <td key={i}>{val}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        )}

        {!loading && response?.type === 'chart' && (
          <Bar
            data={{
              labels: response.labels,
              datasets: [
                {
                  label: 'Values',
                  data: response.values,
                  backgroundColor: 'rgba(75,192,192,0.6)',
                },
              ],
            }}
            options={{ responsive: true }}
          />
        )}
      </div>
    </div>
  );
}

export default App;
