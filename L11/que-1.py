def get_integer_input():
    while True:
        user_input = input("Enter an integer: ")
        try:
            value = int(user_input)
            print(f"Valid integer entered: {value}")
            break
        except ValueError:
            print("Error: Input is not an integer. Please try again.")


get_integer_input()
