import sys

def main():
    filename = sys.argv[1]
    f = open(filename, "r")
    contents = f.read()
    result = contents.split()
    sum_numbers = 0
    for number in result:
        sum_numbers += int(number)
    print(sum_numbers)



if __name__ == '__main__':
    main()
