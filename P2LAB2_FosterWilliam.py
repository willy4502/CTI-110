# William Foster
# 3-10-25
# P2LAB2
# Code that uses a dictionary to store user input and displays output to the user

cars = {
 
'Camaro': 18.21,
 
'Prius': 52.36,
 
'Model S': 110,
 
'Silverado': 26
 
}
print('Cars:', cars.keys())
car = input("Enter a vehicle to see its mpg: ")
 
print()
 
sp_car = cars[car]
 
print(f"The {car} gets {sp_car} mpg.")
print()
miles = float(input(f"How many miles will you drive the {car}?: "))
print()
gas_needed = miles / sp_car
print(f'{gas_needed:.2f} gallon(s) of gas are needed to drive the {car} {miles} miles.')