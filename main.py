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

def get_password(index):
    return passwords[index]

def save_password(pwd):
    passwords.append(Password(pwd))

passwords = []

if __name__ == "__main__":
    while True:
        print("\n1. Сгенерировать пароль")
        print("2. Показать все пароли")
        print("3. Удалить пароль")
        print("4. Выход")

        choice = input("Выбор: ")

        if choice == "1":
            pwd = generate_password()
            save_password(pwd)
            print("Сгенерирован и сохранён:", pwd)

        elif choice == "2":
            for i, p in enumerate(passwords):
                print(i, p.password)

        elif choice == "3":
            index = int(input("Введите индекс: "))
            delete_password(index)

        elif choice == "4":
            break