 # William Foster
 # 3-8-2025
 # P2LAB1
 # how to write code that performs mathematical calculations and displays information to users


import math

radius = float(input('What is the radius of the circle?: '))
diamater = radius * 2
circum = 2 * radius * math.pi
area = math.pi * radius ** 2
print(f'The diameter of the circle is: {diamater:.1f}')
print(f'The circumference of the circle is: {circum:.2f}')
print(f'The area of the circle is: {area:.3f}')
