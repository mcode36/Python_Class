## Special project: FInd all the factors of an integer number

- Background: See https://www.mathsisfun.com/numbers/factors-all-tool.html

- Let's say the given number is N. 
- We will use linear search to try out all the numbers in between 1 to N/2.
  We can skip the numbers larger than N/2 because:
  Assume y = N/2
  It also means N/y = 2
  So if N/(y+1) the result is smaller than 2. And we know there is no possible integer between 1 and 2.
  
So here is the program:
