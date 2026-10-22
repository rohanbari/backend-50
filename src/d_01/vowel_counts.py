import sys


def main() -> None:
    while True:
        try:
            print("Input a sentence and hit enter:")
            string = input()

            print(f"Total vowel count: {countVowels(string)}")
        except KeyboardInterrupt as e:
            print("\nThank you for using this program.")
            sys.exit(0)
        except Exception as e:
            print("This is an ill-formed sentence. Please retry.")


def countVowels(string: str) -> int:
    """Counts vowels in the given string.

    Args:
        string (str): String to count vowels from

    Returns:
        int: No. of vowels
    """
    count = 0
    for char in string.lower():
        if char in "aeiou":
            count += 1

    return count


if __name__ == "__main__":
    main()
