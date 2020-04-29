# Python Genius CLass: Week 2

  - Data Types
  - Booleans
  - Operators
  - For Loops

## Highlights

1. Data Types

   - Python has these built-in data types:
     - **str**
     - **int**, **float**, complex
     - **list**, **tuple**, range
     - **dict**
     - set frozenset
     - **bool**
     - bytes, bytearray, memoryview
   - type() : get data type of a variable

   Practice: Use type(x) == str to check if x is a string
   
2. Booleans

   - These is only two values for Booleans: True or False
   - bool() : Evaluate value and return True or False
   - These values are considered False:
     - None : 
     - 0  : Number 0
     - "" : Empty string
     - () : Empty tuple
     - [] : Empty list (or empty array)
     - {} : Empty dictionary

3. Operators
   - Arithmetic operators: +, -, *, / ...
   - Assignment Operators: =,  +=, -= ...
   - Comparison Operators: ==,  !=,  \<,  \>,  \<=  ...
   - Logical Operators: and,  or,  not ...
   - Identity Operators: is, is not
   - Membership Operators: in, not in
   - Bitwise Operators: &, |, ^, ~, \<\<, \>\>

4. For loops
   - for something in List_or_array:
   - range() function: range(start,end,step)
   - for variable in range():
   - break, continue

   Practice: Write a program to calculate the sum of all the numbers from 1 to 50

## Challenges

1. Write a program to calculate the sum of all the even numbers from 0 to 100

2. Write a program called boohoo.py:
   - loop x from 1 to 100
   - if x is multiple of 2, print "boo"
   - if x is multiple of 3, print "hoo"
   - if x is multiple of both 2 and 3, print "boohoo"

3. Write a program called xmas_tree.py:
   - The program will take one odd number from user
   - If number fall out of range (3 to 7),  the program will quit with an error message
   - The program will print tower based on the input number.
   - For example, if the number is 5, the print result should look like this:
   ~~~~
       *
      ***
     *****
    *******
   *********
   ~~~~


