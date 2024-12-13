import win32evtlog

def check_event_logs():
    server = 'localhost'
    log_type = 'Security'
    
    hand = win32evtlog.OpenEventLog(server, log_type)
    events = win32evtlog.ReadEventLog(hand, win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ, 0)
    
    failed_logins = 0
    for event in events:
        event_id = event.EventID
        if event_id == 4625:  # Failed login attempt
            failed_logins += 1
    
    return failed_logins
