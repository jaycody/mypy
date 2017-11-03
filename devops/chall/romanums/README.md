# Roman Numerals
> HCI Programming Challenge 3/20/2017 - thx tim!
______________

## Challenge
Write a function that accepts an integer parameter. Your function should return a string with the Roman numeral representation. Only positive integers greater than 0 should be accepted, otherwise throw an InvalidArgumentException.


## Description of Roman numerals

```
Symbol
	I
	V
	X
	L
	C
	D
	M
	Number
	1
	5
	10
	50
	100
	500
	1000


Number
	4
	9
	40
	90
	400
	900
	Symbols
	IV
	IX
	XL
	XC
	CD
	CM
	

Samples
1 => I
2 => II
3 => III
4 => IV
5 => V
6 => VI
7 => VII
8 => VIII
9 => IX
10 => X

```


## Instructions
1. Copy all files from HCI's code challlenge dir to your own directory
2. From your dir, open the file RomanNumeral.php
3. The toRoman() method should return a string with the Roman numeral representation of the input
4. To run the program, pass in the start and end of range:
```
./to_roman.php 50
```
5. To run the unit tests:
```
# Standard unit tests:
phpunit --exclude-group large RomanNumeralTest

# Unit tests with large ranges:
phpunit RomanNumeralTest
```
