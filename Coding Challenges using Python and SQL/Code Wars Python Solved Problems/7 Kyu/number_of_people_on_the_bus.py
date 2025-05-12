# Question: Number of People in the Bus
# Categories: 7 Kyu

def number(bus_stops: list[list[int]]) -> int:
    total_number_of_people = 0

    for i in range(len(bus_stops)):
        people_that_get_on_the_bus = bus_stops[i][0]
        people_that_left_the_bus = bus_stops[i][1]

        total_number_of_people += people_that_get_on_the_bus
        total_number_of_people -= people_that_left_the_bus
    
    return total_number_of_people