def main():
    num_lines = int(input())

    i = 1
    for a in range(num_lines):
        print(str(i) + " " + str(i + 1) + " " + str(i + 2) + " PUM")
        i = i + 4

if __name__ == "__main__":
    main()
