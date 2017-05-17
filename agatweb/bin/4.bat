bin\system 3 5 %1
bin\system 4 5 %1
bin\system 5 5 %1
rem echo \relax > %1_system_3x3_K.tex
echo \MultiKramer[1%2]{5} > %1_system_3x3_K.tex
echo \MultiInvertSystem[2%2]{5} > %1_system_3x3_I.tex
echo \MultiSolveKramer[3%2]{5}{O} > ans_%1_system_3x3_K.tex
echo \MultiSolveInvertSystem[4%2]{5}{O} > ans_%1_system_3x3_I.tex
