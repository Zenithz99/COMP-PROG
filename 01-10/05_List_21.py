def plus_grade(x) :
  if x == "B+" : return "A"
  elif x == "B" : return "B+"
  elif x == "C+" : return "B"
  elif x == "C" : return "C+"
  elif x == "D+" : return "C"
  elif x == "D" : return "D+"
  elif x == "F" : return "D"

x = input()
list_name = []
list_grade = []
while x != "q" :
  student_id , student_grade = x.split(" ")
  list_name.append(student_id)
  list_grade.append(student_grade)
  x = input()
t = [x for x in input().split(" ")]

new_list_grade = []
for i in range(len(list_name)) :
  if list_name[i] in t :
    print(list_name[i],plus_grade(list_grade[i]))
  else :
    print(list_name[i],list_grade[i])