month = ["January" , "February" , "March" , "April" , "May" , "June" , "July" , "August" , "September" , "October" , "November" ,"December"]

inp = input()

d,m,y = inp.split("/")

print(month[int(m)-1] + " " +  d + ", " + y)