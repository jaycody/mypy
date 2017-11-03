#!/usr/bin/php
<?php

require_once 'KaprekarNumbers.php';

if ($argc !== 3 || !ctype_digit($argv[1]) || !ctype_digit($argv[2])) { 
    die('Missing or invalid input parameter for the start or end of range' . PHP_EOL); 
}

$start = (int) $argv[1];
$end = (int) $argv[2];

$kaprekars = (new KaprekarNumbers())->calculate($start, $end);

echo "The Kaprekar numbers in the range ({$start}...{$end} are:" . PHP_EOL
    . (empty($kaprekars) ? 'None' : join(', ', $kaprekars)) . PHP_EOL;

