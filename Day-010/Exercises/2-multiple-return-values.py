def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Empty Name, Please Provide a Valid Name"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"
