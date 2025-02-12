#simple password Genratercls

import random
import string

def generated_password(length=12):
     characters = string.ascii_letters + string.punctuation #alphabat small and capital combine symbols 
     password = ''.join(random.choice(characters)for _ in range(length))
     return password

length = int(input("Enter the length of password:"))

password = generated_password(length)
print("Generated Password is: ", password)