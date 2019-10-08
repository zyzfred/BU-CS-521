def main():
  # Students' answers to the questions
  answers = [
  ['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
  ['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'],
  ['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'],
  ['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'],
  ['A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
  ['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
  ['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
  ['E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D']]
  # Key to the questions
  keys = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']

  # Create a list to save grades
  grade_dict = dict()
  # Grade all answers
  for i in range(len(answers)):
    # Grade one student
    correctCount = 0
    for j in range(len(answers[i])):
      if answers[i][j] == keys[j]:
        correctCount += 1
    grade_dict[int(i)] = correctCount

  # sort with an increasing order and print
  for grade in sorted(grade_dict.values()):
    for sid in grade_dict.keys():
      if grade_dict[sid] == grade:
        print('Student', sid, '\'s correct count is', grade)
        grade_dict.pop(sid)
        break
    else:
        continue
  
main()