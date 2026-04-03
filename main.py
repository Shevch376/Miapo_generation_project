import random
import string

class Password:
    def __init__(self, value):
        self.password = value
        self.length = len(value)
        self.created_at = "now"

def generate_password(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def delete_password(index):
    passwords.pop(index)

passwords = []

def save_password(pwd):
    passwords.append(Password(pwd))
