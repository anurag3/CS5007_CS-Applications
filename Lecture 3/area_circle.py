import math

def main():
    outer = float(input("Enter radius of the outer circle:"))
    inner = float(input("Enter radius of the inner circle:"))

    area = (math.pi * outer ** 2) - (math.pi * inner ** 2)

    print("Area of part between outer and inner circle is", area)
    print("rounded to", round(area, 4))

if __name__ == "__main__":
    main()