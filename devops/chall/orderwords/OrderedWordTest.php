<?php

require_once 'OrderedWord.php';

class OrderedWordTest extends PHPUnit_Framework_TestCase
{
    /**
     * @dataProvider orderedWordProvider
     * @group standard
     */
    public function testOrderedWords($word)
    {
        $this->assertSame(true, (new OrderedWord())->isOrdered($word));
    }

    public function orderedWordProvider()
    {
        return [
            ['cat'],
            ['CAT'],
            ['TAC'],
            ['AAA'],
            ['DEMONS'],
            ['SKID'],
            ['LKJONMSRQP'],
            ['ABCDEFGHIJKLMNOPQRSTUVWXYZ'],
            ['ZYXWVUTSRQPONMLKJIHGFEDCBA'],
            ['AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ'],
            ['ZZYYXXWWVVUUTTSSRRQQPPOONNMMLLKKJJIIHHGGFFEEDDCCBBAA'],
            ['abcabcdefdefghighijkljklmnomnopqrspqrstuvtuvwxyzwxyz'],
            ['zyxwzyxwvutvutsrqpsrqponmonmlkjlkjihgihgfedfedcbacba'],
        ];
    }

    /**
     * @dataProvider unorderedWordProvider
     * @group standard
     */
    public function testUnorderedWords($word)
    {
        $this->assertSame(false, (new OrderedWord())->isOrdered($word));
    }

    public function unorderedWordProvider()
    {
        return [
            ['DOG'],
            ['rose'],
            ['coffee'],
            ['JKLMNOGHI'],
            ['abcabcdefdefghighijkljklmnomnopqrspqrstuvtuvwxyzwxyza'],
            ['zabcabcdefdefghighijkljklmnomnopqrspqrstuvtuvwxyzwxyza'],
            ['abcdc'],
        ];
    }
}
