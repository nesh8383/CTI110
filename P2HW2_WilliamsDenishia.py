#denishia Williams
#4/21/2024
#P2HW2
#design program that ask user to enter grades





module1 = float(input("Enter grade for module 1: "))
module2 = float(input("enter grade for module 2: "))
module3 = float(input("enter grade for module 3: "))
module4 = float(input("enter grade for module 4: "))
module5 = float(input("enter grade for module 5: "))
module6 = float(input("enter grade for module 6: "))



grade =[]
#add grade to list

grade.append(module1)
grade.append(module2)
grade.append(module3)
grade.append(module4)
grade.append(module5)
grade.append(module6)




print("------------Results------------")
print(f'Lowest Grade:  {min(grade)}')
print(f'highest Grade: {max(grade)}')
print(f'sum of Grade:  {sum(grade)}')
#print {max(grade)} f string needed
#print {sum(grade)} f string needed

Average = sum(grade)/len(grade)
print(f'Average :      {Average:.2f}')

print("------------------------------------------")



