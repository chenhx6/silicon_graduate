# -*- coding: utf-8 -*-
path = "raw/writing/gpt/A130/these_2023_template/these_template/Tex/Appendix.tex"

content = r"""%---------------------------------------------------------------------------%
%->> Appendix
%---------------------------------------------------------------------------%
\thispagestyle{appendixheader}
\ctexset{
    chapter = {
        numbering = true,
        number = \Alph{chapter},
        name = {附录~, },
    }
}
\renewcommand{\theequation}{\Alph{chapter}.\arabic{equation}}
\renewcommand{\thefigure}{\Alph{chapter}-\arabic{figure}}
\renewcommand{\thetable}{\Alph{chapter}-\arabic{table}}

\IfFileExists{Tex/Appendices/AppendixA.tex}{%
    \setcounter{chapter}{0}% 保证附录编号为附录 A (0+1=1 -> A)
    \input{Tex/Appendices/AppendixA}%
}{%
    % 暂无附录 A
}

\IfFileExists{Tex/Appendices/AppendixB.tex}{%
    \setcounter{chapter}{1}% 保证附录编号为附录 B (1+1=2 -> B)
    \input{Tex/Appendices/AppendixB}%
}{%
    % 暂无附录 B
}

\IfFileExists{Tex/Appendices/AppendixC.tex}{%
    \setcounter{chapter}{2}% 保证附录编号为附录 C (2+1=3 -> C)
    \input{Tex/Appendices/AppendixC}%
}{%
    % 暂无附录 C
}

\IfFileExists{Tex/Appendices/AppendixE.tex}{%
    \setcounter{chapter}{4}% 保证附录编号为附录 E (4+1=5 -> E, 保持 D 缺位时不顺延)
    \input{Tex/Appendices/AppendixE}%
}{%
    % 暂无附录 E
}

\IfFileExists{Tex/Appendices/AppendixF.tex}{%
    \setcounter{chapter}{5}% 保证附录编号为附录 F (5+1=6 -> F)
    \input{Tex/Appendices/AppendixF}%
}{%
    % 暂无附录 F
}
%---------------------------------------------------------------------------%
"""

with open(path, "w", encoding="utf-8") as f:
    f.write(content.strip() + "\n")

print("Successfully written canonical Appendix.tex")
