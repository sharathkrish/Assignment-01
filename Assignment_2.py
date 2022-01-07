# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 07:46:12 2022

@author: hp
"""

1.What are the two values of the Boolean data type? How do you write them?

True or False 
bool() function used to define boolean data type


2. What are the three different types of Boolean operators?

AND, OR, NOT


3. Make a list of each Boolean operators truth tables (i.e. every possible combination of Boolean
values for the operator and what it evaluate ).

x y AND OR
0 0  0   0   
0 1  0   1   
1 0  0   1
1 1  1   1



4. What are the values of the following expressions?

(5 > 4) and (3 == 5)  ----->  FALSE

not (5 > 4) ----->  FALSE


(5 > 4) or (3 == 5) --------> TRUE

not ((5 > 4) or (3 == 5)) -------->FALSE

(True and True) and (True == False)  ------> FALSE

(not False) or (not True) -----------> TRUE 


5. What are the six comparison operators?

less than ( < ), 
less than or equal to ( <= ),
greater than ( > ), 
greater than or equal to ( >= ), 
equal to ( == ), 
and not equal to ( != ).


6. How do you tell the difference between the equal to and assignment operators?Describe a
condition and when you would use one.

The “=” is an assignment operator is used to assign the value on the right to the variable on the left.
The '==' operator checks whether the two given operands are equal or not. If so, it returns true. 
Otherwise it returns false.


7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print(&#39;eggs&#39;) ----- Block 1
if spam &gt; 5:
print(&#39;bacon&#39;) ----- Block 2 
else:
print(&#39;ham&#39;)
print(&#39;spam&#39;)
print(&#39;spam&#39;) ------ Block 3
      
      
8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam.

spam = 7
if   spam == 1:
    print("hello")
elif spam == 2:
    print("howdy")
else:
    print("anything else")
    
    
9.If your programme is stuck in an endless loop, what keys you’ll press?

press CTRL + C on the command line

10. How can you tell the difference between break and continue?

The Python break statement stops the loop in which the statement is placed. 
A Python continue statement skips a single iteration in a loop.

11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

for i in range(10):
    print(i, end=" ")
print()

for i in range(0,10):
    print(i, end=" ")
print()

for i in range(0,10,1):
    print(i, end=" ")
print()

Could not find any difference between each of them. 3rd one is used when we need to change the step size.

12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop.

for i in range(10):
    print(i, end=" ")
print()

i= 1
while(i<=10):
    print(i)
    i=i+1
        

13. If you had a function named bacon() inside a module named spam, how would you call it after
importing spam?

import spam
bacon() 
