def calculate_bmi(weight_pounds, height_feet, height_inches):
    weight_kg = weight_pounds * 0.453592

    total_height_inches = height_feet * 12 + height_inches
    height_m = total_height_inches * 0.0254

    bmi = weight_kg / (height_m**2)

    return round(bmi, 1)


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "UNDERWEIGHT"
    elif 18.5 <= bmi < 24.9:
        return "NORMAL"
    elif 25 <= bmi < 29.9:
        return "OVERWEIGHT"
    else:
        return "OBESE"
