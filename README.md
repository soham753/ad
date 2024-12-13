from flask import Flask, jsonify
from eventlog import check_event_logs
from registry import check_registry

app = Flask(__name__)

@app.route('/api/anomalies', methods=['GET'])
def get_anomalies():
    anomalies = []
    
    # Detect anomalies in event logs
    failed_logins = check_event_logs()
    if failed_logins > 5:  # Example threshold
        anomalies.append({"message": f"Suspicious failed login attempts: {failed_logins}"})
    
    # Detect registry anomalies
    registry_changes = check_registry()
    if registry_changes:
        anomalies.append({"message": "Unauthorized registry changes detected"})
    
    return jsonify(anomalies)

if __name__ == '__main__':
    app.run(debug=True)
