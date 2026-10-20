def main() -> None:
    print("Input a sentence and hit enter:")
    string = input()

    print(f"Total vowel count: {countVowels(string)}")


def countVowels(string: str) -> int:
    count = 0
    for char in string.lower():
        if char in "aeiou":
            count += 1

    return count


if __name__ == "__main__":
    main()
