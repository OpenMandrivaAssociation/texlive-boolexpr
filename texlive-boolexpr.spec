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
Requires(pre):	texlive-tlpkg
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

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/boolexpr
%dir %{_datadir}/texmf-dist/source/latex/boolexpr
%dir %{_datadir}/texmf-dist/tex/latex/boolexpr
%doc %{_datadir}/texmf-dist/doc/latex/boolexpr/README
%doc %{_datadir}/texmf-dist/doc/latex/boolexpr/boolexpr.pdf
%doc %{_datadir}/texmf-dist/source/latex/boolexpr/boolexpr.dtx
%doc %{_datadir}/texmf-dist/source/latex/boolexpr/boolexpr.ins
%{_datadir}/texmf-dist/tex/latex/boolexpr/boolexpr.sty
