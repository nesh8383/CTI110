# denishia williams
# 4/26/2024
# P3HW3
# understanding of decision structures




#ask user to enter name of employee:
name = input("Enter the name of the employee: ")

#ask user to enter number of hours worked:
hours = float(input("please enter hours worked: "))

#ask user to enter employee's pay rate:
rate = float(input("please enter rate of pay:  "))





 
    
if hours > 40:
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (rate * 1.5)
else:
    overtime_pay = 0


regular_pay = 40 * rate
total_pay = regular_pay + overtime_pay


    









print("---------------------------------------------------------")

print("Employee name: Denishia Williams")

print("Hours worked\t",   "pay Rate\t",   "overtime\t",   "Overtime Pay\t",   "reghour Pay\t",  "gross Pay")
print("--------------------------------------------------------------------------------------------------------")
print(hours,"\t\t",  rate,"\t\t",  overtime_hours,"\t\t",  overtime_pay,"\t",  regular_pay,"\t\t",  total_pay,"\t\t")
