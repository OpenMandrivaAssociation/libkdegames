%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	KDE games library
Name:		libkdegames
Version:	19.04.1
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://games.kde.org/
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
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
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5QuickWidgets)
BuildRequires:	cmake(OpenAL)

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

%files common -f libkdegames5.lang
%{_sysconfdir}/xdg/libkdegames.categories
%{_datadir}/carddecks/
%{_datadir}/kconf_update/kgthemeprovider-migration.upd

#-------------------------------------------------------------------------------

%package corebindings
Summary:	Qml plugins for KDE games
Group:		Graphical desktop/KDE

%description corebindings
Qml plugins for KDE games.

%files corebindings
%{_libdir}/qt5/qml/org/kde/games

#-------------------------------------------------------------------------------

%define KF5KDEGames_major 7
%define libKF5KDEGames %mklibname KF5KDEGames %{KF5KDEGames_major}

%package -n %{libKF5KDEGames}
Summary:	Runtime Library for KDE games
Group:		System/Libraries
Obsoletes:	%{_lib}kdegames4 < 1:4.8.0
Obsoletes:	%{_lib}kdegames5 < 1:4.9.0
Obsoletes:	%{_lib}kggzgames4 < 1:4.8.0
Obsoletes:	%{_lib}kggzmod4 < 1:4.8.0
Obsoletes:	%{_lib}kggznet4 < 1:4.8.0
Obsoletes:	%{mklibname kdegames 6} < %{EVRD}
Obsoletes:	%{mklibname kf5kdegames 6} < 1:5.12.0

%description -n %{libKF5KDEGames}
Runtime Library for KDE games.

%files -n %{libKF5KDEGames}
%{_libdir}/libKF5KDEGames.so.%{KF5KDEGames_major}*

#-------------------------------------------------------------------------------

%define KF5KDEGamesPrivate_major 1
%define libKF5KDEGamesPrivate %mklibname KF5KDEGamesPrivate 1

%package -n %{libKF5KDEGamesPrivate}
Summary:	Runtime Library for KDE games
Group:		System/Libraries
Obsoletes:	%{mklibname kdegamesprivate 1} < %{EVRD}
Obsoletes:	%{mklibname kf5kdegamesprivate 6} < 1:5.12.0

%description -n %{libKF5KDEGamesPrivate}
Runtime Library for KDE games.

%files -n %{libKF5KDEGamesPrivate}
%{_libdir}/libKF5KDEGamesPrivate.so.%{KF5KDEGamesPrivate_major}*

#-------------------------------------------------------------------------------

%define devname %mklibname KF5KDEGames -d

%package -n %{devname}
Summary:	Headers files for KDE games library
Group:		Development/KDE and Qt
Obsoletes:	kdegames4-devel < 1:4.9.80
Requires:	%{libKF5KDEGames} = %{EVRD}
Requires:	%{libKF5KDEGamesPrivate} = %{EVRD}
Obsoletes:	libkdegames-devel < 1:15.12.0-2
Provides:	libkdegames-devel = 1:15.12.0-2

%description -n %{devname}
Headers files needed to build applications based on KDE games library.

%files -n %{devname}
%{_libdir}/cmake/KF5KDEGames
%{_libdir}/libKF5KDEGamesPrivate.so
%{_libdir}/libKF5KDEGames.so
%{_includedir}/*

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libkdegames5
