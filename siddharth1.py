import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    password_length = int(input("Enter password length (at least 8 characters): "))
    
    if password_length < 8:
        print("Password should be at least 8 characters long.")
    else:
        generated_password = generate_password(password_length)
        print("Generated password:", generated_password)
