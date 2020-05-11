import moonlander

# testing show_welcome() -> None:
# moonlander.show_welcome()


# testing get_fuel() -> int:
# assert moonlander.get_fuel() == 80
# assert moonlander.get_fuel() == 800
# assert moonlander.get_fuel() == 100


# # testing get_fuel_rate(fuel_amount: int) -> int:
# assert moonlander.get_fuel_rate(2) == 2 
# assert moonlander.get_fuel_rate(4) == 4
# assert moonlander.get_fuel_rate(6) == 6


#  testing display_state(time: int, altitude: float, velocity: float, 
#  fuel_amount: int, fuel_rate: int) -> None:
# assert moonlander.display_state(2, 100, -10, 50, 8) == "Time: 2 s\n"\
# + "Fuel: 50 l\n"\
# + "Rate: 8 l/s\n"\
# + "Altitude: 100.00 m\n"\
# + "Velocity: -10.00 m/s\n"\
# assert moonlander.display_state(130, 50, -4.32, 80, 6) == "Time: 130 s\n"\
# + "Fuel: 80 l\n"\
# + "Rate: 6 l/s\n"\
# + "Altitude: 50.00 m\n"\
# + "Velocity: -4.32 m/s\n"\
# assert moonlander.display_state(10, 30, -0.65, 460, 3) == "Time: 10 s\n"\
# + "Fuel: 460 l\n"\
# + "Rate: 3 l/s\n"\
# + "Altitude: 30.00 m\n"\
# + "Velocity: -0.65 m/s\n"\


# # testing display_landing_status(velocity: float) -> None:
# assert moonlander.display_landing_status(-0.65) == "[LANDING STATUS] "\
# + "The Eagle has landed!"
# assert moonlander.display_landing_status(-4.82) == "[LANDING STATUS] "\
# + "Enjoy your oxygen while it lasts!"
# assert moonlander.display_landing_status(-20.13) == "[LANDING STATUS] "\
# + "Ouch, that hurt!"


# testing update_acceleration(gravity: float, fuel_rate: int) -> float:
assert moonlander.update_acceleration(1.62, 10) == 1.62
assert moonlander.update_acceleration(1.62, 0) == -1.62
assert moonlander.update_acceleration(1.62, 5) == 0
assert moonlander.update_acceleration(0, 3) == 0
assert moonlander.update_acceleration(1.62, 20) == 4.86


# testing update_altitude(altitude: float, velocity: float,  
#     acceleration: float) -> float:
assert moonlander.update_altitude(100.0, -50, 20) == 60
assert moonlander.update_altitude(0.0, -20.0, 100.0) == 30
assert moonlander.update_altitude(500.0, -30.0, 4.0) == 472


# testing update_velocity(velocity: float, acceleration: float) -> float:
assert moonlander.update_velocity(10, 30) == 40
assert moonlander.update_velocity(-20, 40) == 20
assert moonlander.update_velocity(30, 0) == 30
assert moonlander.update_velocity(0, 0) == 0
assert moonlander.update_velocity(0, 25) == 25
assert moonlander.update_velocity(-5, -10) == -15
assert moonlander.update_velocity(6, -10) == -4

# testing update_fuel(fuel_amount: int, fuel_rate: int) -> int:
assert moonlander.update_fuel(100, 9) == 91
assert moonlander.update_fuel(0, 0) == 0
assert moonlander.update_fuel(20, 0) == 20
