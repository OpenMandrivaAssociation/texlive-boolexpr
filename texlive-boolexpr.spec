Name:		texlive-boolexpr
Version:	17830
Release:	2
Summary:	A boolean expression evaluator and a switch command
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/boolexpr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boolexpr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boolexpr.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boolexpr.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
