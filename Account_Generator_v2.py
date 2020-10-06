# your code goes here
import random
name_list = ["Timmy Turner", "Trixie Tang", "Wanda Magic" ]
Id_value = list()
student_data2 = []

for name in name_list:
  x = random.randint(111111,999999)
  word = name.split()
  word = word[1]
  x2 = str(x)[3:6]
  student_names = {"Name" : str(name), "ID": str(x) , "Email" : str(name.lower()[0]) + str(word.lower()) + x2 + "@email.com" }
  student_data2.append(student_names)

student_data2

# Update the printing functionality to utilize this new dictionary variable to print out the student roster.
# What does this mean?

print(f"Student Roster\n")
for list_item in student_data2:
  print('Name:' + list_item['Name'] + '\nID:' + list_item['ID'] + '\nEmail:' + list_item['Email'] +'\n')
