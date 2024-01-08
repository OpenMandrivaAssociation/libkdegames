%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	KDE games library
Name:		plasma6-libkdegames
Version:	24.01.85
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://games.kde.org/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/libkdegames-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(openal)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6Codecs)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DNSSD)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6GlobalAccel)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6Bookmarks)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6KDELibs4Support)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickWidgets)
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

%files common -f libkdegames6.lang
%{_datadir}/qlogging-categories6/libkdegames.categories
%{_datadir}/carddecks/
%{_datadir}/kconf_update/kgthemeprovider-migration.upd

#-------------------------------------------------------------------------------

%package corebindings
Summary:	Qml plugins for KDE games
Group:		Graphical desktop/KDE

%description corebindings
Qml plugins for KDE games.

%files corebindings
%{_libdir}/qt6/qml/org/kde/games

#-------------------------------------------------------------------------------

%define KF6KDEGames_major 7
%define libKF6KDEGames %mklibname KF6KDEGames %{KF6KDEGames_major}

%package -n %{libKF6KDEGames}
Summary:	Runtime Library for KDE games
Group:		System/Libraries
Obsoletes:	%{_lib}kdegames4 < 1:4.8.0
Obsoletes:	%{_lib}kdegames6 < 1:4.9.0
Obsoletes:	%{_lib}kggzgames4 < 1:4.8.0
Obsoletes:	%{_lib}kggzmod4 < 1:4.8.0
Obsoletes:	%{_lib}kggznet4 < 1:4.8.0
Obsoletes:	%{mklibname kdegames 6} < %{EVRD}
Obsoletes:	%{mklibname kf6kdegames 6} < 1:6.12.0

%description -n %{libKF6KDEGames}
Runtime Library for KDE games.

%files -n %{libKF6KDEGames}
%{_libdir}/libKF6KDEGames.so.%{KF6KDEGames_major}*

#-------------------------------------------------------------------------------

%define KF6KDEGamesPrivate_major 7
%define libKF6KDEGamesPrivate %mklibname KF6KDEGamesPrivate %{KF6KDEGamesPrivate_major}

%package -n %{libKF6KDEGamesPrivate}
Summary:	Runtime Library for KDE games
Group:		System/Libraries
Obsoletes:	%{mklibname kdegamesprivate 1} < %{EVRD}
Obsoletes:	%{mklibname kf6kdegamesprivate 6} < 1:6.12.0

%description -n %{libKF6KDEGamesPrivate}
Runtime Library for KDE games.

%files -n %{libKF6KDEGamesPrivate}
%{_libdir}/libKF6KDEGamesPrivate.so.%{KF6KDEGamesPrivate_major}*

#-------------------------------------------------------------------------------

%define devname %mklibname KF6KDEGames -d

%package -n %{devname}
Summary:	Headers files for KDE games library
Group:		Development/KDE and Qt
Obsoletes:	kdegames4-devel < 1:4.9.80
Requires:	%{libKF6KDEGames} = %{EVRD}
Requires:	%{libKF6KDEGamesPrivate} = %{EVRD}
Obsoletes:	libkdegames-devel < 1:16.12.0-2
Provides:	libkdegames-devel = 1:16.12.0-2

%description -n %{devname}
Headers files needed to build applications based on KDE games library.

%files -n %{devname}
%{_libdir}/cmake/KF6KDEGames
%{_libdir}/libKF6KDEGamesPrivate.so
%{_libdir}/libKF6KDEGames.so
%{_includedir}/*

#------------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libkdegames6
