import sys


def get_contents(filename):
    with open(filename, "r") as f:
        contents = f.read()
    return contents


def has_contents(count):
    return len(sys.argv[1:]) >= count


def main():
    files = []
    if has_contents(1):
        for arg in sys.argv[1:]:
            files.append(get_contents(arg))
        print('\n'.join(files))
    else:
        print("There are no arguments")

if __name__ == '__main__':
    main()
