#!/usr/bin/python3

# mkpwd.py - make a simple random password

import string, random

def generateSecureKey(size):
    # print("creating secure number of size " + str(size))
    return ''.join(random.SystemRandom().choice(string.digits + string.ascii_uppercase) for _ in range(size))


size = input("Enter size for random security key: ")
print(generateSecureKey(int(size)))

