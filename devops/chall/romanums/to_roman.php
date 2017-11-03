#!/usr/bin/php
<?php

require_once 'RomanNumeral.php';

if ($argc !== 2 || !ctype_digit($argv[1])) {
    die('Missing or invalid number' . PHP_EOL); 
}

$number = (int) $argv[1];

$roman = (new RomanNumeral())->toRoman($number);
//echo $roman . PHP_EOL;
