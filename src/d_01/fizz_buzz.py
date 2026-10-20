def main() -> None:
    while True:
        try:
            num = int(input("Input a number: "))

            if num % 15 == 0:
                print("FizzBuzz")
            elif num % 3 == 0:
                print("Fizz")
            elif num % 5 == 0:
                print("Buzz")
            else:
                print("It's not a FizzBuzz-able number.")
        except KeyboardInterrupt as e:
            print("\nThanks for using this program!")
            exit(0)
        except Exception as e:
            print("Error: It's not a valid number!")


if __name__ == "__main__":
    main()
