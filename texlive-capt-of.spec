# revision 16813
# category Package
# catalog-ctan /macros/latex/contrib/capt-of
# catalog-date 2010-01-27 23:13:46 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-capt-of
Version:	20100127
Release:	3
Summary:	Captions on more than floats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/capt-of
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/capt-of.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/capt-of.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/capt-of.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100127-2
+ Revision: 749974
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100127-1
+ Revision: 718006
- texlive-capt-of
- texlive-capt-of
- texlive-capt-of
- texlive-capt-of
- texlive-capt-of

