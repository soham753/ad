// src/AnomalyChart.js
import React from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS } from 'chart.js/auto'; // Required to register all components of Chart.js

function AnomalyChart({ anomalies }) {
  // Format the data for the chart
  const chartData = {
    labels: anomalies.map((anomaly, index) => `Time ${index + 1}`), // Label the time based on anomaly index
    datasets: [
      {
        label: 'Detected Anomalies',
        data: anomalies.map((anomaly) => anomaly.count), // Example: anomaly count (you can adjust this)
        fill: false,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1,
      },
    ],
  };

  return (
    <div className="chart-container">
      <h3>Anomaly Detection Chart</h3>
      <Line data={chartData} />
    </div>
  );
}

export default AnomalyChart;
