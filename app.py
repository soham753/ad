import React, { useState } from 'react';
import Axios from 'axios';

function Login({ setAuthToken }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    Axios.post('http://127.0.0.1:5000/login', { username, password })
      .then((response) => {
        localStorage.setItem('authToken', response.data.access_token);
        setAuthToken(response.data.access_token);
        window.location.href = '/dashboard';
      })
      .catch((error) => alert('Login failed!'));
  };

  return (
    <div>
      <h2>Login</h2>
      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={handleLogin}>Login</button>
    </div>
  );
}

export default Login;
