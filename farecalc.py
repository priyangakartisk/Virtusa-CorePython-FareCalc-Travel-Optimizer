

vehicle_rates = {
    'Economy' : 10,
    'Premium' : 18,
    'SUV'     : 25
}

def calculate_fare(km, vehicle_type, hour):

    vehicle_type = vehicle_type.strip().title()

    if vehicle_type not in vehicle_rates:
        return None, None, None

    rate      = vehicle_rates[vehicle_type]
    base_fare = km * rate

    if 17 <= hour <= 20:
        surge_multiplier = 1.5
        is_peak          = True
    else:
        surge_multiplier = 1.0   
        is_peak          = False

    final_fare = base_fare * surge_multiplier

    return base_fare, final_fare, is_peak


def get_number(prompt, num_type=float):
    while True:
        try:
            value = num_type(input(prompt))
            if value < 0:
                print("  ⚠  Please enter a positive number.\n")
            else:
                return value
        except ValueError:
            print("  ⚠  That doesn't look like a number. Try again.\n")


def print_receipt(name, vehicle_type, km, hour, base_fare, final_fare, is_peak):

    vehicle_type = vehicle_type.strip().title()
    rate         = vehicle_rates[vehicle_type]
    surge_label  = "YES  (×1.5 — Peak Hours 5PM–8PM)" if is_peak else "NO"

    print()
    print("╔══════════════════════════════════════════╗")
    print("║        CityCab  —  Ride Price Receipt     ║")
    print("╠══════════════════════════════════════════╣")
    print(f"║  Passenger   : {name:<27}║")
    print(f"║  Vehicle     : {vehicle_type:<27}║")
    print(f"║  Rate        : ${rate:<2} per km                   ║")
    print(f"║  Distance    : {km:<6.1f} km                      ║")
    print(f"║  Hour        : {hour:<2}:00                         ║")
    print("╠══════════════════════════════════════════╣")
    print(f"║  Base Fare   : ${base_fare:<26.2f}║")
    print(f"║  Surge       : {surge_label:<27}║")
    print("╠══════════════════════════════════════════╣")
    print(f"║  FINAL FARE  : ${final_fare:<26.2f}║")
    print("╚══════════════════════════════════════════╝")
    print()


def main():

    print("╔══════════════════════════════════════════╗")
    print("║      Welcome to FareCalc by CityCab       ║")
    print("║      Type EXIT as name to quit            ║")
    print("╚══════════════════════════════════════════╝")

    print("\n  Available Vehicles:", list(vehicle_rates.keys()))

    while True:

        print()

        name = input("Enter Passenger Name (or EXIT): ").strip()

        if name.upper() == "EXIT":
            print("\n  Thanks for using CityCab. Safe travels!\n")
            break

        if name == "":
            print("  ⚠  Name cannot be blank. Try again.")
            continue

        vehicle_input = input("Enter Vehicle Type (Economy / Premium / SUV): ").strip().title()

        if vehicle_input not in vehicle_rates:
            print(f"\n  ✖  Service Not Available: '{vehicle_input}' is not in our fleet.")
            print(f"     Available options are: {list(vehicle_rates.keys())}\n")
            continue

        km = get_number("Enter Distance (km)           : ", float)

        while True:
            hour = get_number("Enter Hour of Day (0-23)      : ", int)
            if 0 <= hour <= 23:
                break
            print("  ⚠  Hour must be between 0 and 23.\n")

        base_fare, final_fare, is_peak = calculate_fare(km, vehicle_input, hour)

        print_receipt(name, vehicle_input, km, hour, base_fare, final_fare, is_peak)


if __name__ == "__main__":
    main()
