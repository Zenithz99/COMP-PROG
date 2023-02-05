m = int(input())
score1 = 0
score2 = 0
for i in range(m*3) :
  inp = input()
  p1,p2 = inp[0],inp[2]
  if (p1 == "R" and p2 == "S") : score1 += 1
  elif (p1 == "S" and p2 == "P") : score1 += 1
  elif (p1 == "P" and p2 == "R") : score1 += 1
  elif (p2 == "R" and p1 == "S") : score2 += 1
  elif (p2 == "S" and p1 == "P") : score2 += 1
  elif (p2 == "P" and p1 == "R") : score2 += 1
  
  if score1 == m or score2 == m :
    print(score1,score2)
    if score1 == m :
      print("Player 1 wins")
    elif score2 == m :
      print("Player 2 wins")
    break
if not (score1 == m or score2 == m) :
  print(score1,score1)
  print("Tie")