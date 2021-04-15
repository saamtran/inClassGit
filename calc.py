def calc(a,b):
    sum = a + b
    print(sum)

    array = []
    array.append(sum)

    sub = a - b
    print(sub)

    array.append(sub)

    multiply = a * b
    print(multiply)

    array.append(multiply)


def main():
    a = 15
    b = 5
    calc(a,b)

main()