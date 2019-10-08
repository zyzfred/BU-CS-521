import os.path
infile = input('Enter a filename: ')

if os.path.isfile(infile) == False:
  print(infile, "does not exist")
else:
  rmSTR = input('Enter the string to be removed: ')
  outfile = rmSTR + "_removed_file.txt"
  fin = open(infile)
  fout = open(outfile, "w")
  for line in fin:
    line = line.replace(rmSTR, "")
    fout.write(line)
  fin.close()
  fout.close()
  print('Done')
