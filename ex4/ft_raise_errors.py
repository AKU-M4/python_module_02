def check_plant_health(plant_name, water_level, sunlight_hours):
    """ Function to check plant's health and to raise errors when needed """

    l_hour = f"Error: Sunlight hours {sunlight_hours} is too low (min 2)\n"
    h_hour = f"Error: Sunlight hours {sunlight_hours} is too high (max 12)\n"
    water_low = f"Error: Water level {water_level} is too low (min 1)\n"
    water_high = f"Error: Water level {water_level} is too high (max 10)\n"

    try:
        if plant_name is None:
            raise ValueError("plant_name can't be empty\n")
        elif water_level > 10:
            raise ValueError(water_high)
        elif water_level < 1:
            raise ValueError(water_low)
        elif sunlight_hours < 2:
            raise ValueError(l_hour)
        elif sunlight_hours > 12:
            raise ValueError(h_hour)
        else:
            print(f"Plant '{plant_name}' is healthy!\n")
    except ValueError as e:
        print(f"{e}")


def test_plant_checks():
    """ Function to test Errors """
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    check_plant_health('tomato', 10, 5)

    print("Testing empty plant name...")
    check_plant_health(None, 10, 5)

    print("Testing bad water level...")
    check_plant_health('tomato', 15, 5)

    print("Testing good values...")
    check_plant_health('tomato', 10, 0)

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
