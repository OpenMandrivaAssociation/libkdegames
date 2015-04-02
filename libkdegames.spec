%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	KDE games library
Name:		libkdegames
Version:	15.03.97
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://games.kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(openal)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DNSSD)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5GlobalAccel)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	cmake
BuildRequires:	ninja

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
%{_datadir}/carddecks/
%{_datadir}/kconf_update/kgthemeprovider-migration.upd

#-------------------------------------------------------------------------------

%package corebindings
Summary:	Qml plugins for KDE games
Group:		Graphical desktop/KDE

%description corebindings
Qml plugins for KDE games.

%files corebindings
%{_libdir}/qml/org/kde/games

#-------------------------------------------------------------------------------

%define libkdegames_major 6
%define libkdegames %mklibname kf5kdegames %{libkdegames_major}

%package -n %{libkdegames}
Summary:	Runtime Library for KDE games
Group:		System/Libraries
Obsoletes:	%{_lib}kdegames4 < 1:4.8.0
Obsoletes:	%{_lib}kdegames5 < 1:4.9.0
Obsoletes:	%{_lib}kggzgames4 < 1:4.8.0
Obsoletes:	%{_lib}kggzmod4 < 1:4.8.0
Obsoletes:	%{_lib}kggznet4 < 1:4.8.0
Obsoletes:	%{mklibname kdegames 6} < %{EVRD}

%description -n %{libkdegames}
Runtime Library for KDE games.

%files -n %{libkdegames}
%{_kde_libdir}/libKF5KDEGames.so.%{libkdegames_major}*

#-------------------------------------------------------------------------------

%define libkdegamesprivate_major 1
%define libkdegamesprivate %mklibname kf5kdegamesprivate 1

%package -n %{libkdegamesprivate}
Summary:	Runtime Library for KDE games
Group:		System/Libraries
Obsoletes:	%{mklibname kdegamesprivate 1} < %{EVRD}

%description -n %{libkdegamesprivate}
Runtime Library for KDE games.

%files -n %{libkdegamesprivate}
%{_libdir}/libKF5KDEGamesPrivate.so.%{libkdegamesprivate_major}*

#-------------------------------------------------------------------------------

%package devel
Summary:	Headers files for KDE games library
Group:		Development/KDE and Qt
Obsoletes:	kdegames4-devel < 1:4.9.80
Requires:	%{libkdegames} = %{EVRD}
Requires:	%{libkdegamesprivate} = %{EVRD}

%description devel
Headers files needed to build applications based on KDE games library.

%files devel
%{_libdir}/cmake/KF5KDEGames
%{_libdir}/libKF5KDEGamesPrivate.so
%{_libdir}/libKF5KDEGames.so
%{_includedir}/*

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake -G Ninja
ninja

%install
DESTDIR="%buildroot" ninja -C build install
