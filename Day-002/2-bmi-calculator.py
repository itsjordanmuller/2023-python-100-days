# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height_float = float(height)
weight_float = float(weight)
bmi = (weight_float) / (height_float**2)
print(int(bmi))
