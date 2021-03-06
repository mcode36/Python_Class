# Python Genius Class: Week 1

  - Print(), Input()
  - Comment
  - Variables
  - If statement

## Highlights
1. How to run python program

   Use YourName.py to demonstrate:
   - python IDLE
   - on command line
   
2. Python Indentation

   - What is block of code : YourName.py

3. Comments
   - Why do we need comments
     - As a reminder
     - Experiment with different codes
   - \# : For single line comments
   - \'\'\' : For multiple line comments

4. Print (example: print.py)
   - Basic print
   - print with no new line
   - format print

5. Python Variables

   - Syntax: variable = value
   - Variable's type can be changed over time
   - String variables can be declared either by using single or double quotes
   - Restriction on variable names
     - Can only contain alpha-numeric characters and underscores
     - cannot start with a number
     - Variable names are case-sensitive

   - Global variables and scopes: Explained in later chapters

6. Python Conditions: If Statement
   - "if:" clause
   - "if: ... else:" clause
   - Comparison Operators: 
     - ==, !=
     - \> , \>=
     - \< , \<=
     
   - Logic operators: 'AND', 'OR'
   - 'Pass' statement

## Challenges

1. Write a python program called area.py :
   - The program will get 2 inputs from user : <base> and <height>
   - Calculate the area of the triangle and print the result.
   - Formula : area_of_triangle = <base> * <height> / 2
   - For example, if <base> is 20 and <height> is 10, the program should print something like this:
     The area of a triangle with base=20 and height=10 is: 100

2. Write a python program called your_score.py :
   - The program will take two inputs from user: <name> and <score>
   - If score is 'equal or greater than' 60, print:
     Good job, <name> !! You passed.
   - If score is less than 60, print:
     Oops, <name>, you failed. Try harder next time.

3. Write a python program called grade.py
   - The program will take two inputs from user: <name> and <score>
   - Depending on the score, the program will print:
     "Hi, <name>, your grade is <grade>"
   - Grading:
     - E : when score is less than 60 (not including 60)
     - D : when score is greater or equal 60 AND less than 70
     - C : when score is greater or equal 70 AND less than 80
     - B : when score is greater or equal 80 AND less than 90
     - A : when score is greater or equal 90 AND less than 100
   - When grading is 'A', print extra line : "Wow, Excellent!!"

4. Bonus: Write a python program to convert Celsius to Fahrenheit:
   - The program will first ask user whether they want to:
     - Convert from Celsius to Fahrenheit
     - Convert Fahrenheit to Celsius
   - Then the program will ask for a number. The prompt should based on question 1. For example:
     Temperature (in degC) ? 
   - Calculate result. FOr example:
     30 degC = 86 degF
