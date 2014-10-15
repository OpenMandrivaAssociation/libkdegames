Summary:	KDE games library
Name:		libkdegames
Version:	4.14.2
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://games.kde.org/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(sndfile)

%description
This packages provides common code and data for many KDE games.

#-------------------------------------------------------------------------------

%package common
Summary:	Common files needed by KDE games
Group:		Graphical desktop/KDE
BuildArch:	noarch
Obsoletes:	kdegames4-core < 1:4.9.80

%description common
This package provides common files needed by KDE games such as carddecks
for KDE cardgames.

%files common
%{_kde_appsdir}/carddecks/
%{_kde_appsdir}/kconf_update/kgthemeprovider-migration.upd

#-------------------------------------------------------------------------------

%package corebindings
Summary:	Qml plugins for KDE games
Group:		Graphical desktop/KDE

%description corebindings
Qml plugins for KDE games.

%files corebindings
%{_kde_libdir}/kde4/imports/org/kde/games/core/KgItem.qml
%{_kde_libdir}/kde4/imports/org/kde/games/core/libcorebindingsplugin.so
%{_kde_libdir}/kde4/imports/org/kde/games/core/qmldir

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
* Wed Oct 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.2-1
- New version 4.14.2

* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.1-1
- New version 4.14.1

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.2-1
- New version 4.13.2

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- New version 4.11.0
- New subpackage corebindings

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

