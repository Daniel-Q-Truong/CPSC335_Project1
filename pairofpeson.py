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
    


def main():
    row = [0, 2, 1, 3]
    minimumSwaps = getMinimumSwaps(row)
    print("Minimum number of swaps with row: "+str(minimumSwaps))

if __name__ == "__main__":
    main()
