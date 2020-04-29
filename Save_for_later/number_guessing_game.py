# Example: Number guessing game
#   - Python Indentation
#   - input()
#   - if

my_answer = 67
your_answer = input("Give me a number (from 0 to 100): ")
while (int(your_answer) != my_answer):
    if int(your_answer) > my_answer:
        print("Too big, try again...")
    else:
        print("Too small, try again...")
    your_answer = input("Give me a number (from 0 to 100): ")
print("You got it!! The answer is ",my_answer)

''' 
## version 0: Buggy version

my_answer = 67
your_answer = input("Give me a number (from 0 to 100): "):
while (your_answer != my_answer):
    if your_answer > my_answer:
      print("Too big, try again...")
    else
      print("Too small, try again...")
    your_answer = input("Give me a number (from 0 to 100): ")
    
    
'''

''' 
## version 2: Reducing two input() statements to one

my_answer = 67
your_answer = 1
while (your_answer != my_answer):
    your_answer = input("Give me a number (from 0 to 100): ")
    if your_answer > my_answer:
        print("Too big, try again...")
    else:
        print("Too small, try again...")
    
    
'''

'''
## version 3: Endless loop? (hint: wrong data type)

my_answer = 67
your_answer = input("Give me a number (from 0 to 100): ")
while (int(your_answer) != my_answer):
    if int(your_answer) > my_answer:
        print("Too big, try again...")
    else:
        print("Too small, try again...")
    your_answer = input("Give me a number (from 0 to 100): ")
print("You got it!! The answer is ",my_answer)
'''

