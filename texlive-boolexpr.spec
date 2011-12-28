# revision 17830
# category Package
# catalog-ctan /macros/latex/contrib/boolexpr
# catalog-date 2010-04-12 11:39:15 +0200
# catalog-license lppl
# catalog-version 3.14
Name:		texlive-boolexpr
Version:	3.14
Release:	1
Summary:	A boolean expression evaluator and a switch command
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/boolexpr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boolexpr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boolexpr.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boolexpr.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The \boolexpr macro evaluates boolean expressions in a purely
expandable way. \boolexpr{ A \OR B \AND C } expands to 0 if the
logical expression is TRUE. A, B, C may be: - numeric
expressions such as: x=y, x<>y, x>y or x<y; - boolean switches:
\iftrue 0\else 1\fi; - conditionals: \ifcsname
whatsit\endcsname 0\else 1\fi; - another \boolexpr: \boolexpr{
D \OR E \AND F }: \boolexpr may be used with \ifcase:
\ifcase\boolexpr{ A \OR B \AND C } What to do if true \else
What to do if false \fi The \switch command (which is also
expandable) has the form: \switch \case{<boolean expression>}
... \case{<boolean expression>} ... ... \otherwise ...
\endswitch.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/boolexpr/boolexpr.sty
%doc %{_texmfdistdir}/doc/latex/boolexpr/README
%doc %{_texmfdistdir}/doc/latex/boolexpr/boolexpr.pdf
#- source
%doc %{_texmfdistdir}/source/latex/boolexpr/boolexpr.dtx
%doc %{_texmfdistdir}/source/latex/boolexpr/boolexpr.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
