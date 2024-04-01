#Lists inside the list stored in the 'students' variable
students = [['BSIT',['David', 'Alenere']], ['BSCS', ['Jaymar', 'Emman', 'Patrick']]]

for student in students:
  print(student[0])
  for y in student[1]:
    print(' -',y)
  print()