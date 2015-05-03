import requests
import json
from bs4 import BeautifulSoup
from scan_bg_webs import Histogram


class Crawler:

    def __init__(self):
        self.link = 'http://register.start.bg'
        self.histogram = Histogram()
        self.lying_headers = {
                            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                            }


    def find_redirected_links(self):
        r = requests.get(self.link, allow_redirects=True)
        soup = BeautifulSoup(r.content)
        all_links = []
        link = 'link.php'
        for tag in soup.find_all('a'):
            if tag.get('href') is not None and link in tag.get('href'):
                valid_link = tag.get('href')
                all_links.append(valid_link)
        return all_links


    def result(self):
        result = self.find_redirected_links()
        for link in result:
            try:
                crawled = requests.head(self.link + '/' + str(link), headers=self.lying_headers, timeout=3.0, allow_redirects=True)
                if "Server" in crawled.headers:
                    print(crawled.headers["Server"])
                    if 'Apache' in crawled.headers["Server"]:
                        self.histogram.add('Apache')
                    if 'IIS' in crawled.headers["Server"]:
                        self.histogram.add('IIS')
                    if 'lighttppd' in crawled.headers["Server"]:
                        self.histogram.add('lighttppd')
                    if 'nginx' in crawled.headers["Server"]:
                        self.histogram.add('nginx')
                    if 'Apache' not in crawled.headers["Server"] and 'IIS' not in crawled.headers["Server"] and 'lighttppd' not in crawled.headers["Server"] and 'nginx' not in crawled.headers["Server"]:
                        self.histogram.add('other')

            except requests.exceptions.RequestException as e:
                pass

    def to_JSON(self):
        with open('server_software_data.json', 'w') as output:
            json.dump(self.histogram.get_dict(), output)

c = Crawler()
c.result()
c.to_JSON()
print(c.histogram.get_dict())
