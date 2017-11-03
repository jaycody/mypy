<?php

require_once 'DayTrader.php';

class DayTraderTest extends PHPUnit_Framework_TestCase
{
    /**
    * @dataProvider validPricesProvider
    * @group standard
    */
    public function testValidPrices(array $prices, array $expected)
    {
        $this->assertSame($expected, 
            (new DayTrader($prices))->calcBestTrade());
    }

    public function validPricesProvider()
    {
        $large = range(11.00, 19.00, 0.01);
        $large[0] = 30.00;
        $large[4] = 10.00;
        $large[7] = 20.00;

        return [
            [[1.00, 2.00, 3.00, 4.00, 5.00], [1.00, 5.00]],
            [[2.00, 3.00, 1.00, 4.00, 5.00], [1.00, 5.00]],
            [[2.00, 3.00, 4.00, 1.00, 5.00], [2.00, 5.00]],
            [[1.00, 5.00, 2.00, 4.00, 3.00], [1.00, 4.00]],
            [[5.00, 1.00, 2.00, 3.00, 4.00], [1.00, 4.00]],
            [[19.35, 19.30, 18.88, 18.93, 18.95, 19.03, 19.00, 18.97, 18.97, 18.98], [18.88, 19.03]],
            [[9.20, 8.03, 10.02, 8.08, 8.14, 8.10, 8.31, 8.28, 8.35, 8.34, 8.39, 8.45, 8.38, 8.38, 8.32, 8.36, 8.28, 8.28, 8.38, 8.48, 8.49, 8.54, 8.73, 8.72, 8.76, 8.74, 8.87, 8.82, 8.81, 8.82, 8.85, 8.85, 8.86, 8.63, 8.70, 8.68, 8.72, 8.77, 8.69, 8.65, 8.70, 8.98, 8.98, 8.87, 8.71, 9.17, 9.34, 9.28, 8.98, 9.02, 9.16, 9.15, 9.07, 9.14, 9.13, 9.10, 9.16, 9.06, 9.10, 9.15, 9.11, 8.72, 8.86, 8.83, 8.70, 8.69, 8.73, 8.73, 8.67, 8.70, 8.69, 8.81, 8.82, 8.83, 8.91, 8.80, 8.97, 8.86, 8.81, 8.87, 8.82, 8.78, 8.82, 8.77, 8.54, 8.32, 8.33, 8.32, 8.51, 8.53, 8.52, 8.41, 8.55, 8.31, 8.38, 8.34, 8.34, 8.19, 8.17, 8.16], [8.03, 9.34]],
            [[1.00, 1.00, 1.00, 0.99, 0.99, 0.99], []],
            [[1.00, 1.00, 1.00, 1.00, 1.00, 1.00], []],
            [[1.00, 1.00, 0.99, 0.99, 0.99], []],
            [$large, [10.00, 20.00]],
        ];
    }

    /**
    * @dataProvider multipleValidPricesProvider
    * @group standard
    */
    public function testMultipleValidPrices(array $prices, array $expected)
    {
        $this->assertContains((new DayTrader($prices))->calcBestTrade(), $expected);
    }

    public function multipleValidPricesProvider()
    {
        return [
            [[11.00, 12.00, 13.00, 4.00, 5.00, 6.00], [[11.00, 13.00], [4.00, 6.00]]],
            [[31.01, 31.03, 31.63, 31.44, 31.47, 25.55, 25.56, 25.55, 25.53, 25.50, 25.66, 19.35, 19.30, 18.88, 18.93, 18.95, 19.03, 19.00, 18.97, 18.97, 18.98], [[31.01, 31.63], [25.53, 25.66], [18.88, 19.03]]],
        ];
    }

    /**
    * @dataProvider validPricesLargeSetProvider
    * @group large
    */
    public function testValidLargeSetPrices(array $prices, array $expected)
    {
        $this->assertSame($expected, 
            (new DayTrader($prices))->calcBestTrade());
    }

    public function validPricesLargeSetProvider()
    {
        $large1 = range(11.00, 19.00, 0.01);
        $large2 = $large1;

        $large1[0] = 30.00;
        $large1[4] = 10.00;
        $large1[7] = 20.00;

        shuffle($large2);
        $large2[0] = 30.00;
        $large2[4] = 10.00;
        $large2[7] = 20.00;

        $large3 = range(100.00, 1.00, -0.01);
        $large3[1] = 0.01;
        $large3[] = 111.11;

        $large4 = range(100.02, 1.00, -0.01);
        $large4[0] = 0.01;
        $large4[1] = 111.11;

        return [
            [$large1, [10.00, 20.00]],
            [$large2, [10.00, 20.00]],
            [$large3, [0.01, 111.11]],
            [$large4, [0.01, 100.00]],
            [range(30.00, 10.00, -0.01), []],
            [range(100.00, 0.00, -0.01), []],
        ];
    }

//    /**
//    * @dataProvider invalidNumberProvider
//    * @expectedException InvalidArgumentException
//    */
//    public function testInvalidNumbers($num)
//    {
//        (new NumberTheory())->numberType($num);
//    }
//
//    public function invalidNumberProvider()
//    {
//        return [
//            [0],
//            [-1],
//            [123.45],
//            ['1abc'],
//            ['bad value'],
//        ];
//    }

}
