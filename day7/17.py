def max2(x):
    #sorted(x, reverse=True)
    x.sort(reverse=True)
    return x[0], x[1]


if __name__ == "__main__":
    x = [1, 2, 5, 4, 0, 1, -3, 25, 7, 8, 5, 4, 100]
    print(max2(x))
