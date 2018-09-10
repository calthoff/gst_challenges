import random
import string


def generate_function():
    password = ''
    for i in range(random.randint(3, 5)):
            password += random.choice(string.punctuation)
            password += random.choice(string.ascii_lowercase)
            password += random.choice(string.ascii_uppercase)
            password += str(random.choice(range(0, 9)))
    return password


print(generate_function())
