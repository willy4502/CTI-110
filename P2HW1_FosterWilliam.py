 # William Foster
 # 3-14-2025
 # P2HW2
 # a program that does some basic math on numbers (output will be nicely formatted)
 
print('This program calculates and displays travel expenses')
budget=float(input('Enter budget: '))
 
destination=(input('Enter your travel destination: '))

gas_s=float(input('How much do you think you will spend on gas? '))
 
hotel_s=float(input('Approximately, how much will you need for accomodation/hotel? '))

food_s=float(input('Last, how much do you need for food? '))
 
print()
 
print('------------Travel Expenses------------')

print(f"{'Location:':<18} {destination}")
print(f"{'Initial Budget:':<18} ${budget:,.2f}")
print(f"{'Fuel:':<18} ${gas_s:,.2f}")
print(f"{'Accommodation:':<18} ${hotel_s:,.2f}")
print(f"{'Food:':<18} ${food_s:,.2f}")


print('---------------------------------------')
print()

balance = budget - gas_s - hotel_s - food_s
 
print(f'Remaining Balance: ${balance:.2f}')