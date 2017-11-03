# Perfect Numbers
> HCI Programming Challenge 12/8/2015 - thx tim!
﻿_____________


## Description
Greek mathematicians were intrigued by certain characteristics of positive integers. They discovered that some numbers are equal  to the sum of their proper divisors. Greek mathematicians discovered a sense of balance or perfection in such numbers, and labeled them "perfect."  

A positive proper divisor is a positive divisor of a number n, excluding n itself. For example, 1, 2, and 3 are positive proper divisors of 6, but 6 itself is not.  

Whole numbers are said to be abundant, deficient or perfect. A whole number is abundant if the sum of its proper divisors is greater than the whole number. The whole number 12 is abundant.  Its proper divisors are 1, 2, 3, 4 and 6 and the sum of the proper divisors is 16, which is greater than 12.   

A whole number is deficient if the sum of its proper divisors is less than the whole number. The number 4 is deficient. Its proper divisors are 1 and 2 and the sum of its proper divisors is 3, which is less than 4.

## Output
Your program should output if the number is deficient, abundant, or perfect along with the amount by which it is abundant/deficient. The format of the output should match the following:  

```
Input: 4
Sum of positive divisors: 3
Output: 4 is deficient by 1
```

```
Input: 6
Sum of positive divisors: 6
Output: 6 is perfect
```

```
Input: 12
Sum of positive divisors: 16
Output: 12 is abundant by 4
```

```
Extra Credit
If the input value is not a positive whole number, throw an InvalidArgumentException
```

Instructions
1. Copy all files from HCI's code challenge repo to your own directory
2. From your dir, open the file NumberTheory.php and implement the numberType() method. That method should return the message indicating if the number if deficient, abundant, or perfect.
3. To run the program:
```
./numtype.php <number>
```
    - For example: ./numtype.php 10
4. To run the unit tests:
```
# Without the extra credit:
phpunit --filter testValid NumberTheoryTest

# With the extra credit:
phpunit NumberTheoryTest
```
