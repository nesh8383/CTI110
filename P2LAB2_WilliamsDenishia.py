#denishia williams
#4/24/2024
#p2LAB2
#creating dictinary keys



print ("The keys in the dictionary is:")

print ("Camero","Prius", "Model S", "Silverado")

vehicle = {"Camero":18.21,"Prius":52.36, "Model S":110, "Silverado":26}
 

name = input("Enter a vehicle to see its mpg: ")


print(f'the {name} gets (mpg_dict{vehicle[name]} mpg.')
mpg = vehicle[name]


miles = float(input("How many miles will you drive with the "+name+":"))
gas = miles/mpg


print(f'{gas:2f} gallons of gas needed to drive the {name} {miles}')
