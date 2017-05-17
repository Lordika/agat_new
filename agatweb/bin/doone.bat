type include\header.tex > %1.tex
type include\answer.tex > ans_%1.tex
echo \SetName{%1} > Name.tex
call bin\%3 %1 %2
call bin\maketex %1
call bin\maketex ans_%1
