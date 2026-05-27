# Week 2

light_year_km = 9260000000000
light_speed_km_per_second = 299792.458

def light_year_to_km(light_years):
    return light_years * light_year_km

def percent_light_speed_calculation(percent_speed):
    return (percent_speed / 100) * light_speed_km_per_second

def time_travel_years(distance_light_year, percent_speed):
    return distance_light_year / (percent_speed * light_speed_km_per_second)

def show_intro():
    print("Welcome to the Light-Year Travel Calculator!")
    print()
    print("This program estimates time traveled across space.")
    print("A light-year is a distance, not a unit of time.")
    print()

def main():
    show_intro()

    try:
        distance_light_year = float(input("Enter a distance in light-years: "))
        percent_light_speed = float(input("Enter travel speed as a % of light speed: "))
    except ValueError:
        print("Invalid response. Enter only numbers. ")
        return "Your insubordination to follow instructions leaves me baffled now be gone"
    
    if distance_light_year <= 0:
        print("Distance must be grater than 0. ")
        return

    elif percent_light_speed <= 0:
        print("Speed must be grater than 0. ")
        return 
    
    elif percent_light_speed >= 100:
        print("This is purely simulation so calculations will go forth but you have to understand in normal situations this breaks multiple laws of physics. ")
        print()

    print()
    

    percent_speed = percent_light_speed_calculation(percent_light_speed)
    time_to_travel = time_travel_years(distance_light_year, percent_light_speed)


    print(f"Distance, {distance_light_year:,}, light year.")
    print(f"Distance in km, {light_year_to_km(distance_light_year)}km.")
    print(f"Travel speed: {percent_speed}km/s")
    print(f"Estimated time: {time_to_travel}")

    print()

    print("Interception")
    print(f"At {percent_speed}% the speed of light, travelling {distance_light_year} light-years would take about {time_to_travel}. ")

main()
    

