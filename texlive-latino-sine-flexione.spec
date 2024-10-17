Name:		texlive-latino-sine-flexione
Version:	69568
Release:	1
Summary:	LaTeX support for documents written in Peano's Interlingua
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/latino-sine-flexione
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latino-sine-flexione.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latino-sine-flexione.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Latino sine Flexione (or Interlingua) is a language constructed
by Giuseppe Peano at the beginning of the last century. This
simplified Latin is designed to be an instrument for
international cooperation, especially in the academic sphere.
(Note that this "Interlingua" is different from the
"Interlingua" that was created a few decades after Peano's work
and which is supported by babel-interlingua!) This package
provides the necessary translations to use the language within
a LaTeX document. It also imports fontenc in order to be able
to use ligatures and quotation marks. Finally, it offers a text
in Interlingua that can be used as a dummy text: Fundamento de
intelligentia. This article by H. Bijlsma was first published
in Schola et Vita Anno I (1926).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/latino-sine-flexione
%doc %{_texmfdistdir}/doc/latex/latino-sine-flexione

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
