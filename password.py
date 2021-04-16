import random
import math

def main():
    array = []
    strPass = ""
    num = int(input("How long should your password be? \n"))

    for i in range(1, num+1):
        password = random.randint(0,9)
        strPass = strPass + str(password)
        
    print("Your password of", num, "length is: ", strPass)


main()