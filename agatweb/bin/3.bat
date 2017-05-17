echo \MultiInvertMatrix[5%2]{5}{2} > %1_invert_2x2_.tex
echo \relax > %1_invert_3x3_.tex
echo \MultiSolveInvertMatrix[5%2]{10}{2}{O} > ans_%1_invert_2x2_.tex
echo \relax > ans_%1_invert_3x3_.tex
bin\invertmatr 3 5 %1
bin\invertmatr 4 5 %1
bin\invertsystem 2 5 %1