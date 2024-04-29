#Denishia williams
#4/26/2024
#P3LAB
#Branching 


change_amount = int(input() )

if change_amount <= 0:
    print("No change")
    

dollars = change_amount // 100


if dollars > 0 and change_amount > 0:
    change_amount = change_amount - (dollars * 100)
if dollars == 1:
    print(dollars, 'Dollar')
elif dollars > 1:
    print(dollars, 'Dollars')
    
quarters = change_amount // 25


if quarters > 0 and change_amount > 0:
    change_amount = change_amount - (quarters * 25)
if quarters == 1:
    print(quarters, 'Quarter')
elif quarters > 1:
    print(quarters, 'Quarters')
    
dimes = change_amount // 10


if dimes > 0 and change_amount > 0:
    change_amount = change_amount - (dimes * 10)
if dimes == 1:
    print(dimes, 'Dime')
elif dimes > 1:
    print(dimes, 'Dimes')
    

nickles = change_amount // 5


if nickles > 0 and change_amount > 0:
    change_amount = change_amount - (nickles * 5)
if nickles == 1:
    print(nickles, 'Nickel')
elif nickles > 1:
    print(nickels, 'Nickles')
    

pennies = change_amount // 1


if pennies > 0 and change_amount > 0:
    change_amount = change_amount - (pennies * 1)
if pennies == 1:
    print(pennies, 'Penny')
elif pennies > 1:
    print(pennies, 'Pennies')


