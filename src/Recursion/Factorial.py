def factorial(number: int) -> int:
    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)

if __name__ == "__main__":
    print(factorial(5))
