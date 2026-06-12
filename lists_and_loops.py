def square_numbers(values: list[int]) -> list[int]:
    squares: list[int] = []
    for value in values:
        squares.append(value * value)
    return squares


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print("Input:", numbers)
    print("Squares:", square_numbers(numbers))
