import requests
from bs4 import BeautifulSoup


def main():
    resp = requests.get(
        'http://v.taobao.com/v/content/live?catetype=704&from=taovlang')
    soup = BeautifulSoup(resp.text, 'lxml')
    for img_tag in soup.select('img[src]'):
        print(img_tag.attrs['src'])


if __name__ == "__main__":
    main()
