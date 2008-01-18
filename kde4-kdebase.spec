# TODO:
# - check BR list
# - more file moves between packages
# - Req, Obsolets and Conflicts for every package
# - new dsecriptions

# Conditional build:
%bcond_without	hidden_visibility	# pass '--fvisibility=hidden' & '--fvisibility-inlines-hidden' to g++
#
<<<<<<< kdebase4.spec
%define		_state		stable
%define		_minlibsevr	9:%{version}
=======
%define		_state		stable
%define		_minlibsevr	9:4.0.0
>>>>>>> 1.2

Summary:	K Desktop Environment - core files
Summary(es.UTF-8):   K Desktop Environment - archivos básicos
Summary(ja.UTF-8):   KDEデスクトップ環境 - 基本ファイル
Summary(ko.UTF-8):   KDE - 기본 파일
Summary(pl.UTF-8):   K Desktop Environment - pliki środowiska
Summary(pt_BR.UTF-8):   K Desktop Environment - arquivos básicos
Summary(ru.UTF-8):   K Desktop Environment - базовые файлы
Summary(uk.UTF-8):   K Desktop Environment - базові файли
Summary(zh_CN.UTF-8):   KDE核心
<<<<<<< kdebase4.spec
%define	orgname	kdebase
Name:		kdebase4
Version:	4.0.0
=======
Name:		kdebase4
Version:	4.0.0
>>>>>>> 1.2
Release:	0.1
Epoch:		9
License:	GPL
Group:		X11/Applications
<<<<<<< kdebase4.spec
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/latest/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	01d8f2f16cbd4e225efc996b0dd39769
Source1:	%{name}-kdesktop.pam
Source2:	%{name}-kdm.pam
Source3:	%{name}-kdm-np.pam
Source4:	%{name}-kdm.init
Source5:	%{name}-kdm.Xsession
Source6:	%{name}-kdm_pldlogo.png
Source7:	%{name}-kdm_pldwallpaper.png
#Source8:	%{orgname}-searchproviders.tar.bz2
=======
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kdebase-%{version}.tar.bz2
# Source0-md5:	01d8f2f16cbd4e225efc996b0dd39769
Source1:	kdebase-kdesktop.pam
Source8:	kdebase-searchproviders.tar.bz2
>>>>>>> 1.2
# Source8-md5:	582b29204e85c01a91799ed72f845312
<<<<<<< kdebase4.spec
#Source10:	%{orgname}-servicemenus.tar.bz2
=======
Source10:	kdebase-servicemenus.tar.bz2
>>>>>>> 1.2
# Source10-md5:	f48ac7af286f4c87961de4bb24d07772
<<<<<<< kdebase4.spec
#Source13:	ftp://ftp.pld-linux.org/software/kde/%{orgname}-konqsidebartng-PLD-entries-0.1.tar.bz2
=======
Source13:	ftp://ftp.pld-linux.org/software/kde/kdebase-konqsidebartng-PLD-entries-0.1.tar.bz2
>>>>>>> 1.2
# Source13-md5:	c8b947bc3e8a2ac050d9e9548cf585fc
# Temporary taken from kde svn
BuildRequires:	OpenEXR-devel >= 1.2.2
BuildRequires:	OpenGL-devel
%{?with_hidden_visibility:BuildRequires:	QtCore-devel >= 4.2.0}
BuildRequires:	QtNetwork-devel >= 4.2.0
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	cdparanoia-III-devel
BuildRequires:	cups-devel
BuildRequires:	cyrus-sasl-devel
BuildRequires:	db-devel
#BuildRequires:	dbus-qt-devel >= 0.70
BuildRequires:	ed
%{?with_hidden_visibility:BuildRequires:	gcc-c++ >= 5:4.1.0-0.20051206r108118.1}
BuildRequires:	gettext-devel
BuildRequires:	hal-devel
BuildRequires:	jasper-devel
BuildRequires:	kdelibs4-devel >= %{_minlibsevr}
BuildRequires:	kdepimlibs4-devel >= %{version}
BuildRequires:	lame-libs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libraw1394-devel >= 1.2.0
BuildRequires:	libsmbclient-devel >= 3.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libusb-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	lm_sensors-devel
BuildRequires:	motif-devel
BuildRequires:	openssl-devel >= 0.9.7c
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	qimageblitz-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	samba-devel
BuildRequires:	sed >= 4.0
#BuildRequires:	unsermake >= 040511
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libfontenc-devel
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-proto-scrnsaverproto-devel
BuildRequires:	xorg-util-imake
BuildConflicts:	kdebase-konqueror-libs
Conflicts:	kdelibs < 9:3.1.94.040110-1
# TODO: sensors
#BuildRequires:	sensors-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	libtool(.*)
%define		_xdgdatadir	%{_datadir}/desktop-directories
# openexr detection fails
%undefine	configure_cache

%description
This package contains KDE base system which includes:
- KDE Control Centre with modules
- KDesktop (a desktop) and Kicker (a panel)
- KWin window manager and several decorations
- KDE splash themes and plugins
- thumbnail creation, mail, news and terminal emulation support
- many more.

%description -l ja.UTF-8
KDEデスクトップ環境用の基本アプリケーション。
以下のようなパッケージが入っています。

%description -l pl.UTF-8
Ten pakiet zawiera podstawowe aplikacje KDE:
- Centrum sterowania z modułami
- KDesktop (pulpit) i Kicker (panel)
- menedżer okien Kwin i dekoracje
- ekrany startowe KDE
- obsługę podglądu plików, protokołów poczty i news oraz emulacji
  terminala

%description -l ru.UTF-8
Базовые программы для K Desktop Environment. Включены: 
kwin (оконный менеджер), konqueror (файловый менеджер,
web-браузер, ftp-клиент, ...), konsole (замена xterm), kicker
(запускалка программ и пейджер рабочего стола), kaudio (аудиосервер),
kdehelp (программа для просмотра справочных файлов kde, файлов info и
man), kthememgr (система для управления альтернативными пакетами тем)
и другие компоненты KDE (kcheckpass, kikbd, kscreensaver, kcontrol,
kfind, kfontmanager, kmenuedit, kappfinder).

%description -l uk.UTF-8
Базові програми для K Desktop Environment. Включені: 
kwin (віконный менеджер), konqueror (файловий менеджер, web-браузер,
ftp-кліент, ...), konsole (заміна xterm), kicker (запускалка програм
та пейджер робочого столу), kaudio (аудіосервер), kdehelp (програма
для перегляду файлів довідки kde, файлів info та man), kthememgr
(система для керування альтернативними пакетами тем) та інші
компоненти KDE (kcheckpass, kikbd, kscreensaver, kcontrol, kfind,
kfontmanager, kmenuedit, kappfinder).

%package devel
Summary:	Include files to develop KDE applications
Summary(pl.UTF-8):   Pliki nagłówkowe potrzebne do tworzenia aplikacji KDE
Summary(pt_BR.UTF-8):   Arquivos de inclusão para compilar aplicativos que usem bibliotecas do kdebase
Group:		X11/Development/Libraries
Requires:	%{name}-desktop-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-libksgrd = %{epoch}:%{version}-%{release}
Requires:	kdelibs-devel >= %{_minlibsevr}
#Obsoletes:	kdebase-ksysguard-libs

%description devel
This package contains header files needed to develop KDE applications.

%description devel -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe niezbędne do programowania aplikacji
KDE.

%description devel -l pt_BR.UTF-8
Este pacote contém os arquivos de inclusão que são necessários para
compilar aplicativos que usem bibliotecas do kdebase.

<<<<<<< kdebase4.spec
%package -n kde4-decoration-b2
Summary:	KDE Window Decoration - B2
Summary(pl.UTF-8):   Dekoracja okna dla KDE - B2
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde4-decoration-b2
A Beos like window decoration with rectangular window title to the
left. The actual window decoration does not take more than 20-30% of
the screen width and if two window titles overlap each other, they are
aligned next to each other.

%description -n kde4-decoration-b2 -l pl.UTF-8
Podobna do Beos dekoracja okien z prostokątnym tytułem okna po lewej
stronie. Nie zajmuje ona więcej niż 20-30% szerokości ekranu, a w
przypadkach gdyby dwie dekoracje się zasłaniały, są one układane obok
siebie.

%package -n kde4-decoration-keramik
Summary:	KDE Window Decoration - keramik
Summary(pl.UTF-8):   Dekoracja okna dla KDE - keramik
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}
Conflicts:	kdebase-desktop < 9:3.3.91

%description -n kde4-decoration-keramik
KDE Window Decoration - keramik.

%description -n kde4-decoration-keramik -l pl.UTF-8
Dekoracja okna dla KDE - keramik.

%package -n kde4-decoration-laptop
Summary:	KDE Window Decoration - Laptop
Summary(pl.UTF-8):   Dekoracja okna dla KDE - Laptop
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde4-decoration-laptop
A window decoration with stripped window title and lightly convex
window buttons.

%description -n kde4-decoration-laptop -l pl.UTF-8
Dekoracja okna z paskowanym tytułem okna oraz lekko wypukłymi
przyciskami okna.

%package -n kde4-decoration-modernsys
Summary:	KDE Window Decoration - ModernSys
Summary(pl.UTF-8):   Dekoracja okna dla KDE - ModernSys
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde4-decoration-modernsys
A window decoration with small, top-aligned window buttons and a
window title with gray lines surronding the text of the title. Also
with a convex resize handle on the bottom-right window corner.

%description -n kde4-decoration-modernsys -l pl.UTF-8
Dekoracja okna z małymi, wyrównanymi do góry przyciskami okna oraz
tytułem okna otoczonym szarymi liniami. Ma również wypukły uchwyt
służący do zmiany rozmiaru w prawym dolnym rogu okna.

%package -n kde4-decoration-quartz
Summary:	KDE Window Decoration - Quartz
Summary(pl.UTF-8):   Dekoracja okna dla KDE - Quartz
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde4-decoration-quartz
A window decoration with solid borders. The window caption consists of
a lighter area for the window title and a darker area for window
buttons. Between the two area there is a stylish transition.

%description -n kde4-decoration-quartz -l pl.UTF-8
Dekoracja okna z pełnymi krawędziami. Nagłówek okna składa się z
jasnego obszaru dla tytułu okna i ciemniejszego dla przycisków. Między
obszarami jest stylowy przejście.

%package -n kde4-decoration-redmond
Summary:	KDE Window Decoration - Redmond
Summary(pl.UTF-8):   Dekoracja okna dla KDE - Redmond
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde4-decoration-redmond
A window decoration resembling the one from Windows 98.

%description -n kde4-decoration-redmond -l pl.UTF-8
Dekoracja okna przypominająca tę z Windows 98.

%package -n kde4-decoration-web
Summary:	KDE Window Decoration - Web
Summary(pl.UTF-8):   Dekoracja okna dla KDE - Web
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde4-decoration-web
A completely flat window decoration with rounded corners and visible,
thin borders.

%description -n kde4-decoration-web -l pl.UTF-8
Zupełnie płaska dekoracja okna z zaokrąglonymi brzegami oraz
widocznymi, cienkimi krawędziami.

%package -n kde4-kgreet-classic
Summary:	KDE greeter libraries
Summary(pl.UTF-8):   Biblioteki służące do zapytań o hasło
Group:		X11/Libraries
Requires:	kdelibs4 >= %{_minlibsevr}
Provides:	kde-kgreet
Conflicts:	kdm <= 3.2.90.040503-1

%description -n kde4-kgreet-classic
Tools for asking for passwords in the classic, default look.

%description -n kde4-kgreet-classic -l pl.UTF-8
Narzędzia służące do zapytań o hasło - klasyczny, domyślny motyw
wyglądu.

%package -n kde4-kgreet-winbind
Summary:	KDE greeter libraries
Summary(pl.UTF-8):   Biblioteki służące do zapytań o hasło
Group:		X11/Libraries
Requires:	kdelibs4 >= %{_minlibsevr}
Provides:	kde-kgreet
Conflicts:	kdm <= 3.2.90.040503-1

%description -n kde4-kgreet-winbind
Tools for asking for passwords - winbind.

%description -n kde4-kgreet-winbind -l pl.UTF-8
Narzędzia służące do zapytań o hasło - winbind.

%package -n kde4-kio-ldap
Summary:	KDE LDAP protocol service
Summary(pl.UTF-8):   Obsługa protokołu LDAP
Group:		X11/Libraries
Requires:	kdelibs4 >= %{_minlibsevr}
Conflicts:	konqueror < 9:3.5.5

%description -n kde4-kio-ldap
KDE LDAP protocol service.

%description -n kde4-kio-ldap -l pl.UTF-8
Obsługa protokołu LDAP.

%package -n kde4-kio-nntp
Summary:	KDE NNTP protocol service
Summary(pl.UTF-8):   Obsługa protokołu NNTP
Group:		X11/Libraries
Requires:	kdelibs4 >= %{_minlibsevr}
Obsoletes:	kdebase-mailnews

%description -n kde4-kio-nntp
KDE NNTP protocol service.

%description -n kde4-kio-nntp -l pl.UTF-8
Obsługa protokołu NNTP.

%package -n kde4-kio-pop3
Summary:	KDE POP3 protocol service
Summary(pl.UTF-8):   Obsługa protokołu POP3
Group:		X11/Libraries
Requires:	kdelibs4 >= %{_minlibsevr}
Obsoletes:	kdebase-mailnews

%description -n kde4-kio-pop3
KDE POP3 protocol service.

%description -n kde4-kio-pop3 -l pl.UTF-8
Obsługa protokołu POP3.

%package -n kde4-kio-smtp
Summary:	KDE SMTP protocol service
Summary(pl.UTF-8):   Obsługa protokołu SMTP
Group:		X11/Libraries
Requires:	kdelibs4 >= %{_minlibsevr}
Obsoletes:	kdebase-mailnews

%description -n kde4-kio-smtp
KDE SMTP protocol service.

%description -n kde4-kio-smtp -l pl.UTF-8
Obsługa protokołu SMTP.

%package -n kde4-kside-default
Summary:	Default kicker sidebar
Summary(pl.UTF-8):   Domyślny boczny pasek do menu KDE
Group:		Themes
Requires:	%{name}-desktop >= 9:3.5.5
Provides:	kde-kside
Obsoletes:	kde-kside

%description -n kde4-kside-default
Default kicker sidebar with a gear and the K Desktop Environment text.

%description -n kde4-kside-default -l pl.UTF-8
Domyślny boczny pasek do menu KDE z turbinką oraz napisem K Desktop
Environment.

%package -n kde4-logoutpic-default
Summary:	KDE "Logout" picture
Summary(pl.UTF-8):   Obrazek okna "Wyloguj" KDE
Group:		X11/Amusements
Requires:	%{name}-desktop
Provides:	kde-logoutpic
Obsoletes:	kde-logoutpic-PLD

%description -n kde4-logoutpic-default
Default "Logout" picture with a KDE logo.

%description -n kde4-logoutpic-default -l pl.UTF-8
Standardowy obrazek okna "Wyloguj" z logiem KDE.

%package -n kde4-splash-Default
Summary:	Default clasic KDE splashscreen
Summary(pl.UTF-8):   Domyślny klasyczny ekran startowy KDE
Group:		X11/Amusements
# DONT PUT STRICT R: HERE
Requires:	%{name}-desktop >= %{epoch}:%{version}-%{release}
# Because of incorrectly added strict deps there
Obsoletes:	kde-splash-Default-KDE

%description -n kde4-splash-Default
Default splashscreen that came with this version of KDE.

%description -n kde4-splash-Default -l pl.UTF-8
Domyślny ekran powitalny dostarczony w tej wersji KDE.

%package -n kde4-splash-blue-bend
Summary:	KDE blue-bend splashscreen
Summary(pl.UTF-8):   Ekran powitalny KDE blue-bend
Group:		X11/Amusements
# DONT PUT STRICT R: HERE
Requires:	%{name}-desktop >= %{epoch}:%{version}-%{release}

%description -n kde4-splash-blue-bend
KDE blue-bend splashcreen.

%description -n kde4-splash-blue-bend -l pl.UTF-8
Ekran powitalny KDE blue-bend.

%package -n kde4-splashplugin-Redmond
Summary:	ksplash plugin Redmond
Summary(pl.UTF-8):   Wtyczka ksplash Redmond
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}
Obsoletes:	kde-splashplugin-XpLike

%description -n kde4-splashplugin-Redmond
A splash screen plugin that resembles the Windows XP post login
animations.

%description -n kde4-splashplugin-Redmond -l pl.UTF-8
Wtyczka ekranu powitalnego KDE, podobna do animacji, które w Windows
XP mają miejsce po zalogowaniu.

%package -n kde4-splashplugin-Standard
Summary:	ksplash plugin Standard
Summary(pl.UTF-8):   Wtyczka ksplash Standard
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde4-splashplugin-Standard
A standard splash screen plugin for KDE. It is themable and shows
splashscreens on the center of the screen. The splash themes for this
plugin consist of a main picture and two icon bars that are shown
under it. For every step of the loading process a different icon is
highlighted.

%description -n kde4-splashplugin-Standard -l pl.UTF-8
Standardowa wtyczka uruchamiana podczas startu KDE. Obsługuje motywy i
pokazuje ekrany startowe na środku ekranu. Motywy startowe dla tej
wtyczki składają się z głównego obrazka i dwóch pasków ikon pod nim
pokazywanych. Dla każdego kroku procesu ładowania podświetlana jest
inna ikona.

=======
>>>>>>> 1.2
%package common-filemanagement
Summary:	Common Files for kate and konqueror
Summary(pl.UTF-8):   Pliki wspólne dla kate i konquerora
Group:		X11/Libraries
Requires:	%{name}-common-konsole = %{epoch}:%{version}-%{release}
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description common-filemanagement
Thumbnail and file sharing libraries for kate and konqueror.

%description common-filemanagement -l pl.UTF-8
Biblioteki służące do tworzenia podglądu i wymiany plików dla kate i
konquerora.

%package common-konsole
Summary:	Common files for konsole and konsolepart
Summary(pl.UTF-8):   Pliki wspólne dla konsole i konsolepart
Group:		X11/Applications
Requires(post,postun):	fontpostinst
Requires:	kdelibs4 >= %{_minlibsevr}
Obsoletes:	kdebase < 3.5.5
Obsoletes:	kdebase-fonts

%description common-konsole
Color schemes, icons, fonts and shell profiles for konsole.

%description common-konsole -l pl.UTF-8
Schematy kolorów, ikony, czcionki oraz profile sesji dla konsole.

%package core
Summary:	KDE Core Apps
Summary(pl.UTF-8):   Podstawowe aplikacje KDE
Group:		X11/Applications
Requires:	kdelibs4 >= %{_minlibsevr}
Requires:	sudo
Requires:	xdg-menus
Obsoletes:	kdebase < 8:3.5.5
Obsoletes:	kdebase-helpcenter
Obsoletes:	kdebase-kcontrol
Obsoletes:	kdebase-khelpcenter
Conflicts:	kttsd <= 040609

%description core
KDE Core apps. This package contains:
- Control Center;
- Help Center;
- Print System;
- Crash Handlers;
- A Frontend for "su" program.

%description core -l pl.UTF-8
Podstawowe aplikacje środowiska KDE. Pakiet ten zawiera:
- Centrum sterowania;
- System drukowania;
- System pomocy;
- Programy obsługi błędów;
- Frontend dla programu "su".

%package desktop
Summary:	KDesktop - handling of desktop icons, popup menus etc.
Summary(pl.UTF-8):   KDesktop - obsługa ikon na pulpicie, menu itp.
Group:		X11/Applications
Requires:	%{name}-desktop-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-kdialog = %{epoch}:%{version}-%{release}
Requires:	%{name}-kfind = %{epoch}:%{version}-%{release}
Requires:	eject
Requires:	kde4-kgreet
Requires:	kde4-kside
Requires:	kde4-logoutpic
Requires:	kde4-splash-Default
Requires:	konqueror4 = %{epoch}:%{version}-%{release}
Requires:	pam >= 0.79.0
Provides:	kdebase4-kicker
Obsoletes:	kde-decoration-plastik
Obsoletes:	kde-theme-keramik
Obsoletes:	kdebase
Obsoletes:	kdebase-fonts
Obsoletes:	kdebase-kcheckpass
Obsoletes:	kdebase-kdesktop
Obsoletes:	kdebase-kdesktop_lock
Obsoletes:	kdebase-khelpcenter
Obsoletes:	kdebase-kicker
Obsoletes:	kdebase-kioslave
Obsoletes:	kdebase-kmenuedit
Obsoletes:	kdebase-konqueror
Obsoletes:	kdebase-ksystraycmd
Obsoletes:	kdebase-kwin
Obsoletes:	kdebase-kwin_plugin
Obsoletes:	kdebase-kwmtheme
Obsoletes:	kdebase-kxmlrpc
Obsoletes:	kdebase-screensaver
Obsoletes:	kdebase-static
Obsoletes:	kdebase-wallpapers
Obsoletes:	khotkeys
Conflicts:	kdeedu-libkdeeduui < 8:3.5.5

%description desktop
KDesktop is the program that handles the desktop icons, the popup
menus for the desktop, the mac menubar, and the screensaver system.

%description desktop -l pl.UTF-8
KDesktop to program obsługujący ikony na pulpicie, menu dla pulpitu,
pasek menu oraz system wygaszacza ekranu.

%package desktop-libs
Summary:	KDesktop libraries
Summary(pl.UTF-8):   Biblioteki KDesktop
Group:		X11/Libraries
Requires(post,postun):	/sbin/ldconfig
Requires:	konqueror4-libs = %{epoch}:%{version}-%{release}
Obsoletes:	kdebase-desktop < 9:3.5.5
Obsoletes:	kdebase-kicker-libs

%description desktop-libs
KDesktop libraries (taskbar, splash themes and window decorations).

%description desktop-libs -l pl.UTF-8
Biblioteki KDesktop (pasek zadań, obsługa motywów obrazków startowych
i dekoracji okna).

%package infocenter
Summary:	KDE Info Center
Summary(pl.UTF-8):   Centrum informacji o systemie dla KDE
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	pciutils

%description infocenter
Application for displaying information about your system.

%description infocenter -l pl.UTF-8
Centrum informacji o systemie dla KDE.

%package kappfinder
Summary:	Menu Updating Tool
Summary(pl.UTF-8):   Narzędzie do aktualizacji menu
Group:		X11/Applications
Requires:	kdelibs4 >= %{_minlibsevr}
Obsoletes:	kdebase =< 8:3.5.5

%description kappfinder
The tool for finding installed application and adding them to your
menu.

%description kappfinder -l pl.UTF-8
Narzędzie do wyszukiwania zainstalowanych aplikacji i dodawania ich do
menu.

%package kdialog
Summary:	A KDE version of dialog
Summary(pl.UTF-8):   Wersja KDE dialogu
Group:		X11/Applications
Requires:	kdelibs4 >= %{_minlibsevr}
Obsoletes:	kdebase < 8:3.5.5

%description kdialog
Kdialog allows to display window dialogs with KDE widgets from shell
scripts.

%description kdialog -l pl.UTF-8
Kdialog umożliwia wyświetlanie komunikatów w okienkach KDE z poziomu
skryptów powłoki.

%package kfind
Summary:	KDE Find Tool
Summary(pl.UTF-8):   Narzędzie do wyszukiwania plików dla KDE
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	kfind

%description kfind
A tool for find files for KDE.

%description kfind -l pl.UTF-8
Narzędzie do wyszukiwania plików dla KDE.

<<<<<<< kdebase4.spec
%package kfontinst
Summary:	K Font Installer
Summary(pl.UTF-8):   Instalator fontów dla KDE
Group:		X11/Applications
#Requires:	konqueror = %{epoch}:%{version}-%{release}
# for /usr/share/doc/kde/HTML/en/kcontrol, probably stupid
Requires:	kdebase4-core = %{epoch}:%{version}-%{release}
Obsoletes:	kdebase-desktop < 3.5.5

%description kfontinst
KDE font installer.

%description kfontinst -l pl.UTF-8
Instalator czcionek dla KDE.

%package kjobviewer
Summary:	Print Job Viewer
Summary(pl.UTF-8):   Podgląd zadań drukowania
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description kjobviewer
KDE print queue viewer.

%description kjobviewer -l pl.UTF-8
Przeglądarka kolejki drukowania dla KDE.

%package klipper
Summary:	Clipboard Tool
Summary(pl.UTF-8):   Narzędzie schowka
Group:		X11/Applications
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description klipper
A tool extending the clipboard support for KDE. Note that it requires
a powerful computer.

%description klipper -l pl.UTF-8
Narzędzie rozszerzające obsługę schowka dla KDE. Wymaga ono szybkiego
systemu.

=======
>>>>>>> 1.2
%package konsole
Summary:	KDE Terminal Emulator
Summary(pl.UTF-8):   Emulator terminala dla KDE
Group:		X11/Applications
Requires:	%{name}-common-konsole = %{epoch}:%{version}-%{release}
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	konsole

%description konsole
KDE Terminal Emulator.

%description konsole -l pl.UTF-8
Emulator terminala dla KDE.

<<<<<<< kdebase4.spec
%package kpager
Summary:	Desktop Pager
Summary(pl.UTF-8):   Przełącznik biurek
Group:		X11/Applications
Requires:	kdelibs4 >= %{_minlibsevr}
Obsoletes:	kdebase =< 8:3.5.5

%description kpager
KDE Desktop Pager.

%description kpager -l pl.UTF-8
Przełącznik biurek dla KDE.

%package kpersonalizer
Summary:	KDE desktop settings wizard
Summary(pl.UTF-8):   Kreator ustawień środowiska KDE
Group:		X11/Applications
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}
Requires:	%{name}-klipper = %{epoch}:%{version}-%{release}
Obsoletes:	kdebase < 9:3.5.5

%description kpersonalizer
KDE desktop settings wizard.

%description kpersonalizer -l pl.UTF-8
Kreator ustawień środowiska KDE.

%package ksysguard
Summary:	System Guard
Summary(pl.UTF-8):   Strażnik systemu
Group:		X11/Applications
Requires(post,postun):	/sbin/ldconfig
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	%{name}-libksgrd = %{epoch}:%{version}-%{release}

%description ksysguard
KDE System Guard.

%description ksysguard -l pl.UTF-8
Strażnik systemu dla KDE.

=======
>>>>>>> 1.2
%package kwrite
Summary:	KDE Text Editor
Summary(pl.UTF-8):   Edytor tekstu dla KDE
Group:		X11/Applications/Editors
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	kwrite

%description kwrite
KWrite is a simple texteditor, with syntaxhighlighting, codefolding,
dynamic word wrap and more, it's the lightweight version of Kate,
providing more speed for minor tasks.

%description kwrite -l pl.UTF-8
KWrite to prosty edytor tekstu z podświetlaniem składni, zwijaniem
kodu, dynamicznym zawijaniem wierszy itp. Jest lżejszą wersją Kate,
szybszą dla mniejszych zadań.

%package kwrited
Summary:	KDE write messaging daemon
Summary(pl.UTF-8):   Demon do KDE obsługujący wymianę wiadomości za pomocą write
Group:		X11/Applications
# With functional reasons
Requires:	kdebase4-core = %{epoch}:%{version}-%{release}
Obsoletes:	kdebase < 8:3.5.5

%description kwrited
A kde daeomn that watches for messages from local users sent with
write or wall.

%description kwrited -l pl.UTF-8
Demon KDE, który monitoruje wiadomości jakie lokalni użytkownicy
wysyłają za pomocą komend write lub wall.

<<<<<<< kdebase4.spec
%package libkate
Summary:	A libraries for KDE text editors
Summary(pl.UTF-8):   Biblioteki dla edytorów tekstu KDE
Group:		X11/Libraries
Requires(post,postun):	/sbin/ldconfig
Requires:	kdelibs4 >= %{_minlibsevr}
Obsoletes:	kdebase-kate < 8:3.5.5
Obsoletes:	kdebase-libkmultitabbar

%description libkate
A libraries shared between KDE text editors. They provide an
embeddable kate interface.

%description libkate -l pl.UTF-8
Biblioteki współdzielone między edytorami tekstu w KDE. Dostarczają
interfejs kate, który można osadzać w innych aplikacjach.

%package libksgrd
Summary:	ksgrd library
Summary(pl.UTF-8):   Biblioteka ksgrd
Group:		X11/Libraries
Requires(post,postun):	/sbin/ldconfig
Requires:	kdelibs4 >= %{_minlibsevr}
Obsoletes:	kdebase-ksysguard-libs
Obsoletes:	ksysguard < 9:3.5.5

%description libksgrd
A library containing functions for the system monitor KSysGuard.

%description libksgrd -l pl.UTF-8
Biblioteka zawierające funkcje monitora systemu - KSysGuard.

%package screensavers
Summary:	KDE screensavers
Summary(pl.UTF-8):   Wygaszacze ekranu desktopu KDE
Summary(ru.UTF-8):   хранители экрана для KDE
Summary(uk.UTF-8):   зберігачі екрану для KDE
Group:		X11/Applications
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description screensavers
KDE screensavers.

%description screensavers -l pl.UTF-8
Wygaszacze ekranu desktopu KDE.

%description screensavers -l ru.UTF-8
Некоторые 3D хранители экрана для K Desktop Environment.

=======
>>>>>>> 1.2
%package useraccount
Summary:	User Account
Summary(pl.UTF-8):   Konto użytkownika
Group:		X11/Applications
Obsoletes:	kdeutils-kdepasswd
Obsoletes:	kdeutils-userinfo

%description useraccount
useraccount changes user account information. This module contains
kdepasswd program functionality.

%description useraccount -l pl.UTF-8
useraccount zmienia informacje o koncie użytkownika. Ten moduł zawiera
funkcjonalność programu kdepasswd.

<<<<<<< kdebase4.spec
%package -n kdm4
Summary:	KDE Display Manager
Summary(pl.UTF-8):   Zarządca ekranów KDE
=======
%package -n dolphin
Summary:	Dolphin - KDE4 file manager
Summary(pl.UTF-8):   Dolphin - menadżer plików KDE4
>>>>>>> 1.2
Group:		X11/Applications
<<<<<<< kdebase4.spec
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	kde4-kgreet
Requires:	pam >= 0.79.0
Requires:	rc-scripts
Requires:	xorg-app-sessreg
Obsoletes:	X11-xdm
Obsoletes:	entrance
Obsoletes:	gdm
Obsoletes:	kdebase-kdm
Obsoletes:	kdebase-pam
Obsoletes:	wdm
Obsoletes:	xdm

%description -n kdm4
A program used for managing X11 sessions on local or remote computers.
Also provides graphical login method.

%description -n kdm4 -l pl.UTF-8
Program służący do zarządzania zarówno lokalnymi jak i zdalnymi
sesjami X11. Udostępnia także graficzny tryb logowania.
=======

%description -n dolphin
Dolphin - KDE4 file manager.
>>>>>>> 1.2

%package -n konqueror4
Summary:	Konqueror - web browser and file manager
Summary(pl.UTF-8):   Konqueror - przeglądarka WWW i zarządca plików
Group:		X11/Applications
Requires:	%{name}-common-filemanagement = %{epoch}:%{version}-%{release}
Requires:	konqueror4-libs = %{epoch}:%{version}-%{release}
Provides:	wwwbrowser
Obsoletes:	kdebase-konqueror
Obsoletes:	kdebase-libkmultitabbar

%description -n konqueror4
Konqueror is the file manager for the K Desktop Environment. It
supports basic file management on local UNIX filesystems, from simple
cut/copy and paste operations to advanced remote and local network
file browsing.

Konqueror is the canvas for all the latest KDE technology, from KIO
slaves (which provide mechanisms for file access) to component
embedding via the KParts object interface, and it is one of the most
customizable applications available.

Konqueror is an Open Source web browser with HTML4.0 compliance,
supporting Java applets, JavaScript, CSS1 and (partially) CSS2, as
well as Netscape plugins (for example, Flash or RealVideo plugins).

Konqueror is a universal viewing application, capable of embedding
read-only viewing components in itself to view documents without ever
launching another application.

%description -n konqueror4 -l pl.UTF-8
Konqueror to zarządca plików dla środowiska KDE. Obsługuje podstawowe
zarządzanie plikami w lokalnych uniksowych systemach plików, od
prostych operacji wycinania/kopiowania i wklejania do zaawansowanego
przeglądania plików z sieci zdalnych i lokalnych.

Konqueror to podstawa dla wszystkich nowych technologii KDE, od usług
KIO (dostarczających mechanizmy dostępu do plików) po osadzanie
komponentów poprzez interfejs obiektowy KParts i jest jedną z
najbardziej poddających się dostosowaniu do własnych potrzeb
dostępnych aplikacji.

Konqueror jest także przeglądarką WWW o otwartych źródłach, zgodną z
HTML 4.0, obsługującą aplety Javy, JavaScript, CSS1 i (częściowo)
CSS2, a także wtyczki Netscape'a (na przykład Flash i RealAudio).

Konqueror jest uniwersalną aplikacją do przeglądania, umożliwiającą
osadzenie w niej komponentów do przeglądania aby oglądać dokumenty bez
uruchamiania innej aplikacji.

%package -n konqueror4-libs
Summary:	konqueror shared libraries
Summary(pl.UTF-8):   Biblioteki współdzielone konquerora
Group:		X11/Libraries
Requires(post,postun):	/sbin/ldconfig
Requires:	kdelibs4 >= %{_minlibsevr}
Obsoletes:	kdebase-konqueror-libs
Obsoletes:	kdebase-libkickermain
Obsoletes:	kdebase-libkonq
Obsoletes:	kdebase-libkonqsidebarplugin
Obsoletes:	konqueror < 9:3.5.5

%description -n konqueror4-libs
Konqueror shared libraries.

%description -n konqueror4-libs -l pl.UTF-8
Biblioteki współdzielone konquerora.

<<<<<<< kdebase4.spec
%package apidocs
Summary:	API documentation
Summary(pl.UTF-8):   Dokumentacja API
Group:		Documentation
Requires:	kdelibs4 >= 9:3.5.5

%description apidocs
Annotated reference of konqueror,kate,kicker,kcontrol and other
kdebase programming interfaces including:
- class lists
- class members
- namespaces

%description apidocs -l pl.UTF-8
Dokumentacja interfejsów programowania konquerora, kate, kickera,
kcontrol i innych z kdebase z przypisami. Zawiera:
- listy klas i ich składników
- listę przestrzeni nazw (namespace)

=======
>>>>>>> 1.2
%prep
<<<<<<< kdebase4.spec
%setup -q -n %{orgname}-%{version}

#cd kcontrol/ebrowsing/plugins/ikws/searchproviders
#for i in  google*.desktop
#do
#	url=`grep 'Query=' $i|sed -e 's,google.com,google.pl,g'|cut -c 7-`
#	echo "Query[pl]=${url}" >> $i
#done
#cd -
=======
%setup -q -n kdebase-%{version}
>>>>>>> 1.2

%{__sed} -i -e 's/Categories=.*/Categories=Audio;Mixer;/' \
	apps/kappfinder/apps/Multimedia/alsamixergui.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Audio;Recorder;/' \
	apps/kappfinder/apps/Multimedia/rezound.desktop \
	apps/kappfinder/apps/Multimedia/sweep.desktop \
	apps/kappfinder/apps/Multimedia/audacity.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Office;PDA;/' \
	apps/kappfinder/apps/Utilities/xgnokii.desktop
for f in `find . -name \*.desktop`; do
	if grep -q '\[ven\]' $f; then
		sed -i -e 's/\[ven\]/[ve]/' $f
	fi
done

%build
export QTDIR=%{_prefix}
mkdir build
cd build
%cmake \
-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d \
	$RPM_BUILD_ROOT/etc/{X11,pam.d} \
	$RPM_BUILD_ROOT%{_libdir}/kde4/plugins/konqueror

# Install miscleanous PLD files
install %{SOURCE1}	$RPM_BUILD_ROOT/etc/pam.d/kdesktop
<<<<<<< kdebase4.spec
install %{SOURCE2}	$RPM_BUILD_ROOT/etc/pam.d/kdm
install %{SOURCE3}	$RPM_BUILD_ROOT/etc/pam.d/kdm-np
install %{SOURCE4}	$RPM_BUILD_ROOT/etc/rc.d/init.d/kdm
install %{SOURCE5}	$RPM_BUILD_ROOT/etc/X11/kdm/Xsession
install %{SOURCE6}	$RPM_BUILD_ROOT%{_datadir}/apps/kdm/pics/pldlogo.png
install %{SOURCE7}	$RPM_BUILD_ROOT%{_datadir}/wallpapers/kdm_pld.png

#%{__tar} xfj %{SOURCE8} -C $RPM_BUILD_ROOT%{_datadir}/services/searchproviders/
#%{__tar} xfj %{SOURCE10} -C $RPM_BUILD_ROOT%{_datadir}/apps/konqueror/servicemenus/
#mv $RPM_BUILD_ROOT%{_datadir}/apps/konqueror/servicemenus/scripts/* $RPM_BUILD_ROOT%{_bindir}
#rm -rf $RPM_BUILD_ROOT%{_datadir}/apps/konqueror/servicemenus/scripts
#%{__tar} xfj %{SOURCE13} -C $RPM_BUILD_ROOT%{_datadir}/apps/konqsidebartng/virtual_folders/
=======
%{__tar} xfj %{SOURCE13} -C $RPM_BUILD_ROOT%{_datadir}/apps/konqsidebartng/virtual_folders/
>>>>>>> 1.2

%clean
rm -rf $RPM_BUILD_ROOT

%post common-konsole
%{_bindir}/fontpostinst misc

%postun common-konsole
%{_bindir}/fontpostinst misc

%post core -p /sbin/ldconfig
%postun core -p /sbin/ldconfig

%post	desktop-libs	-p /sbin/ldconfig
%postun	desktop-libs	-p /sbin/ldconfig

<<<<<<< kdebase4.spec
%post	libkate		-p /sbin/ldconfig
%postun	libkate		-p /sbin/ldconfig

%post	libksgrd	-p /sbin/ldconfig
%postun	libksgrd	-p /sbin/ldconfig

%post	-n konqueror4-libs	-p /sbin/ldconfig
%postun	-n konqueror4-libs	-p /sbin/ldconfig
=======
%post	-n konqueror-libs	-p /sbin/ldconfig
%postun	-n konqueror-libs	-p /sbin/ldconfig
>>>>>>> 1.2

<<<<<<< kdebase4.spec
%post -n kdm4
/sbin/chkconfig --add kdm
if [ -f /var/lock/subsys/kdm ]; then
	%banner kdm -e <<EOF
 ***************************************************
 *                                                 *
 * NOTE:                                           *
 * To make sure that new version of KDM is running *
 * You should restart KDM with:                    *
 * "/sbin/service kdm restart".                    *
 *                                                 *
 * WARNING:                                        *
 * Restarting KDM will terminate any X session     *
 * started by it!                                  *
 *                                                 *
 ***************************************************

EOF
else
	%banner kdm -e <<EOF
Run "/sbin/service kdm start" to start kdm.

EOF
fi

%preun -n kdm4
if [ "$1" = "0" ]; then
	%service kdm stop
	/sbin/chkconfig --del kdm
fi

=======
>>>>>>> 1.2
%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdolphinprivate.so
%attr(755,root,root) %{_libdir}/libkonq.so
%attr(755,root,root) %{_libdir}/libkonqsidebarplugin.so
%{_includedir}/*.h

%files -n dolphin
%defattr(644,root,root,755)
<<<<<<< kdebase4.spec
#%{_kdedocdir}/en/%{name}-apidocs
%endif

%files -n kde4-decoration-b2
%defattr(644,root,root,755)
%{_libdir}/kde4/kwin3_b2.la
%attr(755,root,root) %{_libdir}/kde4/kwin3_b2.so
%{_libdir}/kde4/kwin_b2_config.la
%attr(755,root,root) %{_libdir}/kde4/kwin_b2_config.so
%{_datadir}/apps/kwin/b2.desktop

%files -n kde4-decoration-keramik
%defattr(644,root,root,755)
%{_libdir}/kde4/kwin3_keramik.la
%attr(755,root,root) %{_libdir}/kde4/kwin3_keramik.so
%{_libdir}/kde4/kwin_keramik_config.la
%attr(755,root,root) %{_libdir}/kde4/kwin_keramik_config.so
%{_datadir}/apps/kwin/keramik.desktop

%files -n kde4-decoration-laptop
%defattr(644,root,root,755)
%{_libdir}/kde4/kwin3_laptop.la
%attr(755,root,root) %{_libdir}/kde4/kwin3_laptop.so
%{_datadir}/apps/kwin/laptop.desktop

%files -n kde4-decoration-modernsys
%defattr(644,root,root,755)
%{_libdir}/kde4/kwin3_modernsys.la
%attr(755,root,root) %{_libdir}/kde4/kwin3_modernsys.so
%{_libdir}/kde4/kwin_modernsys_config.la
%attr(755,root,root) %{_libdir}/kde4/kwin_modernsys_config.so
%{_datadir}/apps/kwin/modernsystem.desktop

%files -n kde4-decoration-quartz
%defattr(644,root,root,755)
%{_libdir}/kde4/kwin3_quartz.la
%attr(755,root,root) %{_libdir}/kde4/kwin3_quartz.so
%{_libdir}/kde4/kwin_quartz_config.la
%attr(755,root,root) %{_libdir}/kde4/kwin_quartz_config.so
%{_datadir}/apps/kwin/quartz.desktop

%files -n kde4-decoration-redmond
%defattr(644,root,root,755)
%{_libdir}/kde4/kwin3_redmond.la
%attr(755,root,root) %{_libdir}/kde4/kwin3_redmond.so
%{_datadir}/apps/kwin/redmond.desktop

%files -n kde4-decoration-web
%defattr(644,root,root,755)
%{_libdir}/kde4/kwin3_web.la
%attr(755,root,root) %{_libdir}/kde4/kwin3_web.so
%{_datadir}/apps/kwin/web.desktop

%files -n kde4-kgreet-classic
%defattr(644,root,root,755)
%{_libdir}/kde4/kgreet_classic.la
%attr(755,root,root) %{_libdir}/kde4/kgreet_classic.so

%files -n kde4-kgreet-winbind
%defattr(644,root,root,755)
%{_libdir}/kde4/kgreet_winbind.la
%attr(755,root,root) %{_libdir}/kde4/kgreet_winbind.so

%if %{with ldap}
%files -n kde4-kio-ldap
%defattr(644,root,root,755)
%{_libdir}/kde4/kio_ldap.la
%attr(755,root,root) %{_libdir}/kde4/kio_ldap.so
%{_datadir}/services/ldap.protocol
%{_datadir}/services/ldaps.protocol
%endif

%files -n kde4-kio-nntp
%defattr(644,root,root,755)
%{_libdir}/kde4/kio_nntp.la
%attr(755,root,root) %{_libdir}/kde4/kio_nntp.so
%{_datadir}/services/nntp.protocol
%{_datadir}/services/nntps.protocol

%files -n kde4-kio-pop3
%defattr(644,root,root,755)
%{_libdir}/kde4/kio_pop3.la
%attr(755,root,root) %{_libdir}/kde4/kio_pop3.so
%{_datadir}/services/pop3.protocol
%{_datadir}/services/pop3s.protocol

%files -n kde4-kio-smtp
%defattr(644,root,root,755)
%{_libdir}/kde4/kio_smtp.la
%attr(755,root,root) %{_libdir}/kde4/kio_smtp.so
%{_datadir}/services/smtp.protocol
%{_datadir}/services/smtps.protocol

%files -n kde4-kside-default
%defattr(644,root,root,755)
%{_datadir}/apps/kicker/pics/kside*.png

%files -n kde4-logoutpic-default
%defattr(644,root,root,755)
%{_datadir}/apps/ksmserver/pics/shutdownkonq.png

%files -n kde4-splash-Default
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/Default

%files -n kde4-splash-blue-bend
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/blue-bend

%files -n kde4-splashplugin-Redmond
%defattr(644,root,root,755)
%{_libdir}/kde4/ksplashredmond.la
%attr(755,root,root) %{_libdir}/kde4/ksplashredmond.so
%{_datadir}/apps/ksplash/Themes/Redmond
%{_datadir}/services/ksplashredmond.desktop

%files -n kde4-splashplugin-Standard
%defattr(644,root,root,755)
%{_libdir}/kde4/ksplashstandard.la
%attr(755,root,root) %{_libdir}/kde4/ksplashstandard.so
%{_datadir}/apps/ksplash/Themes/Standard
%{_datadir}/apps/ksplash/pics/splash.png
%{_datadir}/services/ksplashstandard.desktop
=======
%doc %{_kdedocdir}/en/dolphin/*
%attr(755,root,root) %{_bindir}/dolphin
%attr(755,root,root) %{_libdir}/libdolphinprivate.so.*
%attr(755,root,root) %{_libdir}/kde4/dolphinpart.so
%{_datadir}/config.kcfg/dolphin_columnmodesettings.kcfg
%{_datadir}/config.kcfg/dolphin_detailsmodesettings.kcfg
%{_datadir}/config.kcfg/dolphin_directoryviewpropertysettings.kcfg
%{_datadir}/config.kcfg/dolphin_generalsettings.kcfg
%{_datadir}/config.kcfg/dolphin_iconsmodesettings.kcfg
%{_datadir}/config.kcfg/keditbookmarks.kcfg
%{_datadir}/apps/dolphin/dolphinui.rc
%{_datadir}/apps/dolphin/icons/hicolor/128x128/actions/preview.png
%{_datadir}/apps/dolphin/icons/hicolor/16x16/actions/preview.png
%{_datadir}/apps/dolphin/icons/hicolor/22x22/actions/preview.png
%{_datadir}/apps/dolphin/icons/hicolor/32x32/actions/preview.png
%{_datadir}/apps/dolphin/icons/hicolor/48x48/actions/preview.png
%{_datadir}/apps/dolphin/icons/hicolor/64x64/actions/preview.png
%{_datadir}/apps/dolphin/icons/oxygen/16x16/actions/view-file-columns.png
%{_datadir}/apps/dolphin/icons/oxygen/22x22/actions/view-file-columns.png
%{_datadir}/apps/dolphin/icons/oxygen/32x32/actions/view-file-columns.png
%{_datadir}/apps/dolphin/icons/oxygen/48x48/actions/view-file-columns.png
%{_datadir}/apps/dolphin/icons/oxygen/scalable/actions/view-file-columns.svgz
%{_datadir}/apps/dolphinpart/dolphinpart.rc
%{_desktopdir}/kde4/dolphin.desktop
%{_datadir}/kde4/services/dolphinpart.desktop
>>>>>>> 1.2

%files common-filemanagement
%defattr(644,root,root,755)

%files common-konsole
%defattr(644,root,root,755)
%{_datadir}/apps/konsole

%files core
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kded_konqy_preloader.so
%attr(755,root,root) %{_libdir}/kde4/konq_aboutpage.so
%attr(755,root,root) %{_libdir}/kde4/konq_remoteencoding.so
%attr(755,root,root) %{_libdir}/kde4/konq_shellcmdplugin.so
%attr(755,root,root) %{_libdir}/kde4/konq_sidebar.so
%attr(755,root,root) %{_libdir}/kde4/konq_sidebartree_bookmarks.so
%attr(755,root,root) %{_libdir}/kde4/konq_sidebartree_dirtree.so
%attr(755,root,root) %{_libdir}/kde4/konq_sidebartree_history.so
%attr(755,root,root) %{_libdir}/kde4/konq_sound.so
%attr(755,root,root) %{_libdir}/kde4/konqsidebar_tree.so
%attr(755,root,root) %{_libdir}/kde4/konqsidebar_web.so
%attr(755,root,root) %{_libdir}/kde4/libkcminit_nsplugins.so
%attr(755,root,root) %{_libdir}/kde4/libkhtmlkttsdplugin.so
%attr(755,root,root) %{_libdir}/kde4/libnsplugin.so

%{_datadir}/apps/kcontrol/pics/onlyone.png
%{_datadir}/apps/kcontrol/pics/overlapping.png

%attr(755,root,root) %{_libdir}/libkdeinit4_keditbookmarks.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kfmclient.so
%{_datadir}/apps/khtml/kpartplugins/khtmlkttsd.desktop
%{_datadir}/apps/khtml/kpartplugins/khtmlkttsd.rc

%files desktop
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kdesktop
%{_desktopdir}/kde4/Home.desktop
%{_desktopdir}/kde4/kdepasswd.desktop
%{_desktopdir}/kde4/kfmclient.desktop
%{_desktopdir}/kde4/kfmclient_dir.desktop
%{_desktopdir}/kde4/kfmclient_html.desktop
%{_desktopdir}/kde4/kfmclient_war.desktop
%{_datadir}/apps/kconf_update/favicons.upd
%{_datadir}/apps/kconf_update/kfmclient_3_2.upd
%{_datadir}/apps/kconf_update/kfmclient_3_2_update.sh
%{_datadir}/apps/kconf_update/move_favicons.sh
%{_datadir}/apps/kconf_update/socks.upd
%attr(755,root,root) %{_bindir}/kbookmarkmerger
%{_datadir}/templates
%{_iconsdir}/*/*/apps/*.png
%{_iconsdir}/*/*/apps/*.svgz


%files desktop-libs
%defattr(644,root,root,755)

%files infocenter
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kinfocenter
%{_desktopdir}/kde4/kinfocenter.desktop
%attr(755,root,root) %{_libdir}/libkdeinit4_kinfocenter.so
%{_datadir}/apps/kinfocenter

%files kappfinder
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kappfinder
%{_iconsdir}/*/*/apps/kappfinder.png
%{_datadir}/apps/kappfinder
%{_desktopdir}/kde4/kappfinder.desktop

%files kdialog
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdialog
%{_datadir}/dbus-1/interfaces/org.kde.kdialog.ProgressDialog.xml

%files kfind
%defattr(644,root,root,755)
%doc %{_kdedocdir}/en/kfind/*
%attr(755,root,root) %{_bindir}/kfind
%attr(755,root,root) %{_libdir}/kde4/libkfindpart.so
%{_desktopdir}//kde4/kfind.desktop
%{_datadir}/kde4/services/kfindpart.desktop

%files konsole
%defattr(644,root,root,755)
%doc %{_kdedocdir}/en/konsole/*
%attr(755,root,root) %{_bindir}/konsole
%attr(755,root,root) %{_bindir}/konsoleprofile
%attr(755,root,root) %{_libdir}/libkdeinit4_konsole.so
%attr(755,root,root) %{_libdir}/kde4/libkonsolepart.so
%{_desktopdir}/kde4/konsole.desktop
%{_iconsdir}/*/*/apps/konsole.png
%{_iconsdir}/*/*/apps/konsole.svgz
%{_datadir}/kde4/services/konsole-script.desktop
%{_datadir}/kde4/services/ServiceMenus/konsolehere.desktop
%{_datadir}/kde4/services/konsolepart.desktop

%files kwrite
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwrite
%doc %{_kdedocdir}/en/kwrite/*
%attr(755,root,root) %{_libdir}/libkdeinit4_kwrite.so
%{_datadir}/apps/kwrite
%{_desktopdir}/kde4/kwrite.desktop

%files kwrited
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kded_kwrited.so
%{_datadir}/kde4/services/kded/kwrited.desktop

%files useraccount
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdepasswd
%attr(755,root,root) %{_libdir}/kde4/kcm_useraccount.so
%{_datadir}/apps/kdm/pics/users/*
%{_datadir}/config.kcfg/kcm_useraccount.kcfg
<<<<<<< kdebase4.spec
%{_datadir}/config.kcfg/kcm_useraccount_pass.kcfg
%{_desktopdir}/kde/kdepasswd.desktop
%{_datadir}/services/kcm_useraccount.desktop

%files -n kdm4
%defattr(644,root,root,755)
#%doc README.pam kdm/{ChangeLog,README,TODO}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kdm
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kdm-np
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.kdm
%attr(754,root,root) /etc/rc.d/init.d/kdm
%dir /etc/X11/kdm
%dir /etc/X11/kdm/faces
#%config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/kdmrc
#%config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/backgroundrc
#%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/Xreset
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/Xsession
#%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/Xsetup
#%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/Xstartup
#%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/Xwilling
#%config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/Xaccess
#%dir /etc/X11/kdm/faces
%config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/faces/.default.face.icon
%config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/faces/root.face.icon
%attr(755,root,root) %{_bindir}/genkdmconf
%attr(755,root,root) %{_bindir}/kdm
%attr(755,root,root) %{_bindir}/kdmctl
%attr(755,root,root) %{_bindir}/kdm_config
%attr(755,root,root) %{_bindir}/kdm_greet
%attr(755,root,root) %{_bindir}/krootimage
%{_libdir}/kde4/kcm_kdm.la
%attr(755,root,root) %{_libdir}/kde4/kcm_kdm.so
%{_datadir}/apps/kdm
%{_datadir}/wallpapers/kdm_pld.png
%{_datadir}/services/kdm.desktop
#%{_desktopdir}/kde/kdm.desktop
#%{_iconsdir}/*/*/apps/kdmconfig.png
=======
%{_datadir}/kde4/services/kcm_useraccount.desktop
>>>>>>> 1.2

%files -n konqueror4
%defattr(644,root,root,755)
%doc %{_kdedocdir}/en/konqueror/*
%attr(755,root,root) %{_bindir}/keditbookmarks
%attr(755,root,root) %{_bindir}/keditfiletype
%attr(755,root,root) %{_bindir}/kfmclient
%attr(755,root,root) %{_bindir}/konqueror
%attr(755,root,root) %{_bindir}/nspluginscan
%attr(755,root,root) %{_bindir}/nspluginviewer
%attr(755,root,root) %{_libdir}/libkonquerorprivate.so
%attr(755,root,root) %{_libdir}/kde4/kcm_css.so
%attr(755,root,root) %{_libdir}/kde4/kcm_filetypes.so
%attr(755,root,root) %{_libdir}/kde4/kcm_history.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kio.so
%attr(755,root,root) %{_libdir}/kde4/kcm_konq.so
%attr(755,root,root) %{_libdir}/kde4/kcm_konqhtml.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kurifilt.so
%attr(755,root,root) %{_libdir}/kde4/kcm_performance.so
%attr(755,root,root) %{_libdir}/kde4/kded_favicons.so
%attr(755,root,root) %{_libdir}/libkonq.so.*
%attr(755,root,root) %{_libdir}/libkonqsidebarplugin.so.*
%attr(755,root,root) %{_libdir}/libkonquerorprivate.so.*
%{_desktopdir}/kde4/konqbrowser.desktop
%{_desktopdir}/kde4/konquerorsu.desktop
%{_datadir}/apps/kconf_update/konqsidebartng.upd
%{_datadir}/apps/kconf_update/move_konqsidebartng_entries.sh
%attr(755,root,root) %{_libdir}/libkdeinit4_konqueror.so
%{_datadir}/apps/kbookmark
%{_datadir}/apps/kcmcss
%{_datadir}/apps/keditbookmarks
%{_datadir}/apps/konqiconview
%{_datadir}/apps/konqlistview
%{_datadir}/apps/konqueror/about
%{_datadir}/apps/konqueror/icons
%{_datadir}/apps/konqueror/pics
%{_datadir}/apps/konqueror/profiles
%{_datadir}/kde4/servicetypes/findpart.desktop
%{_datadir}/kde4/servicetypes/konqaboutpage.desktop
%{_datadir}/kde4/servicetypes/konqpopupmenuplugin.desktop
%{_datadir}/kde4/servicetypes/terminalemulator.desktop
%{_datadir}/kde4/servicetypes/uasprovider.desktop
%{_datadir}/kde4/services/useragentstrings/firefox15oncurrent.desktop
%{_datadir}/kde4/services/useragentstrings/firefox20oncurrent.desktop
%{_datadir}/kde4/services/useragentstrings/googlebot.desktop
%{_datadir}/kde4/services/useragentstrings/ie401onwinnt4.desktop
%{_datadir}/kde4/services/useragentstrings/ie50onppc.desktop
%{_datadir}/kde4/services/useragentstrings/ie55onwinnt5.desktop
%{_datadir}/kde4/services/useragentstrings/ie60oncurrent.desktop
%{_datadir}/kde4/services/useragentstrings/ie60onwinnt51.desktop
%{_datadir}/kde4/services/useragentstrings/lynxoncurrent.desktop
%{_datadir}/kde4/services/useragentstrings/mozoncurrent.desktop
%{_datadir}/kde4/services/useragentstrings/mozoncurrent12.desktop
%{_datadir}/kde4/services/useragentstrings/mozonwinxp.desktop
%{_datadir}/kde4/services/useragentstrings/nn301oncurrent.desktop
%{_datadir}/kde4/services/useragentstrings/nn475oncurrent.desktop
%{_datadir}/kde4/services/useragentstrings/nn475onwin95.desktop
%{_datadir}/kde4/services/useragentstrings/ns71oncurrent.desktop
%{_datadir}/kde4/services/useragentstrings/ns71onwinnt51.desktop
%{_datadir}/kde4/services/useragentstrings/op403onwinnt4.desktop
%{_datadir}/kde4/services/useragentstrings/op85oncurrent.desktop
%{_datadir}/kde4/services/useragentstrings/op90oncurrent.desktop
%{_datadir}/kde4/services/useragentstrings/safari12.desktop
%{_datadir}/kde4/services/useragentstrings/safari20.desktop
%{_datadir}/kde4/services/useragentstrings/w3moncurrent.desktop
%{_datadir}/kde4/services/useragentstrings/wgetoncurrent.desktop
%{_datadir}/kde4/services/cache.desktop
%{_datadir}/kde4/services/cookies.desktop
%{_datadir}/kde4/services/desktoppath.desktop
%{_datadir}/kde4/services/ebrowsing.desktop
%{_datadir}/kde4/services/filebehavior.desktop
%{_datadir}/kde4/services/filebrowser.desktop
%{_datadir}/kde4/services/filepreviews.desktop
%{_datadir}/kde4/services/filetypes.desktop
%{_datadir}/kde4/services/kcmcss.desktop
%{_datadir}/kde4/services/kcmhistory.desktop
%{_datadir}/kde4/services/kcmkonqyperformance.desktop
%{_datadir}/kde4/services/kcmperformance.desktop
%{_datadir}/kde4/services/kded/favicons.desktop
%{_datadir}/kde4/services/kded/konqy_preloader.desktop
%{_datadir}/kde4/services/khtml_behavior.desktop
%{_datadir}/kde4/services/khtml_filter.desktop
%{_datadir}/kde4/services/khtml_fonts.desktop
%{_datadir}/kde4/services/khtml_general.desktop
%{_datadir}/kde4/services/khtml_java_js.desktop
%{_datadir}/kde4/services/khtml_plugins.desktop
%{_datadir}/kde4/services/konq_aboutpage.desktop
%{_datadir}/kde4/services/konq_sidebartng.desktop
%{_datadir}/kde4/services/konqfilemgr.desktop
%{_datadir}/kde4/services/konqueror.desktop
%{_datadir}/kde4/services/lanbrowser.desktop
%{_datadir}/kde4/services/netpref.desktop
%{_datadir}/kde4/services/proxy.desktop
%{_datadir}/kde4/services/smb.desktop
%{_datadir}/kde4/services/useragent.desktop
%{_datadir}/apps/konqueror/konqueror.rc
%dir %{_datadir}/apps/plugin
%{_datadir}/apps/plugin/nspluginpart.rc
%{_datadir}/autostart/konqy_preload.desktop
%{_datadir}/config/konqsidebartng.rc
%{_datadir}/apps/konqueror/konq-filemanagement.rc
%{_datadir}/apps/konqueror/konq-webbrowsing.rc
%{_datadir}/config.kcfg/konqueror.kcfg
%{_iconsdir}/*/*/apps/konqueror.*
%{_datadir}/dbus-1/interfaces/org.kde.FavIcon.xml
%{_datadir}/dbus-1/interfaces/org.kde.Konqueror.Main.xml
%{_datadir}/dbus-1/interfaces/org.kde.Konqueror.MainWindow.xml
%{_datadir}/dbus-1/interfaces/org.kde.konqueror.Preloader.xml
%{_datadir}/dbus-1/interfaces/org.kde.libkonq.FileUndoManager.xml
%{_datadir}/dbus-1/interfaces/org.kde.nsplugins.CallBack.xml
%{_datadir}/dbus-1/interfaces/org.kde.nsplugins.class.xml
%{_datadir}/dbus-1/interfaces/org.kde.nsplugins.instance.xml
%{_datadir}/dbus-1/interfaces/org.kde.nsplugins.viewer.xml
%{_datadir}/apps/konqsidebartng/add/virtualfolderadd.desktop
%{_datadir}/apps/konqsidebartng/add/webmodule_add.desktop
%{_datadir}/apps/konqsidebartng/dirtree/bookmarks_module.desktop
%{_datadir}/apps/konqsidebartng/dirtree/dirtree_module.desktop
%{_datadir}/apps/konqsidebartng/dirtree/history_module.desktop
%{_datadir}/apps/konqsidebartng/entries/.version
%{_datadir}/apps/konqsidebartng/entries/bookmarks.desktop
%{_datadir}/apps/konqsidebartng/entries/history.desktop
%{_datadir}/apps/konqsidebartng/entries/home.desktop
%{_datadir}/apps/konqsidebartng/entries/remote.desktop
%{_datadir}/apps/konqsidebartng/entries/root.desktop
%{_datadir}/apps/konqsidebartng/entries/services.desktop
%{_datadir}/apps/konqsidebartng/kicker_entries/bookmarks.desktop
%{_datadir}/apps/konqsidebartng/kicker_entries/history.desktop
%{_datadir}/apps/konqsidebartng/kicker_entries/home.desktop
%{_datadir}/apps/konqsidebartng/kicker_entries/remote.desktop
%{_datadir}/apps/konqsidebartng/kicker_entries/root.desktop
%{_datadir}/apps/konqsidebartng/kicker_entries/services.desktop
%{_datadir}/apps/konqsidebartng/virtual_folders/remote/.directory
%{_datadir}/apps/konqsidebartng/virtual_folders/remote/ftp/.directory
%{_datadir}/apps/konqsidebartng/virtual_folders/remote/ftp/kde_ftp.desktop
%{_datadir}/apps/konqsidebartng/virtual_folders/remote/ftp/pld_ftp.desktop
%{_datadir}/apps/konqsidebartng/virtual_folders/remote/ftp/pld_nest_ftp.desktop
%{_datadir}/apps/konqsidebartng/virtual_folders/remote/web/.directory
%{_datadir}/apps/konqsidebartng/virtual_folders/remote/web/apps_web.desktop
%{_datadir}/apps/konqsidebartng/virtual_folders/remote/web/dot_web.desktop
%{_datadir}/apps/konqsidebartng/virtual_folders/remote/web/kde_web.desktop
%{_datadir}/apps/konqsidebartng/virtual_folders/remote/web/look_web.desktop
%{_datadir}/apps/konqsidebartng/virtual_folders/remote/web/pld_web.desktop
%{_datadir}/apps/konqsidebartng/virtual_folders/services/.directory
%{_datadir}/apps/konqsidebartng/virtual_folders/services/applications.desktop
%{_datadir}/apps/konqsidebartng/virtual_folders/services/audiocd.desktop
%{_datadir}/apps/konqsidebartng/virtual_folders/services/settings.desktop
%{_datadir}/apps/konqsidebartng/websidebar/websidebar.html

%files -n konqueror4-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkonq.so.*.*.*
%attr(755,root,root) %{_libdir}/libkonqsidebarplugin.so.*.*.*
