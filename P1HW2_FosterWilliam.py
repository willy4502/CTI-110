# William Foster
 # 3-1-2025
 # P1HW2
 # a program that does some basic math on numbers
 
print('This program calculates and displays travel expenses')
budget=int(input('Enter budget: '))
 
destination=(input('Enter your travel destination: '))

gas_s=int(input('How much do you think you will spend on gas? '))
 
hotel_s=int(input('Approximately, how much will you need for accomodation/hotel? '))

food_s=int(input('Last, how much do you need for food? '))
 
print()
 
print('-----Travel Expenses-----')
 
print('Location:',destination)
 
print('Initial Budget:',budget)
 
print()

print('Fuel:',gas_s) 
 
print('Accomodation:',hotel_s)

print('Food:',food_s)
 
print()

balance = budget - gas_s - hotel_s - food_s
 
print('Remaining Balance:',balance)