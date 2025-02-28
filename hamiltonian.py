def find_preferred_starting_city(distances, fuel, mpg):
    """
    Finds the index of the preferred starting city for a cicular trip

    distances: List of distances between consecutive cities.
    fuel: List of fuel available at each city.
    mpg: Miles per gallon the car can travel.
    return: Index of the preferred starting city.
    """

    num_cities = len(distances)
    total_fuel_surplus = 0  # Tracks overall fuel surplus across all cities
    current_fuel = 0  # Tracks fuel balance while traveling
    start_city = 0  # Tracks the candidate starting city

    for i in range(num_cities):
        net_fuel = fuel[i] * mpg - distances[i]  # Fuel gained minus feel needed
        total_fuel_surplus += net_fuel  # Accumulate net fuel accross all cities
        current_fuel += net_fuel  # Update current fuel balance

        # If current fuel drops below zero, this city cannot be part of a valid route
        if current_fuel < 0:
            start_city = i + 1  # Set the next city as the new starting candidate
            current_fuel = 0  # Reset fuel balance for the new candidate
        
    # if total fuel is non-negative, a solution exists
    return start_city if total_fuel_surplus >= 0 else -1

def main():
    """Runs the function with sample input and prints the result."""
    distances = [5, 25, 15, 10, 15]
    fuel = [1, 2, 1, 0, 3]
    mpg = 10

    result = find_preferred_starting_city(distances, fuel, mpg)
    print(f"preferred starting city index: {result}")

if __name__ == "__main__":
    main()