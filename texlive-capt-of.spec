Name:		texlive-capt-of
Version:	20100127
Release:	1
Summary:	Captions on more than floats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/capt-of
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/capt-of.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/capt-of.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/capt-of.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Defines a command \captionof for putting a caption to something
that's not a float. Note that the caption package includes a
\captionof command that is an extension of that provided by
this package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
