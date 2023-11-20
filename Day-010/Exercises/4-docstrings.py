def format_name(f_name, l_name):
    """Format first and last name to title case.
    Return error message if either name is empty"""
    if f_name == "" or l_name == "":
        return "Empty Name, Please Provide a Valid Name"

    # Convert names to title case
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    # Return the formatted full name
    return f"\n{formatted_f_name} {formatted_l_name}"


print("\nDocstrings Tutorial\n")
print("Name Formatter\n")

# Prompt user for first and last name, and print formatted name
print(
    format_name(
        input("What is your first name? "),
        input("What is your last name? "),
    )
)
