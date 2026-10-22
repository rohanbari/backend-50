def main() -> None:
    while True:
        print("Input several numbers (sep. by space) and hit Enter when done:")
        numString = input().strip()

        if len(numString) == 0:
            print("You can't leave the input blank.")

        try:
            numbers = list(map(int, numString.split()))
            result = largestSecond(numbers)

            if result is not None:
                largest, second = result
                print(f"Largest: {largest}, second largest: {second}")
        except ValueError as e:
            print("Error: Invalid value type. Retry")
            continue
        except KeyboardInterrupt as e:
            print("Bruh! Chill, I'm going. Bye.")
            exit(0)
        except Exception as e:
            print("Error:", e)


def largestSecond(numbers: list[int]):
    """Returns largest and second largest value in the list.

    Args:
        numbers (list[int]): The list to find values from

    Returns:
        _type_: Largest and second largest numbers [or] None
    """
    largest = secondLargest = None

    for num in numbers:
        if largest is None or num > largest:
            secondLargest, largest = largest, num
        elif num != largest and (secondLargest is None or num > secondLargest):
            secondLargest = num

    if secondLargest is None:
        return None

    return largest, secondLargest


if __name__ == "__main__":
    main()
