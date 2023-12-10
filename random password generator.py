#importing random library
import random
import string

#function to generate random password
def generate_password(length=8):
    #defining what characters needed to be in our password in this case we included alphabet
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password
# Example usage:
password = generate_password()
print("Your Random Password:", password)