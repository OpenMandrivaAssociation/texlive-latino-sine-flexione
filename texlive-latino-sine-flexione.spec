%global tl_name latino-sine-flexione
%global tl_revision 69568

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	LaTeX support for documents written in Peanos Interlingua
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/latino-sine-flexione
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latino-sine-flexione.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latino-sine-flexione.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Latino sine Flexione (or Interlingua) is a language constructed by
Giuseppe Peano at the beginning of the last century. This simplified
Latin is designed to be an instrument for international cooperation,
especially in the academic sphere. (Note that this "Interlingua" is
different from the "Interlingua" that was created a few decades after
Peano's work and which is supported by babel-interlingua!) This package
provides the necessary translations to use the language within a LaTeX
document. It also imports fontenc in order to be able to use ligatures
and quotation marks. Finally, it offers a text in Interlingua that can
be used as a dummy text: Fundamento de intelligentia. This article by H.
Bijlsma was first published in Schola et Vita Anno I (1926).

