# python
import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

print("Password Generator")
length = int(input("Enter the password length (at least 8 characters): "))
print("Generated Password : ", generate_password(length))