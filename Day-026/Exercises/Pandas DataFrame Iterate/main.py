import pandas

student_dict = {"student": ["Jordan", "James", "Lily"], "score": [56, 76, 98]}

# for key, value in student_dict.items():
#     print(key)
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
