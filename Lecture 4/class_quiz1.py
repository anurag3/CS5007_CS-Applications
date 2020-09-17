def main():
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    if number1 == 0 and number2 == 0:
        print("Both numbers are zero!")
    else:
        sum = number1 + number2
        if sum > 200:
            sum = str(sum) + " *"
        print("Sum = ", sum)
        print("Product = ", number1 * number2)
        print("Average = ", (number1 + number2)/2)


if __name__ == '__main__':
    main()
