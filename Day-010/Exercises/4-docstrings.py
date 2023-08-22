def format_name(f_name, l_name):
    """Take a first and last name and format it
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "Empty Name, Please Provide a Valid Name"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


print(
    format_name(
        input("What is your first name? "),
        input("What is your last name? "),
    )
)
