bin\eigen_values e 3 10 1 %1 
bin\eigen_values e 3 10 2 %1 
bin\eigen_values e 3 5 3 %1  
bin\eigen_values e 2 5 6 %1
bin\eigen_values e 2 5 7 %1
bin\eigen_values e 2 5 8 %1

rem echo \MultiJordanOne[51%2]{10} > %1_jordan_ex01.tex
rem echo \MultiJordanTwo[52%2]{10} > %1_jordan_ex02.tex
rem echo \MultiJordanThree[53%2]{5} > %1_jordan_ex03.tex
echo \MultiJordanFour[54%2]{5} > %1_jordan_ex04.tex
echo \MultiJordanFive[55%2]{5} > %1_jordan_ex05.tex
rem echo \MultiJordanSix[56%2]{5} > %1_jordan_ex06.tex
rem echo \MultiJordanSeven[57%2]{5} > %1_jordan_ex07.tex
rem echo \MultiJordanEight[58%2]{5} > %1_jordan_ex08.tex
rem echo \MultiSolveJordanOne[51%2]{10}{O} > ans_%1_jordan_ex01.tex
rem echo \MultiSolveJordanTwo[52%2]{10}{O} > ans_%1_jordan_ex02.tex
rem echo \MultiSolveJordanThree[53%2]{5}{O} > ans_%1_jordan_ex03.tex
echo \MultiSolveJordanFour[54%2]{5}{O} > ans_%1_jordan_ex04.tex
echo \MultiSolveJordanFive[55%2]{5}{O} > ans_%1_jordan_ex05.tex
rem echo \MultiSolveJordanSix[56%2]{5}{O} > ans_%1_jordan_ex06.tex
rem echo \MultiSolveJordanSeven[57%2]{5}{O} > ans_%1_jordan_ex07.tex
rem echo \MultiSolveJordanEight[58%2]{5}{O} > ans_%1_jordan_ex08.tex
