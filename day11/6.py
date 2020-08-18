#import requests
import json


def main():
    #resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    filename = './day11/test.json'

    with open(filename, 'r', encoding='utf-8') as f:
        print(json.load(f))
        # for news in data_model['newslist']:
        #     print(news['title'])


if __name__ == "__main__":
    main()
