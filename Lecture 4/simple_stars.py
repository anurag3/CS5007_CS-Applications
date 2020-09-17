
def stars1(rows):
    for i in range(rows):
        star = ""
        for j in range(i + 1):
            star += "* "
        print(star)


def stars2(rows):
    for i in range(rows):
        for j in range(i + 1):
            print("*", end=" ")
        print()

def main():
    rows = int(input("Enter number of rows: "))
    stars1(rows)
    stars2(rows)

if __name__ == '__main__':
    main()