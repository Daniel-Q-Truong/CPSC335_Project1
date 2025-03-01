# This function will return the minimum amount of swaps performed to arrange 'couples' in seats next to each other.
def getMinimumSwaps(row):
    #Variables:
    minimumSwaps = 0        # (Int) Minimum number of swaps returned by the function. Incremented in-loop.

    #The for loop will iterate through the table "row" from index 0 to the index representing the length of the array
    for i in range(0, len(row), 2):
        # row[i] represents individual one, and row[i+1] represents individual two.
        # Because couples come paired starting at (0,1),(2,3),etc, the number can be divided by 2 and rounded
        # to the lower number in order to be considered a match for row[i].
        if row[i] // 2 != row[i + 1] // 2:
            # If row[i+1] is not a couples match for row[i], then we shall iterate through the table again starting
            # from position i+1
            for j in range(i + 1, len(row)):
                # The if statement checks if the number found matches the original as a member of the 'couple'.
                if row[j] // 2 == row[i] // 2:
                    # The numbers are swapped and minimumSwaps is incremented by 1
                    temp = row[i+1]
                    row[i+1] = row[j]
                    row[j] = temp
                    minimumSwaps += 1
    return minimumSwaps
    
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
    print("Algorithm 1: Greedy Approach to Hamiltonian Problem\n")
    #Algorithm 1: Greedy Approach to Hamiltonian Problem
    distances = [5, 25, 15, 10, 15]
    fuel = [1, 2, 1, 0, 3]
    mpg = 10

    result = find_preferred_starting_city(distances, fuel, mpg)
    print(f"preferred starting city index: {result}")

    print("\nAlgorithm 2: Connecting Pairs of Persons\n")
    #Algorithm 2: Connecting Pairs of Persons
    row = [0, 2, 1, 3]
    minimumSwaps = getMinimumSwaps(row)
    print("Minimum number of swaps with row: "+str(minimumSwaps))

if __name__ == "__main__":
    main()
