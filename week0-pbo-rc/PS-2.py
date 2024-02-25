n = int(input("Number of students : "))
print()

grade = {}

for i in range(n):
   name = input("Student's name : ")
   score = int(input("Score : "))
   print()
   grade.update({name : score}) 
print()

print(grade)
