<?php

require_once 'KaprekarNumbers.php';

class KaprekarNumbersTest extends PHPUnit_Framework_TestCase
{
    /**
     * @dataProvider kaprekarNumberProvider
     * @group standard
     */
    public function testKaprekarNumbers($start, $end, $expected)
    {
        $this->assertSame($expected, 
            (new KaprekarNumbers())->calculate($start, $end));
    }

    public function kaprekarNumberProvider()
    {
        return [
            [1, 5, []],
            [2, 8, []],
            [2, 2, []],
            [2, 10, [9]],
            [9, 9, [9]],
            [5, 50, [9, 45]],
            [2, 99, [9, 45, 55, 99]],
            [100, 1000, [297, 703, 999]],
            [1001, 1999, []],
        ];
    }

    /**
     * @dataProvider largeKaprekarNumberProvider
     * @group large
     */
    public function testLargeKaprekarNumbers($start, $end, $expected)
    {
        $this->assertSame($expected, 
            (new KaprekarNumbers())->calculate($start, $end));
    }

    public function largeKaprekarNumberProvider()
    {
        return [
            [1001, 99999, [2223, 2728, 4879, 4950, 5050, 5292, 7272, 7777, 9999, 17344, 22222, 38962, 77778, 82656, 95121, 99999]],
            [500000, 600000, [500500, 533170, 538461]],
            [1, 1000000, [9, 45, 55, 99, 297, 703, 999, 2223, 2728, 4879, 4950, 5050, 5292, 7272, 7777, 9999, 17344, 22222, 38962, 
                          77778, 82656, 95121, 99999, 142857, 148149, 181819, 187110, 208495, 318682, 329967, 351352, 356643, 390313, 
                          461539, 466830, 499500, 500500, 533170, 538461, 609687, 627615, 643357, 648648, 670033, 681318, 791505, 
                          812890, 818181, 851851, 857143, 961038, 994708, 999999]],
        ];
    }

}
