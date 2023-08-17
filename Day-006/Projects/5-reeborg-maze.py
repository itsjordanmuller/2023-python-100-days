# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# Use the below code to help Reeborg navigate a maze

# def turn_right():
#   turn_left()
#   turn_left()
#   turn_left()

# while not at_goal():
#   if right_is_clear():
#       turn_right()
#       move()
#   elif front_is_clear():
#       move()
#   else:
#       turn_left()

# Challenge Test Maze 1 2 & 3
# Reeborg Gets Stuck Sometimes, Use the Below Code to Fix:

# def turn_right():
#   turn_left()
#   turn_left()
#   turn_left()

# while not at_goal():
#   if right_is_clear() and front_is_clear():
#       turn_left()
#   if right_is_clear():
#       turn_right()
#       move()
#   elif front_is_clear():
#       move()
#   else:
#       turn_left()
