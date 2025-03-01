def getMinSwaps(row):
    swaps = 0 # Initialize the function recording the amount of swaps taking place.
    # For loop iterates through the row and then performs a swap when a number is out of place.
    for i in range(0, len(row), 2):
        # Check if the next number represents the spouse
        potentialSpouse = row[i+1]
        # If the number next to row[i] is NOT the spouse (+1 to row[i]'s value)
        if row[i]+1 != row[i+1]:
            # Loop through row items starting from i+1 and ending at the row's length - index position + 1
            for j in range(i, (len(row))):
                # If the row's value is equal to row[i]'s value incremented by 1
                if row[j] == row[i]+1:
                    swaps+=1                        # Increment swaps
                    potentialSpouse = row[j]        # Set potential spouse to row[j]
                    row[j] = row[i+1]               # Swap row[j] with row[i+1]
                    row[i+1] = potentialSpouse      # Set row[i+1] to the value of the original row[j]
        
    return swaps
    


def main():
    row = [0, 2, 1, 3]
    minSwaps = getMinSwaps(row)
    print("Minimum number of swaps with row: "+str(minSwaps))

if __name__ == "__main__":
    main()
