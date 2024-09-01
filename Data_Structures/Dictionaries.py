name = "Ashis Rai"
age = 18
height = 1.43
is_student = True
personal_info = {
    "Name" : name,
    "Age" : age,
    "Height" : height,
    "Is Student" : is_student
}
print(personal_info)

personal_info["Favourite Color"] = "Black"
print(personal_info)



#Since weight is not in the key dictionary it will show error
print(personal_info["weight"])
