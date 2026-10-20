def main() -> None:
    while True:
        try:
            print("Input a string below and hit enter when done:")
            string = input()

            rev = "".join(reversed(string))
            print("Reversed:", rev)
        except KeyboardInterrupt as e:
            print("Thanks for using this program, bye!")
            exit(0)
        except Exception as e:
            print("Ouch! That's an ill-formed sentence. Retry!")


if __name__ == "__main__":
    main()
