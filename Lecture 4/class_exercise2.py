def syracuse(number):
    res = str(number)
    while(number > 1):
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        res = res + str(number)
        print(res)


def main():
    number = int(input("Enter an integer >1: "))
    syracuse(number)


if __name__ == '__main__':
    main()