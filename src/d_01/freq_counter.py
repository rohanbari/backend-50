from collections import Counter


def main() -> None:
    while True:
        print("Input a sentence below:")
        sentence = input().strip()

        if len(sentence) == 0:
            print("Bro, you can't leave the input blank. Try again!")
            continue

        words = sentence.split()
        counter = Counter(words)

        # Sorting items based on descending value of pairs
        sortedCounts = dict(sorted(counter.items(), key=lambda item: -item[1]))

        for key, value in sortedCounts.items():
            print(f"Word: {key} has occurred {value} times.")


if __name__ == "__main__":
    main()
