/* src/Dashboard.css */

/* Dashboard container */
.dashboard-container {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Title for the dashboard */
.dashboard-container h2 {
  text-align: center;
  margin-bottom: 20px;
  font-size: 28px;
  font-weight: bold;
}

/* List for detected anomalies */
.anomaly-list {
  list-style: none;
  padding: 0;
  margin: 20px 0;
}

.anomaly-list li {
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 5px;
}

.anomaly-list li span {
  font-weight: bold;
}

/* Anomaly notification banner */
.anomaly-notification {
  padding: 10px;
  background-color: #ffcc00;
  border: 1px solid #ff9900;
  border-radius: 5px;
  margin-top: 20px;
  font-weight: bold;
}

.anomaly-notification.warning {
  background-color: #ff9900;
  border-color: #ff6600;
}

/* Styling for the chart container */
.chart-container {
  margin-top: 30px;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Styling for buttons on the dashboard */
.dashboard-buttons {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.dashboard-buttons button {
  margin-right: 10px;
  padding: 12px 25px;
  font-size: 16px;
  border-radius: 5px;
  cursor: pointer;
}

.dashboard-buttons button.start {
  background-color: #28a745;
  color: white;
}

.dashboard-buttons button.start:hover {
  background-color: #218838;
}

.dashboard-buttons button.stop {
  background-color: #dc3545;
  color: white;
}

.dashboard-buttons button.stop:hover {
  background-color: #c82333;
}
