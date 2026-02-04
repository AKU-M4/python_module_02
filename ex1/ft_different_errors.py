def test_error_types():
    """ Testing function to handle all the required errors. """
    print("=== Garden Error Types Demo ===")

    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    # 2. ZeroDivisionError
    print("Testing ZeroDivisionError...")
    try:
        # Use numbers here, not the 'test' string variable
        result = 10 / 0

    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    # 3. FileNotFoundError
    print("Testing FileNotFoundError...")
    try:
        f = open("missing_file.txt", "r")
        f -= 1
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    # 4. KeyError
    print("Testing KeyError...")
    try:
        # Dictionary needs {Key: Value} syntax, not just {"Key"}
        my_plants = {"Sunflower": "Yellow", "Rose": "Red"}
        # Try to access a key that isn't there
        print(my_plants["Orchid"])
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    # 5. Multiple Errors Catching
    print("Testing multiple errors together...")
    try:
        result = 10 / 0
        result -= 1
    except (ValueError, ZeroDivisionError, FileNotFoundError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


def garden_operations():
    """ Function to execute all the tests errors and print them. """
    # You only need to call this once, and it runs all tests sequentially
    test_error_types()


if __name__ == "__main__":
    garden_operations()
