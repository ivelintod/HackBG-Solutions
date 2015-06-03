import sys

def main():
    f = "file.txt"
    fi = open(f, "r")
    contents = fi.read()
    print(contents)
    fi.close

if __name__ == '__main__':
    main()
