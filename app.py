import logging
import smtplib
from email.mime.text import MIMEText
from config import SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD

def log_anomalies(anomalies):
    for anomaly in anomalies:
        logging.info(anomaly)

def send_email_alert(message):
    msg = MIMEText(message)
    msg['Subject'] = 'Anomaly Detected in Windows Logs'
    msg['From'] = SMTP_USER
    msg['To'] = 'admin@example.com'

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(msg['From'], [msg['To']], msg.as_string())
            print(f"Alert sent: {message}")
    except Exception as e:
        print(f"Error sending email: {e}")
