from scan_bg_webs import Histogram
import matplotlib.pyplot as plt
import json


def main():
    h = Histogram()
    with open('server_software_data.json', 'r') as data:
        contents = data.read()
        h.dict_histogram = json.loads(contents)
    histogram = h.get_dict()
    keys = list(histogram.keys())
    values = list(histogram.values())

    X = list(range(len(keys)))

    plt.bar(X, values, align="center")
    plt.xticks(X, keys)

    plt.title(".bg servers")
    plt.xlabel("Server")
    plt.ylabel("Count")

    plt.savefig('histogam.png')

if __name__ == '__main__':
    main()
