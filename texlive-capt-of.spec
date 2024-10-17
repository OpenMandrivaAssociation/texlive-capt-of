Name:		texlive-capt-of
Version:	29803
Release:	2
Summary:	Captions on more than floats
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/capt-of
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/capt-of.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/capt-of.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/capt-of.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Defines a command \captionof for putting a caption to something
that's not a float. Note that the caption package includes a
\captionof command that is an extension of that provided by
this package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/capt-of/capt-of.sty
%doc %{_texmfdistdir}/doc/latex/capt-of/README
%doc %{_texmfdistdir}/doc/latex/capt-of/capt-of.pdf
#- source
%doc %{_texmfdistdir}/source/latex/capt-of/capt-of.dtx
%doc %{_texmfdistdir}/source/latex/capt-of/capt-of.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
