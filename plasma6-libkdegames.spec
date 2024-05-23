#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	KDE games library
Name:		plasma6-libkdegames
Version:	24.05.0
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://games.kde.org/
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/libkdegames/-/archive/%{gitbranch}/libkdegames-%{gitbranchd}.tar.bz2#/libkdegames-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/libkdegames-%{version}.tar.xz
%endif
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

%description common
This package provides common files needed by KDE games such as carddecks
for KDE cardgames.

%files common -f libkdegames6.lang
%{_datadir}/qlogging-categories6/libkdegames.categories
%{_datadir}/carddecks/

#-------------------------------------------------------------------------------

%package corebindings
Summary:	Qml plugins for KDE games
Group:		Graphical desktop/KDE

%description corebindings
Qml plugins for KDE games.

%files corebindings
%{_libdir}/qt6/qml/org/kde/games

#-------------------------------------------------------------------------------

%define KDEGames6_major 6
%define libKDEGames6 %mklibname KF6KDEGames6 %{KDEGames6_major}

%package -n %{libKDEGames6}
Summary:	Runtime Library for KDE games
Group:		System/Libraries

%description -n %{libKDEGames6}
Runtime Library for KDE games.

%files -n %{libKDEGames6}
%{_libdir}/libKDEGames6.so.%{KDEGames6_major}*

#-------------------------------------------------------------------------------

%define KDEGames6Private_major 6
%define libKDEGames6Private %mklibname KDEGames6Private %{KDEGames6Private_major}

%package -n %{libKDEGames6Private}
Summary:	Runtime Library for KDE games
Group:		System/Libraries

%description -n %{libKDEGames6Private}
Runtime Library for KDE games.

%files -n %{libKDEGames6Private}
%{_libdir}/libKDEGames6Private.so.%{KDEGames6Private_major}*

#-------------------------------------------------------------------------------

%define devname %mklibname KDEGames6 -d

%package -n %{devname}
Summary:	Headers files for KDE games library
Group:		Development/KDE and Qt
Requires:	%{libKDEGames6} = %{EVRD}
Requires:	%{libKDEGames6Private} = %{EVRD}

%description -n %{devname}
Headers files needed to build applications based on KDE games library.

%files -n %{devname}
%{_libdir}/cmake/KDEGames6
%{_libdir}/libKDEGames6Private.so
%{_libdir}/libKDEGames6.so
%{_includedir}/*

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n libkdegames-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libkdegames6
