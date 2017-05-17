rem latex %1.tex
rem latex %1.tex
rem dvips %1.dvi -o %1.ps
rem ps2pdf %1.ps
pdflatex -halt-on-error %1.tex
pdflatex -halt-on-error %1.tex