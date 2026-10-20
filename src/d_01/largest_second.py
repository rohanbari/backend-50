def main() -> None:
    while True:
        print("Input several numbers (sep. by space) and hit Enter when done:")
        numString = input().strip()

        if len(numString) == 0:
            print("You can't leave the input blank.")

        try:
            numbers = list(map(int, numString.split()))
            largest, second = largestSecond(numbers)

            print(f"Largest: {largest}, second largest: {second}")
        except ValueError as e:
            print("Error: Invalid value type. Retry")
            continue
        except KeyboardInterrupt as e:
            print("Bruh! Chill, I'm going. Bye.")
        except Exception as e:
            print("Error:", e)
            exit(1)


def largestSecond(numbers: list[int]) -> tuple[int, int]:
    largest = numbers[0]
    secondLargest = numbers[0]

    for num in numbers:
        if num > largest:
            secondLargest = largest
            largest = num
        elif num > secondLargest and num != largest:
            secondLargest = num

    return largest, secondLargest


if __name__ == "__main__":
    main()
