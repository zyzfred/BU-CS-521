# get a number 
i = eval(input("Enter the number of students: "))
score_list = []

while i > 0:
  score = eval(input("Enter each student's score: "))
  score_list.append(score)
  i -= 1

score_list.sort(reverse = True)

print("The highest score is:", score_list[0])
print("The second-highest score is:", score_list[1])