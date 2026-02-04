def check_temperature(temp_str):
    """ Basic function that tests temperature and checks if it's valid """
    print(f"Testing Temperature: {temp_str}")
    try:
        temp = int(temp_str)
        if temp < 0:
            print(f"Error: {temp} is too cold for a plants (min 0°C)")
        elif temp > 40:
            print(f"Error: {temp} is too hot for a plants (min 40°C)")
        else:
            print(f"Temperature {temp} is perfect for plants!")
    except Exception:
        print(f"Error: {temp_str} is not a valid number")


if __name__ == "__main__":
    print("=== Garden temperature Checker ===")

    values = {"abc", "40", "60", "-50"}
    for s in values:
        check_temperature(s)
        print()

    print("All tests completed - program didn't crash!")
