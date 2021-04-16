import random
import math

def main():
    array = []
    number = random.randint(1,100)
    print("Random Number Selected: ", number)
    print("All possible divisors: ")

    for i in range(1,number+1):
        if number % i == 0:
            array.append(i)
            i = i+1

    print(array)
main()