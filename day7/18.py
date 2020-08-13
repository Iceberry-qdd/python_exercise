def is_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, day):
    days_of_month = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
                     [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]][is_leap(year)]
    total = 0
    for index in range(month-1):
        total += days_of_month[index]
    return total+day


def main():
    print(which_day(1980, 11, 28))
    print(which_day(1981, 12, 31))
    print(which_day(2018, 1, 1))
    print(which_day(2016, 3, 1))


if __name__ == "__main__":
    main()
