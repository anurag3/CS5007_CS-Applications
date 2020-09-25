def stars(rows):
    for i in range(1, rows + 1):
        star = ""
        star += " " * abs(i - rows)
        for j in range(0, 2 * i - 1):
            star += "*"
        star += " " * abs(i - rows)
        print(star)


def main():
    rows = int(input("Enter number of rows: "))
    stars(rows)


if __name__ == "__main__":
    main()