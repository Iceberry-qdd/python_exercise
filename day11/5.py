import json
#import test


def main():
    mydict = {
        "name": "Iceberry",
        "age": 21,
        "qq": 27832451,
        "friends": [
            "王大锤",
            "白远方"
        ],
        "cars": [
            {
                "brand": "BYD",
                "max_speed": 180
            },
            {
                "brand": "Audi",
                "max_speed": 280
            },
            {
                "brand": "Benz",
                "max_speed": 320
            }
        ]
    }
    try:
        with open('./day11/data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成！')


if __name__ == "__main__":
    main()
