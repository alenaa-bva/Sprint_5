import random

def generate_login():
    base_login = "alenaibragimova1"
    three_random_digits = random.randint(100, 999)
    email = f"{base_login}{three_random_digits}@yandex.ru"
    return email


