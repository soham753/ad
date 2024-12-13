import win32evtlog

def check_event_logs():
    server = 'localhost'
    log_type = 'Security'
    hand = win32evtlog.OpenEventLog(server, log_type)
    events = win32evtlog.ReadEventLog(hand, win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ, 0)

    failed_logins = 0
    privilege_escalations = 0
    suspicious_processes = []
    
    for event in events:
        event_id = event.EventID
        # Detect failed logins (Event ID 4625)
        if event_id == 4625:
            failed_logins += 1
        # Detect privilege escalation (Event ID 4672)
        if event_id == 4672:
            privilege_escalations += 1
        # Detect suspicious processes
        if event.SourceName == "Microsoft-Windows-Security-Auditing" and "malicious.exe" in event.Message.lower():
            suspicious_processes.append(event.Message)

    anomalies = []
    if failed_logins > 5:
        anomalies.append(f"Suspicious failed login attempts: {failed_logins}")
    if privilege_escalations > 0:
        anomalies.append(f"Privilege escalation detected: {privilege_escalations}")
    if suspicious_processes:
        anomalies.append("Suspicious processes detected: " + ", ".join(suspicious_processes))

    return anomalies
