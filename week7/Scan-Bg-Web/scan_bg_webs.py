import requests
#from bs4 import BeautifulSoup

class Histogram:

    def __init__(self):
        self.dict_histogram = {}

    def add(self, server):
        if server in self.dict_histogram.keys():
            self.dict_histogram[server] += 1
        else:
            self.dict_histogram[server] = 1

    def count(self, server):
        return self.dict_histogram[server]

    def __str__(self):
        str_dict = ""
        for key, count in self.dict_histogram.items():
            str_dict += "\n{}: {}".format(key, count)
        return str_dict

    def get_dict(self):
        return self.dict_histogram


def main():

    r = requests.get("http://register.start.bg")
    #print(r.status_code)
    #print(r.headers)
    print(r.content)


if __name__ == '__main__':
    main()
