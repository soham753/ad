// src/App.js
import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Dashboard from './Dashboard';
import Login from './Login';
import { fetchAnomalies } from './api';
import './App.css';

function App() {
  const [authToken, setAuthToken] = useState(localStorage.getItem('authToken')); // Manage auth token
  const [anomalies, setAnomalies] = useState([]); // State to store fetched anomalies
  const [loading, setLoading] = useState(true); // Loading state for API data

  // Use effect to redirect if there's no auth token
  useEffect(() => {
    if (!authToken) {
      window.location.href = '/login'; // Redirect to login page if no token
    }
  }, [authToken]);

  // Fetch anomalies data when the token is present
  useEffect(() => {
    if (authToken) {
      const getAnomalies = async () => {
        setLoading(true);
        try {
          const data = await fetchAnomalies(authToken);
          setAnomalies(data);
        } catch (error) {
          console.error("Error fetching anomalies:", error);
        } finally {
          setLoading(false);
        }
      };
      getAnomalies();
    }
  }, [authToken]);

  return (
    <Router>
      <div className="app-container">
        <header>
          Automated Anomaly Detection Tool
        </header>

        <Switch>
          <Route path="/login">
            <Login setAuthToken={setAuthToken} />
          </Route>

          <Route path="/dashboard">
            <Dashboard anomalies={anomalies} loading={loading} />
          </Route>

          {/* Redirect to dashboard by default */}
          <Route path="/" exact>
            {authToken ? (
              <Dashboard anomalies={anomalies} loading={loading} />
            ) : (
              <Login setAuthToken={setAuthToken} />
            )}
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
