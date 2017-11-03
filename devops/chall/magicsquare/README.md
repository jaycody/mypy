# Magic Squares
> HCI Programming Challenge 6/6/2016 - thx tim!
_________________


## Description
- A magic square is a N x N grid of the distinct, positive integers 1, 2, ...N2 such that each row, column, and major diagonal adds up to the same number, known as the magic constant.
- The magic constant can be calculated as:  
```
½ * N * (N2 + 1)
```

## Example of a 3x3 magic square:


### MagicSquare
- The major diagonals are 8 + 5 + 2 and 6 + 5 + 4.
- Write a function that accepts an array representing a grid containing the numbers in the square and determines whether it's magic by returning true or false.
- We'll represent the grid layout in input as a one dimensional array. For example:
```
[8, 1, 6, 3, 5, 7, 4, 9, 2]
```

### Samples
```
[8, 1, 6, 3, 5, 7, 4, 9, 2] => true
[8, 6, 1, 3, 5, 7, 4, 9, 2] => false
[2, 7, 6, 9, 5, 1, 4, 3, 8] => true
[1, 10, 12, 5, 13, 15, 11, 2, 3, 16, 4, 6, 14, 7, 8, 9] => false
[16, 3, 2, 13, 5, 10, 11, 8, 9, 6, 7, 12, 4, 15, 14, 1] => true
```

### Extra Credit
- Throw an InvalidArgumentException if the input does not meet the grid criteria


## Instructions
1. Copy all files from HCI's code challenge dir to your own directory
2. From your dir, open the file Grid.php
3. The constructor should accept a one-dimensional array representing the arrangement of integers in a NxN grid
4. The isMagicSquare() method should return a boolean indicating whether the
5. To run the program:
```
./magicsquare.php "8, 1, 6, 3, 5, 7, 4, 9, 2"
```
6. To run the unit tests:
```
# Without the extra credit
phpunit --exclude-group extracredit GridTest

#With the extra credit:
phpunit GridTest
```
