// src/api.js
import Axios from 'axios';

// Define the base URL for the backend API
const API_BASE_URL = 'http://127.0.0.1:5000';

// Function to fetch anomalies from the backend
export const fetchAnomalies = async (authToken) => {
  try {
    const response = await Axios.get(`${API_BASE_URL}/api/anomalies`, {
      headers: {
        Authorization: `Bearer ${authToken}`,
      },
    });
    return response.data.anomalies;
  } catch (error) {
    console.error("Error fetching anomalies:", error);
    throw error;
  }
};

// Function to start monitoring anomalies (background job)
export const startMonitoring = async () => {
  try {
    await Axios.post(`${API_BASE_URL}/start-monitoring`);
    console.log("Monitoring started successfully!");
  } catch (error) {
    console.error("Error starting monitoring:", error);
  }
};
