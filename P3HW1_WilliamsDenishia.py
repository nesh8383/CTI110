
# P3HW1
# Denishia williams
# 4/27/2024
# debugging


print("Enter your information below")

mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

# put grades entered to a list

grade = []

grade.append(mod1)
grade.append(mod2)
grade.append(mod3)
grade.append(mod4)
grade.append(mod5)
grade.append(mod6)

# result of the lowest, highest , sum and average for grades

print("------------Results------------")
print (f'Lowest Grade:  {min(grade)}')
print (f'Highest Grade: {max(grade)}')
print (f'Sum of Grades: {sum(grade)}')
average = sum(grade)/len(grade)
print (f'Average :      {average:.2f}')
print("---------------------------------------------")

# result of letter grade for average

# add in

if average >= 90:
   print("Your grade is: A")
   
   
if average <= 90 and average >= 80:
   print("Your grade is: B")
   
   
if average <= 80 and average >= 70:
   print("your grade is: C")
   
   
if average <= 70 and average >= 60:
   print("Your grade is D")

   
   
    # finish this







