from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import logging
from models.eventlog import check_event_logs
from models.registry import check_registry
from models.report import log_anomalies
from models.monitoring import start_monitoring
from models.security import authenticate_user

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Change it to a strong secret key
jwt = JWTManager(app)

logging.basicConfig(filename="logs/anomalies.log", level=logging.INFO, format="%(asctime)s - %(message)s")

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if authenticate_user(username, password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401

@app.route('/api/anomalies', methods=['GET'])
@jwt_required()
def get_anomalies():
    event_anomalies = check_event_logs()
    registry_anomalies = check_registry()
    anomalies = event_anomalies + registry_anomalies

    if anomalies:
        log_anomalies(anomalies)

    return jsonify(anomalies=anomalies), 200

@app.route('/start-monitoring', methods=['POST'])
def start_monitoring_route():
    start_monitoring()
    return jsonify({"msg": "Monitoring started!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
