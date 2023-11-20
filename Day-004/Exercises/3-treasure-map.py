print("\nTreasure Map Game\n")

# Initialize the rows of the treasure map
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "️⬜️", "️⬜️"]
row3 = ["⬜️", "️⬜️", "️⬜️"]

# Group rows into a map
map = [row1, row2, row3]

# Display initial map
print(f"{row1}\n{row2}\n{row3}")

# Get user input for row and column
column_input = input("\nEnter the column number (1-3): \n['1'] ['2'] ['3']\n\n")
row_input = input("\nEnter the row number (1-3): \n\n['1']\n['2']\n['3']\n\n")

# Convert input to integers
column_pick = int(column_input) - 1
row_pick = int(row_input) - 1

# Check if the inputs are within the valid range
if 0 <= row_pick <= 2 and 0 <= column_pick <= 2:
    # Place 'X' at the chosen location on the map
    map[row_pick][column_pick] = "❌"
else:
    print("\nInvalid input. Please enter row and column numbers between 1 and 3.")

# Display updated map with treasure marked
print(f"\n{row1}\n{row2}\n{row3}")
