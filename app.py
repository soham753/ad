import React, { useState, useEffect } from 'react';
import Axios from 'axios';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Dashboard from './Dashboard';
import Login from './Login';

function App() {
  const [authToken, setAuthToken] = useState(localStorage.getItem('authToken'));

  useEffect(() => {
    if (!authToken) {
      window.location.href = '/login';
    }
  }, [authToken]);

  return (
    <Router>
      <Switch>
        <Route path="/login">
          <Login setAuthToken={setAuthToken} />
        </Route>
        <Route path="/dashboard">
          <Dashboard authToken={authToken} />
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
