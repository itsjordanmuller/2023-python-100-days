def my_function():
    result = 3 * 2
    return result


my_function()


def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


formatted_string = format_name("JoRdAn", "MULLER")
print(formatted_string)

print(format_name("JoRdAn", "MULLER"))
