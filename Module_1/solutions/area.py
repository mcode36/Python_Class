''' Assignment
Write a python program called area.py :
   - The program will get 2 inputs from user : <base> and <height>
   - Calculate the area of the triangle and print the result.
   - Formula : area_of_triangle = <base> * <height> / 2
   - For example, if <base> is 20 and <height> is 10, the program should print something like this:
     The area of a triangle with base=20 and height=10 is: 100
'''

base = input('Base of the triangle?')
height = input('Height of the triangle?')
area = int (int(base) * int(height) / 2)

# print('The area of a triangle with base=', base, 'and height=', height, 'is:',area)

# print('The area of a triangle with base={} and height={} is: {}'.format(base,height,area))

print(f'The area of a triangle with base={base} and height={height} is: {area}')
