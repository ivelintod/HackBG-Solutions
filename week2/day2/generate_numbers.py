import sys
from random import randint


def has_arguments(counts):
    return len(sys.argv[1:]) >= counts


def write_to(filename, n):
    with open(filename, "w") as f:
        for i in range(n):
            contents = randint(1, 1000)
            f.write(str(contents) + " ")
    return filename


def main():
    if has_arguments(2):
        filename = write_to(sys.argv[1], int(sys.argv[2]))
        file1 = open(filename, "r")
        content = file1.read()
        print(content)
        file1.close()
    else:
        print("Two arguments needed, idiot")


if __name__ == '__main__':
    main()
