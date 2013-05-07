Name:		libkdegames
Summary:	KDE games library
Version:	4.10.3
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(sndfile)

%description
This packages provides common code and data for many KDE games.

#-------------------------------------------------------------------------------

%package common
Summary:	Common files needed by KDE games
BuildArch:	noarch
Obsoletes:	kdegames4-core < 1:4.9.80

%description common
This package provides common files needed by KDE games such as carddecks
for KDE cardgames.

%files common
%{_kde_appsdir}/carddecks/
%{_kde_appsdir}/kconf_update/kgthemeprovider-migration.upd

#-------------------------------------------------------------------------------

%define libkdegames_major 6
%define libkdegames %mklibname kdegames %{libkdegames_major}

%package -n %{libkdegames}
Summary:	Runtime Library for KDE games
Group:		System/Libraries
Obsoletes:	%{_lib}kdegames4 < 1:4.8.0
Obsoletes:	%{_lib}kdegames5 < 1:4.9.0
Obsoletes:	%{_lib}kggzgames4 < 1:4.8.0
Obsoletes:	%{_lib}kggzmod4 < 1:4.8.0
Obsoletes:	%{_lib}kggznet4 < 1:4.8.0

%description -n %{libkdegames}
Runtime Library for KDE games.

%files -n %{libkdegames}
%{_kde_libdir}/libkdegames.so.%{libkdegames_major}*

#-------------------------------------------------------------------------------

%define libkdegamesprivate_major 1
%define libkdegamesprivate %mklibname kdegamesprivate 1

%package -n %{libkdegamesprivate}
Summary:	Runtime Library for KDE games
Group:		System/Libraries

%description -n %{libkdegamesprivate}
Runtime Library for KDE games.

%files -n %{libkdegamesprivate}
%{_kde_libdir}/libkdegamesprivate.so.%{libkdegamesprivate_major}*

#-------------------------------------------------------------------------------

%package devel
Summary:	Headers files for KDE games library
Group:		Development/KDE and Qt
Requires:	kdelibs4-devel
Obsoletes:	kdegames4-devel < 1:4.9.80
Provides:	kdegames4-devel = %{EVRD}
Requires:	%{libkdegames} = %{EVRD}
Requires:	%{libkdegamesprivate} = %{EVRD}

%description devel
Headers files needed to build applications based on KDE games library.

%files devel
%{_kde_libdir}/cmake/KDEGames/*.cmake
%{_kde_libdir}/libkdegamesprivate.so
%{_kde_libdir}/libkdegames.so
%{_kde_includedir}/*

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

