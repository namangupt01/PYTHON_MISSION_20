import string
import random

def generator():
    s1 = string.ascii_lowercase
    s2= string.ascii_uppercase
    s3= string.digits
    s4= string.punctuation
    print("Enter the length of the password")
    password_length = int(input())

    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    result = ("".join(s[0:password_length]))
    print(result)

    
generator()