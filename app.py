from werkzeug.security import check_password_hash
from config import USERS

def authenticate_user(username, password):
    # Replace with your user database or file-based user storage
    users = {
        "admin": {"password": "hashed_password_here"}
    }

    if username in users:
        return check_password_hash(users[username]["password"], password)
    return False
