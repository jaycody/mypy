#!/usr/bin/php
<?php

require_once 'OrderedWord.php';

if ($argc !== 2 || !ctype_alpha($argv[1])) {
    die('Missing or invalid word' . PHP_EOL); 
}

$word = $argv[1];
$isOrdered = (new OrderedWord())->isOrdered($word);
echo 'Word ' . ($isOrdered ? 'is' : 'is not') . ' ordered' . PHP_EOL;
