#!/usr/bin/python3
def positive_or_negative(number):
    if not isinstance(number, int):
        raise TypeError("number must be an integer")
    if number > 0:
        print(f"{number:d} is positive")
    elif number == 0:
        print(f"{number:d} is zero")
    else:
        print(f"{number:d} is negative")


if __name__ == "__main__":
    import random
    number = random.randint(-10000, 10000)
    positive_or_negative(number)
