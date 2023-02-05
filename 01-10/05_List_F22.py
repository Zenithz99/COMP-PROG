def index_of(grades, ID):
  out = -1
  for i in range(len(grades)) :
    if grades[i][0] == ID : 
      out = i
      break
  return out
def plus_grade(x) :
  if x == "A" : return "A"
  elif x == "B+" : return "A"
  elif x == "B" : return "B+"
  elif x == "C+" : return "B"
  elif x == "C" : return "C+"
  elif x == "D+" : return "C"
  elif x == "D" : return "D+"
  elif x == "F" : return "D"
def firstsort(x) :
    return x[0]
def upgrade(grades, IDs):
  new_grades = []
  for i in range(len(grades)) :
    if grades[i][0] in IDs :
      new_grades.append([grades[i][0],plus_grade(grades[i][1])])
    else :
      new_grades.append([grades[i][0],grades[i][1]])
  new_grades.sort(key = firstsort)
  grades.clear()
  for i in range(len(new_grades)) :
    grades.append(new_grades[i])
  return 
# DON'T remove the following three lines
exec(input())
exec(input())
exec(input())