#!/usr/bin/php
<?php

require_once 'Grid.php';

if (!isset($argv[1])) { 
    die('Missing input parameter' . PHP_EOL); 
}

$arrangement = preg_split('/[\s,]+/', $argv[1]);
$arrangement = array_map('intval', $arrangement);
$grid = new Grid($arrangement);

$outcome = $grid->isMagicSquare();
assert(is_bool($outcome), 'The isMagicSquare() method must return a boolean');

if ($outcome) {
    echo "This IS a magic square." . PHP_EOL;
} else {
    echo "This IS NOT a magic square." . PHP_EOL;
}
