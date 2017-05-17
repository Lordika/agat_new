bin\eigen_values e 3 10 8 %1 
bin\eigen_values k 3 15 9 %1 
rem %bindir%\eigen_values i 3 5 10 %1  
echo \MultiQuadSimple[60%2]{15} > %1_quad_simple.tex
echo \MultiSolveQuadSimple[60%2]{15}{O} > ans_%1_quad_simple.tex
