import random


def generate_email():
    digits = random.randint(100, 999)
    return f"tatianat_53_{digits}@yandex.ru"


def generate_password():
    return f"Password{random.randint(1000, 9999)}"