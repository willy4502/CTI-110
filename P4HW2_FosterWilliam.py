# William Foster
# 4-14-2025
# P42HW2
# 


total_employees = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

while True:
    emp_name = input("Enter employee's name or 'Done' to terminate: ")
    if emp_name == "Done":
        break

    hours = float(input(f"How many hours did {emp_name} work? "))
    pay_rate = float(input(f"What is {emp_name}'s pay rate? "))

    if hours > 40:
        over_hours = hours - 40
        reg_hours = 40
    else:
        over_hours = 0
        reg_hours = hours

    over_pay_rate = pay_rate * 1.5
    reg_pay = reg_hours * pay_rate
    over_pay = over_hours * over_pay_rate
    gross_pay = reg_pay + over_pay

   
    total_employees += 1
    total_overtime_pay += over_pay
    total_regular_pay += reg_pay
    total_gross_pay += gross_pay

    
    print()
    print(f"Employee name: {emp_name}")
    print()
    print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<12}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<10}")
    print("-" * 80)
    print(f"{hours:<15.2f}{pay_rate:<12.2f}{over_hours:<12.2f}{over_pay:<15.2f}{reg_pay:<15.2f}{gross_pay:<10.2f}")
    print()


print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")










print('---------------------------------------------------------------------------------')
print('Employee name: ', emp_name)
print('')
print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'Overtime':<10}"
      f"{'Overtime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<10}")
print('---------------------------------------------------------------------------------')
print(f'{hours:<12}{pay_rate:<12}{over_hours:<12}${over_pay:<15}${pay:<15}${gross_pay:<10}')








