#
# Conditional build:
%bcond_with	python23	# build for python 2.3, not 2.4

Summary:	Photo collection manager and viewer with content-based query
Summary(pl):	Zarz±dca oraz przegl±darka kolekcji zdjêæ
Name:		imgSeek
Version:	0.8.4
Release:	2
License:	GPL v2
Group:		Applications/Graphics/X11
Vendor:		Ricardo Niederberger Cabral <nieder@mail.ru>
Source0:	http://dl.sourceforge.net/imgseek/%{name}-%{version}.tar.bz2
# Source0-md5:	6b79e7e7e588fa9afa71240d5c2d0b52
Source1:	%{name}.desktop
Patch0:		%{name}-settings.patch
Patch1:		%{name}-lib64.patch
URL:		http://imgseek.sourceforge.net/
BuildRequires:	python-Imaging-devel
BuildRequires:	python-PyQt >= 3.5
BuildRequires:	python-devel >= 2.2.0
BuildRequires:	python-modules >= 2.2.0
BuildRequires:	qt-devel >= 3.0.0
BuildRequires:	rpmbuild(macros) >= 1.174
BuildRequires:	sed >= 4.0
Requires:	python-Imaging
Requires:	python-PyQt >= 3.5
%pyrequires_eq	python-libs
Requires:	python-modules >= 2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
imgSeek is a photo collection manager and viewer with content-based
search and many other features. The query is expressed either as a
rough sketch painted by the user or as another image you supply (or an
image in your collection).

%description -l pl
imgSeek jest zarz±dc± i przegl±dark± kolekcji zdjêæ z opart± na
zawarto¶ci wyszukiwark± oraz wieloma innymi funkcjami. Wyboru mo¿na
dokonywaæ zarówno przy pomocy narysowanego przez u¿ytkownika kursorem
kszta³tu jak i w tradycyjny sposób.

%package devel
Summary:	Source files of imgSeek
Summary(pl):	Pliki ¼ród³owe imgSeek
Group:		Development/Languages/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}
%pyrequires_eq	python-libs

%description devel
Python source files provided with imgSeek. They pull together the GUI
of whole application.

%description devel -l pl
Pliki ¼ród³owe pythona dostarczane z imgSeek. Sk³adaj± siê one na GUI
ca³ej aplikacji.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%if %{without python23}
sed -i 's/python2\.3/python2.4/' setup.py
%endif

%build
QTDIR=%{_prefix} %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__python} setup.py install --root=$RPM_BUILD_ROOT
install imgSeek.png $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%dir %{py_sitedir}/imgSeekLib
%{py_sitedir}/imgSeekLib/*.pyc
%attr(755,root,root) %{py_sitedir}/imgSeekLib/*.so
%{_desktopdir}/*
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%{py_sitedir}/imgSeekLib/*.py
