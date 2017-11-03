# Kaprekar Numbers
> HCI Programming Challenge 12/12/2016 - thx tim!
___________



## Description
- A Kaprekar number for a given base is a non-negative integer, the representation of whose square can be split into two parts that add up to the original number again.
- By convention, the second part may start with the digit 0, but must be nonzero.
- For instance
     - 45 is a Kaprekar number, because 452 = 2025 and 20+25 = 45.


## Challenge
- Write a function that accepts two integer parameters representing the start and end of the range to scan, inclusively.
- Your function should return an array containing the Kaprekar numbers in that range, if any exist.
- We'll only be working with base 10 numbers.
- Assume that the following will be true of the input range values:
```
$start > 0
$start <= $end
```

## Samples
```
($low=5, $high=50) => [9, 45]
($low=100, $high=1000) => [297, 703, 999]
```

## Instructions
1. Copy all files from HCI's challenge code repo to your own directory
2. From your dir, open the file KaprekarNumbers.php
3. The calculate() method should return an array containing the Kaprekar numbers in the range [$start, $end]
4. To run the program, pass in the start and end of range:
```
./kaprekars.php 5 50
```
5. To run the unit tests:
```
# Standard unit tests:
phpunit --exclude-group large KaprekarNumbersTest

#Unit tests with large ranges:
phpunit KaprekarNumbersTest
```
