import math


# Function to calculate the number of paint cans required
def paint_calc(height, width, cover):
    # Calculate total & round up to the nearest whole number
    num_cans = (height * width) / cover
    round_up_cans = math.ceil(num_cans)

    # Print the number of cans needed
    print(f"\nYou'll need {round_up_cans} cans of paint.")


print("\nPaint Area Calculator\n")
print(
    "Determines how many cans of paint is appropriate for your job.\n(Not tested and specific to a hypothetical can size.)\n"
)

# Coverage per can of paint
COVERAGE = 5

# Get wall height and width from user
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))

# Call function to calculate and display required paint cans
paint_calc(height=test_h, width=test_w, cover=COVERAGE)
