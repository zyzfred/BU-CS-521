ROW_NUM = 3
COLUMN_NUM = 4

def get_matrix():
  matrix = []

  s1 = input('Enter a 3-by-4 matrix row for row 0: ')
  s2 = input('Enter a 3-by-4 matrix row for row 0: ')
  s3 = input('Enter a 3-by-4 matrix row for row 0: ')

  s1_list = s1.split(' ')
  s2_list = s2.split(' ')
  s3_list = s3.split(' ')

  row0 = [eval(n) for n in s1_list] 
  row1 = [eval(n) for n in s2_list] 
  row2 = [eval(n) for n in s3_list] 

  matrix.append(row0)
  matrix.append(row1)
  matrix.append(row2)
  
  return matrix

def sumColumn(m, columnIndex):
  sum = 0
  for i in range(ROW_NUM):
    sum = sum + m[i][columnIndex]
  
  return sum

def main():

  m_input = get_matrix()

  for i in range(COLUMN_NUM):
    sum_column = sumColumn(m_input, i)
    print('Sum of the elements for column', i, 'is', sum_column)

main()