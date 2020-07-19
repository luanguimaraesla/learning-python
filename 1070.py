def main():
    a = int(input())

    if (a % 2 == 0):
        a = a + 1

    for x in range(6):
        print(a)
        a = a + 2

if __name__ == "__main__":
    main()
