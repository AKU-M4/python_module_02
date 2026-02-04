class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:

    def __init__(self):
        self.plants = []
        self.water_tank = 20

    def add_plant(self, plant_name):
        try:
            if plant_name is None:
                raise PlantError("Plant name can't be empty\n")
            self.plants.append(plant_name)
            print(f"Added {plant_name} Successfully")

        except PlantError as e:
            print(f"{e}")

    def watering_plants(self):
        print("Watering plants...")
        try:
            print("Opening Water system")
            if (self.water_tank < 5):
                raise WaterError("Not enough water in the tank")

            for n in self.plants:
                print(f"Watering {n} - success")
                self.water_tank -= 5

        except WaterError as e:
            raise e

        except Exception as e:
            print(f"Unexcpected error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self, plant_name, water_level, sun_level):
        try:
            if water_level > 10:
                raise ValueError(f"Water level {water_level}"
                                 f"is too high (max 10)")
            print(f"{plant_name}: healthy (water: {water_level},"
                  f"sun: {sun_level})")
        except ValueError as e:
            print(f"Error checking {plant_name}: {e}")


def test_garden_management():
    print("=== Garden Management System ===")

    manager = GardenManager()

    print("Adding plants to garden...")
    manager.add_plant("tomato")
    manager.add_plant("lettuce")
    manager.add_plant("")  # Error

    print("\nWatering plants...")
    try:
        manager.watering_plants()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nChecking plant health...")
    manager.check_health("tomato", 5, 8)
    manager.check_health("lettuce", 15, 8)  # Error

    # 4. Simulate severe failure
    print("\nTesting error recovery...")
    manager.water_tank = 0  # Empty tank
    try:
        manager.watering_plants()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
