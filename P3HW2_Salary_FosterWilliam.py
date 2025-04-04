# William Foster
# 3-27-2025
# P3HW2
# formatting strings to make them display nicely
emp_name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
if hours > 40:
    over_hours = hours - 40
else: 
    over_hours = 0
over_pay_rate = pay_rate * 1.5
pay = min(hours, 40) * pay_rate
over_pay = over_hours * over_pay_rate
gross_pay = pay + over_pay

over_pay = over_hours * over_pay_rate













print('---------------------------------------------------------------------------------')
print('Employee name: ', emp_name)
print('')
print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'Overtime':<10}"
      f"{'Overtime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<10}")
print('---------------------------------------------------------------------------------')
print(f'{hours:<12}{pay_rate:<12}{over_hours:<12}${over_pay:<15}${pay:<15}${gross_pay:<10}')








