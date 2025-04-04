 # William Foster
 # 3-16-2025
 # P2HW2
 # code for grade info
module_1=float(input('Enter grade for Module 1: '))
module_2=float(input('Enter grade for Module 2: '))
module_3=float(input('Enter grade for Module 3: '))
module_4=float(input('Enter grade for Module 4: '))
module_5=float(input('Enter grade for Module 5: '))
module_6=float(input('Enter grade for Module 6: '))

module_grades=[module_1,module_2,module_3,module_4,module_5,module_6]

low_grade=min(module_grades)
high_grade=max(module_grades)
total_grade=sum(module_grades)
num_grade=len(module_grades)
avg_grade= total_grade / num_grade


print()

print('----------Results----------')

print(f'Lowest Grade: {low_grade:.1}') 
print(f'Highest Grade: {high_grade:.1f}')
print(f'Sum of Grades: {total_grade:.1f}')
print(f'Average: {avg_grade:.2f}')

print('---------------------------')

'''
Pseudocode:

    DISPLAY "Enter grade for Module 1: "
    READ module_1 AS FLOAT

    DISPLAY "Enter grade for Module 2: "
    READ module_2 AS FLOAT

    DISPLAY "Enter grade for Module 3: "
    READ module_3 AS FLOAT

    DISPLAY "Enter grade for Module 4: "
    READ module_4 AS FLOAT

    DISPLAY "Enter grade for Module 5: "
    READ module_5 AS FLOAT

    DISPLAY "Enter grade for Module 6: "
    READ module_6 AS FLOAT

    Store all grades in a list
    
    SET module_grades TO [module_1, module_2, module_3, module_4, module_5, module_6]

    Calculate required values

    SET low_grade TO MINIMUM OF module_grades
    SET high_grade TO MAXIMUM OF module_grades
    SET total_grade TO SUM OF module_grades
    SET num_grade TO LENGTH OF module_grades
    SET avg_grade TO total_grade / num_grade

    DISPLAY "--------Results--------"
    DISPLAY "Lowest Grade: " + FORMAT low_grade TO 2 DECIMAL PLACES
    DISPLAY "Highest Grade: " + FORMAT high_grade TO 2 DECIMAL PLACES
    DISPLAY "Sum of Grades: " + FORMAT total_grade TO 2 DECIMAL PLACES
    DISPLAY "Average: " + FORMAT avg_grade TO 2 DECIMAL PLACES
    DISPLAY "-----------------------"
'''
