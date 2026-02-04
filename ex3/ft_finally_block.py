def water_plants(plant_list):
    try:
        for n in plant_list:
            if not isinstance(n, str):
                raise ValueError(f"Cannot water {n} || INVALID INPUT!")
            else:
                print(f"Watering {n}")
    except ValueError as e:
        print(f"Found an invalid plant name: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===")

    normal_list = ["potato", "lilac", "tomato", "cucumber"]
    bad_list = ["potato", "lilac", "tomato", "cucumber", 41, normal_list]
    # testing with normal list
    print("Testing normal watering...")
    water_plants(normal_list)
    print("Watring completed successfully!\n")

    print("Testing with error...")
    water_plants(bad_list)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
