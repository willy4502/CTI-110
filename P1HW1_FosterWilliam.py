print('-----Calculating Exponents-----')

print()
print()

print('Enter an integer as the base value:', end=' ')
base_value = int(input())
print('Enter an integer as the exponent:', end=' ')
exponent = int(input())

print()
print()

total = base_value ** exponent
print(base_value ,'raised to the power of' ,exponent ,'is' ,total ,'!!')

print()
print()

print('-----Addition and Subtraction-----')

print()
print()

print('Enter a starting integer:', end=' ')
start_int = int(input())
print('Enter a integer to add:', end=' ')
add_int = int(input())
print('Enter a integer to subtract:', end=' ')
sub_int = int(input())

total_2 = start_int + add_int - sub_int
print(start_int ,'+',add_int,'-' ,sub_int ,'is equal to' ,total_2)