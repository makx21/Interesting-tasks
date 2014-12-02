<?php

function depth(array $a){

    $depth = -1;

    $q = -1;
    $r = -1;
    $p = 0;

    $arrayCount = count($a);

    for ($i = 1; $i < $arrayCount; $i++){
        if ($q < 0 && $a[$i] >= $a[$i-1]) {
            $q = $i - 1;
        }    

        if (($q >= 0 && $r < 0) && ($a[$i] <= $a[$i-1] || $i + 1 == $arrayCount))
        {
            $r = $i - 1;
            $depth = max($depth, min($a[$p] - $a[$q], $a[$r] - $a[$q]));

            $p = $i - 1;
            $q = -1;
            $r = -1;
        }
    }

    return $depth;
}
