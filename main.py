import random
import string

class Password:
    def __init__(self, value):
        self.value = value

import random
import string

def generate_password(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


passwords = []

print("Password generator app")