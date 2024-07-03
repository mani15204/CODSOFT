import random
import string


try:
    length = int(input("Enter the length of the password:"))
    print(''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length)))
except ValueError:
    print("Enter valid length")