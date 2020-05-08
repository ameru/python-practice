def main() -> None:
    gravity = 1.62
    time = 0
    fuel_rate = 0
    velocity = 0.00
    acceleration = update_acceleration(gravity, fuel_rate)
    show_welcome()
    altitude = get_altitude()
    fuel_amount = get_fuel()
    display_state(time, altitude, velocity, fuel_amount, fuel_rate)
    while fuel_amount > 0 and altitude > 0.00:
        fuel_rate = get_fuel_rate(fuel_amount)
        fuel_amount = update_fuel(fuel_amount, fuel_rate)
        altitude = update_altitude(altitude, velocity, acceleration)
        velocity = update_velocity(velocity, acceleration)
        time += 1
        if fuel_amount == 0:
            fuel_rate = 0
            time -= 1
            while altitude > 0.00:
                time += 1
                display_state(time, altitude, velocity, fuel_amount, fuel_rate)
                fuel_amount = update_fuel(fuel_amount, fuel_rate)
                acceleration = update_acceleration(gravity, fuel_rate)
                altitude = update_altitude(altitude, velocity, acceleration)
                velocity = update_velocity(velocity, acceleration)
            time += 1
        if altitude == 0.00:
            display_landing_status(velocity)


# write other functions below this line
def show_welcome() -> None:
    print("Welcome aboard the Lunar Module (LM) Flight Simulator!")
    print()
    print("To begin, provide an initial altitude and fuel amount.")
    print("To simulate the actual LM, use 1300 meters and 500 liters.")
    print()


def get_altitude() -> float:
    altitude = float(input("Enter initial altitude (1 to 9999 meters): "))
    while (altitude < 1) or (altitude > 9999):
        print("[ERROR] Altitude out of range")
        altitude = float(input("Enter initial altitude (1 to 9999 meters): "))
    return altitude


def get_fuel() -> int:
    fuel_amount = int(input("Enter initial fuel amount (in liters): "))
    while fuel_amount < 0:
        print("[ERROR] Fuel amount must be positive")
        fuel_amount = int(input("Enter initial fuel amount (in liters): "))
    return fuel_amount


def get_fuel_rate(fuel_amount: int) -> int:
    fuel_rate = int(input("Enter fuel rate (0 to 9 liters per second): "))
    while (fuel_rate < 0) or (fuel_rate > 9):
        print("[ERROR] Fuel rate out of range")
        fuel_rate = int(input("Enter fuel rate (0 to 9 liters per second): "))
    if fuel_rate > fuel_amount:
        return fuel_amount
    else:
        return fuel_rate
    

def display_state(time: int, altitude: float, velocity: float, 
    fuel_amount: int, fuel_rate: int) -> None:
    if time == 0:
        print("")
        print("LM state at retrorocket cutoff")
        # print("")
        # print("Time: %d s"%(time))
        # print("Fuel: %d l"%(fuel_amount))
        # print("Rate: %d l/s"%(fuel_rate))
        # print("Altitude: %.2f m"%(altitude))
        # print("Velocity: %.2f m/s"%(velocity))
        print("")
    elif altitude == 0:
        print("")
        print("LM state at landing/impact")
        # print("")
        # print("Time: %d s"%(time))
        # print("Fuel: %d l"%(fuel_amount))
        # print("Rate: %d l/s"%(fuel_rate))
        # print("Altitude: %.2f m"%(altitude))
        # print("Velocity: %.2f m/s"%(velocity))
        print("")
    elif fuel_amount == 0:
        print("[OUT OF FUEL] Time: %d s Fuel: %d l Rate: %d l/s")
        print("Altitude: %.2f m Velocity: %.2f m/s")
        print("")
    if fuel_amount != 0:
        print("Time: %d s"%(time))
        print("Fuel: %d l"%(fuel_amount))
        print("Rate: %d l/s"%(fuel_rate))
        print("Altitude: %.2f m"%(altitude))
        print("Velocity: %.2f m/s"%(velocity))
        print("")


def display_landing_status(velocity: float) -> None:
    if (velocity > -1) and (velocity < 0):
        print("[LANDING STATUS] The Eagle has landed!")
    elif (velocity > -10) and (velocity < -1):
        print("[LANDING STATUS] Enjoy your oxygen while it lasts!")
    else:
        print("[LANDING STATUS] Ouch, that hurt!")


def update_acceleration(gravity: float, fuel_rate: int) -> float:
    return gravity * ((fuel_rate/5) - 1)

def update_altitude(altitude: float, velocity: float,  
    acceleration: float) -> float:
    return altitude + velocity + (acceleration/2)

def update_velocity(velocity: float, acceleration: float) -> float:
    return velocity + acceleration

def update_fuel(fuel_amount: int, fuel_rate: int) -> int:
    if fuel_rate <= fuel_amount:
        return fuel_amount - fuel_rate
    else:
        return 0


# no additional code below this line
if __name__ == "__main__":
    main()
