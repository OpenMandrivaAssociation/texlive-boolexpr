%global tl_name boolexpr
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.14
Release:	%{tl_revision}.1
Summary:	A boolean expression evaluator and a switch command
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/boolexpr
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/boolexpr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/boolexpr.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/boolexpr.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The \boolexpr macro evaluates boolean expressions in a purely expandable
way. \boolexpr{ A \OR B \AND C } expands to 0 if the logical expression
is TRUE. A, B, C may be: numeric expressions such as: x=y, x<>y, x>y or
x<y; - boolean switches: \iftrue 0\else 1\fi; - conditionals: \ifcsname
whatsit\endcsname 0\else 1\fi; - another \boolexpr: \boolexpr{ D \OR E
\AND F }: \boolexpr may be used with \ifcase: \ifcase\boolexpr{ A \OR B
\AND C } What to do if true \else What to do if false \fi The \switch
command (which is also expandable) has the form: \switch \case{<boolean
expression>} ... \case{<boolean expression>} ... ... \otherwise ...
\endswitch

