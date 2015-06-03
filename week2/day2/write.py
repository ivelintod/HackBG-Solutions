import sys


def main():
    f = 'file.txt'
    file = open(f, "w")
    contents = ["Python is an awesome language!", "You should try it"]
    file.write("\n".joint(contents))
    file.close()


