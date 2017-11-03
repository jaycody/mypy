# Ordered Words
> HCI Programming Challenge 8/1/2017 - thx tim!
________________

## Description
- The standard telephone keypad correlates letters to numbers as follows:

```
1 ->
2 -> ABC
3 -> DEF
4 -> GHI
5 -> JKL
6 -> MNO
7 -> PQRS
8 -> TUV
9 -> WXYZ
0 ->
```

- A given input word is defined to be an Ordered Word if, when translated to keypad presses using the above, the resulting number is either non-decreasing or non-increasing.
- In other words, the resultant number cannot both increase and decrease.
- For example, the word CAT translates to 228, which is non-decreasing, and thus an Ordered Word.
- However, the word DOG is 364, which both increases and decreases, and thus is not an Ordered Word.

## Challenge
Given a word, output whether or not it's Ordered.

## Input
- A word (not necessarily a dictionary word) consisting of ASCII alphabet ([A-Z] or [a-z]) letters only
- The word will be at least 2 characters in length.

## Output
- Return true if the input word is ordered or false if it is not ordered.
- Examples
- Here are some ordered words

```
CAT
TAC
AAA
DEMONS
SKID
LKJONMSRQP
ABCDEFGHIJKLMNOPQRSTUVWXYZ
Here are some non-ordered words
DOG
ROSE
COFFEE
JKLMNOGHI
```

## Instructions
1. Copy all files from HCI's code challenge repo to your own directory
2. From your dir, open the file OrderedWord.php
3. The isOrdered() method should return a boolean indicating whether the word is ordered
4. To run the program, pass in a word:
```
./is_ordered.php cat
```
5. To run the unit tests:
```
phpunit OrderedWordTest
```
