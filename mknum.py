#!/usr/bin/python3

# mknum.py - make a simple random list of numbers

import string, random

def generateSecureKey(size):
    # print("creating secure number of size " + str(size))
    return ''.join(random.SystemRandom().choice(string.digits) for _ in range(size))


size = input("Enter size for random num: ")
print(generateSecureKey(int(size)))

