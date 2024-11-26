import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = "".join(random.choice(characters) for _ in range(length))
    return password

password_length = 12
print("Generated Password:", generate_password(password_length))