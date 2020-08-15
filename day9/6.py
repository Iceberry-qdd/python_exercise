from Pet import Pet
from Dog import Dog
from Cat import Cat


def main():
    pets = [Dog('旺财'), Cat('凯迪'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()


if __name__ == "__main__":
    main()
