import threading
import time
from models.eventlog import check_event_logs
from models.registry import check_registry

def monitor_logs():
    while True:
        anomalies = check_event_logs() + check_registry()
        if anomalies:
            print(f"Anomalies detected: {anomalies}")
        time.sleep(10)  # Check every 10 seconds

def start_monitoring():
    thread = threading.Thread(target=monitor_logs)
    thread.daemon = True
    thread.start()

