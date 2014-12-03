<?php

$string = '{Please|Just} make this {cool|awesome|random} test sentence {rotate {quickly|fast} 
	and random|spin and be random}';

function stringShuffle($str){

	$pattern = '/{([^{]+)}/U';
	$randWords = array();

	preg_match_all($pattern, $str, $matches);

	if (empty($matches[0])){
		return $str;
	}

	$randWords = explode('|', substr($matches[0][0], 1, -1));

	shuffle($randWords);

	$shuffleString = str_replace($matches[0][0], $randWords[0], $str);

	return stringShuffle($shuffleString);
}

echo stringShuffle($string);
