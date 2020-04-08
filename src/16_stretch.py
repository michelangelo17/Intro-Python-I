import sys
import math


def is_prime():
    try:
        num = int(sys.argv[1])
        if num <= 1:
            return print('Integer must be greater than one')
        else:
            for i in range(2, num):
                if num % i == 0:
                    return print('Not prime!')
            return print('PRIME!')
    except:
        return print('Please call the program with an integer as an argument')


# is_prime()

def better_is_prime():
    try:
        num = int(sys.argv[1])
        if num <= 1:
            return print('Integer must be greater than one')
        if num <= 3:
            return print('PRIME!')
        if num % 2 == 0 or num % 3 == 0:
            return print('Not prime!')
        for i in range(5, int(math.sqrt(num)), 6):
            if num % i == 0 or num % (i + 2) == 0:
                return print('Not Prime!')
        return print('PRIME!')
    except:
        return print('Please call the program with an integer as an argument')


# better_is_prime()

def sieve():
    try:
        num = int(sys.argv[1])
        bool_array = [True] * (num + 1)
        bool_array[0] = False
        bool_array[1] = False
        multiple = 2
        while multiple ** 2 <= num:
            if bool_array[multiple]:
                for i in range(multiple * 2, num + 1, multiple):
                    bool_array[i] = False
            multiple += 1
        for multiple in range(num + 1):
            if bool_array[multiple]:
                print(multiple)
    except:
        return print('Please call the program with an integer as an argument')


# sieve()
