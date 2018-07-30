#!/usr/bin/python3

# mknum.py - make a simple random list of numbers

import string, random, sys

def generateSecureKey(size):
    # print("creating secure number of size " + str(size))
    return ''.join(random.SystemRandom().choice(string.digits) for _ in range(size))

# If an argument is passed, try to parse it as a number of digits, instead of asking for one
if len(sys.argv) == 2:
    try:
        size = int(sys.argv[1])
        if size > 0:
            print(generateSecureKey(int(size)))
        else:
            print("Please enter a number greater than 0", file=sys.stderr)
            sys.exit(1)
    except SystemExit as e:
        sys.exit(e)
    except:
        print("{} is not a number".format(sys.argv[1]), file=sys.stderr)
else:
    try:
        size = int(input("Enter size for random num: "))
        if size > 0:
            print(generateSecureKey(int(size)))
        else:
            print("Please enter a number greater than 0")
    except:
        print("Please enter a number")
