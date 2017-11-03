# Stock Market Wizard...with perfect hindsight
> HCI Programming Challenge 3/21/2016 - thx tim!

## Description
In this exercise we're playing the stock market. We'll be day trading, so we want to get in and out of a stock before the day is done. The goal is to time our trades so that we make the biggest gain possible -- buy low, sell high.

Given a list of stock price ticks for the day, figure out what trades we should make to maximize our gain within the constraints of the market. The market has a rule that won't let you buy and sell in a pair of ticks - you have to wait for at least one tick to go by before you can sell. And obviously you can't buy in the future and sell in the past. We're only interested in making money, so if a stock purchase would not net a profit for the day then we won't buy it.

### Input
You'll be given an array of stock prices containing floats (dollars and cents), listed in chronological order.


### Output
- Your function should return an array containing the buy and sell price. For example:
```
[1.00, 2.00]
```
- If multiple trades exist with the same maximum profit you can return any one of them (but only one).
- If a stock purchase would not net a profit for the day then you should return an empty array to indicate it shouldn't be bought.


### Sample I/O
```
Input: [1.00, 2.00, 3.00, 4.00, 5.00]
Return: [1.00, 5.00]
```
```
Input: [19.35, 19.30, 18.88, 18.93, 18.95, 19.03, 19.00, 18.97, 18.97, 18.98]
Return: [18.88, 19.03]
```
```
Input: [9.20, 8.03, 10.02, 8.08, 8.14, 8.10, 8.31, 8.28, 8.35, 8.34, 8.39, 8.45, 8.38, 8.38, 8.32, 8.36, 8.28, 8.28, 8.38, 8.48, 8.49, 8.54, 8.73, 8.72, 8.76, 8.74, 8.87, 8.82, 8.81, 8.82, 8.85, 8.85, 8.86, 8.63, 8.70, 8.68, 8.72, 8.77, 8.69, 8.65, 8.70, 8.98, 8.98, 8.87, 8.71, 9.17, 9.34, 9.28, 8.98, 9.02, 9.16, 9.15, 9.07, 9.14, 9.13, 9.10, 9.16, 9.06, 9.10, 9.15, 9.11, 8.72, 8.86, 8.83, 8.70, 8.69, 8.73, 8.73, 8.67, 8.70, 8.69, 8.81, 8.82, 8.83, 8.91, 8.80, 8.97, 8.86, 8.81, 8.87, 8.82, 8.78, 8.82, 8.77, 8.54, 8.32, 8.33, 8.32, 8.51, 8.53, 8.52, 8.41, 8.55, 8.31, 8.38, 8.34, 8.34, 8.19, 8.17, 8.16]
Return: [8.03, 9.34]
```

```
Input: [11.00, 12.00, 13.00, 4.00, 5.00, 6.00]
Return: [11.00, 13.00] OR [4.00, 6.00]
```



## Instructions
1. Copy all files from hci's challenge code dir to your own directory
2. From your dir, open the file DayTrader.php
3. The constructor should accept an array of stock prices (floats) that are in chronological order
4. The calcBestTrade() method should return an array containing the buy & sell price, or an empty array if a profit cannot be made on the stock
5. To run the program:
./makemoney.php "price1, price2, price3, …"
For example:
./makemoney.php "1.00, 2.00, 3.00, 4.00, 5.00"
6. To run the unit tests:
```
# Standard data set:
phpunit --group standard  DayTraderTest

# Large data set:
phpunit --group large DayTraderTest

# All data sets:
phpunit DayTraderTest
```
