import React, { useState, useEffect } from 'react';
import Axios from 'axios';
import { Line } from 'react-chartjs-2';

function Dashboard({ authToken }) {
  const [anomalies, setAnomalies] = useState([]);

  useEffect(() => {
    Axios.get('http://127.0.0.1:5000/api/anomalies', {
      headers: { Authorization: `Bearer ${authToken}` },
    })
      .then((response) => setAnomalies(response.data.anomalies))
      .catch((error) => console.log(error));
  }, [authToken]);

  const chartData = {
    labels: ['0', '1', '2', '3', '4'],
    datasets: [
      {
        label: 'Failed Logins',
        data: anomalies, // Your data here
        fill: false,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1,
      },
    ],
  };

  return (
    <div>
      <h2>Anomalies Detected</h2>
      <Line data={chartData} />
      <ul>
        {anomalies.map((anomaly, index) => (
          <li key={index}>{anomaly}</li>
        ))}
      </ul>
    </div>
  );
}

export default Dashboard;

