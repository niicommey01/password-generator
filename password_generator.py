import string
import random

while True:
    try:
        length = int(input("Enter password length: "))
        if length < 8:
            print("Password must be at least 8 characters.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

password = [
    random.choice(string.ascii_lowercase),
    random.choice(string.ascii_uppercase),
    random.choice(string.digits),
    random.choice(string.punctuation)
]

password += random.choices(chars, k=length - 4)

random.shuffle(password)

print("Strong Password:", "".join(password))
