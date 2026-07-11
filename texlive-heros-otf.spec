%global tl_name heros-otf
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.01
Release:	%{tl_revision}.1
Summary:	Using the OpenType fonts TeX Gyre Heros>
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/heros-otf
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/heros-otf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/heros-otf.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package can only be used with LuaLaTeX or XeLaTeX. It does the font
setting for the OpenType font 'TeX Gyre Heros'. The condensed versions
of the fonts are also supported. The missing typefaces for slanted text
are also defined.

