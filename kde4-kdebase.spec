# TODO:
# - check BR list
# - more file moves between packages
# - Req, Obsolets and Conflicts for every package
# - new dsecriptions

# Conditional build:
%bcond_without	hidden_visibility	# pass '--fvisibility=hidden' & '--fvisibility-inlines-hidden' to g++
#
%define		_state		unstable

Summary:	K Desktop Environment - core files
Summary(es.UTF-8):   K Desktop Environment - archivos básicos
Summary(ja.UTF-8):   KDEデスクトップ環境 - 基本ファイル
Summary(ko.UTF-8):   KDE - 기본 파일
Summary(pl.UTF-8):   K Desktop Environment - pliki środowiska
Summary(pt_BR.UTF-8):   K Desktop Environment - arquivos básicos
Summary(ru.UTF-8):   K Desktop Environment - базовые файлы
Summary(uk.UTF-8):   K Desktop Environment - базові файли
Summary(zh_CN.UTF-8):   KDE核心
%define	orgname	kdebase
Name:		kde4-kdebase
Version:	4.0.60
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	a291f9a05f6634ea5ebf9fbe61aca8a3
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
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	kdelibs-shared >= %{version}
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
Obsoletes:	kdebase4
Conflicts:	kdebase4
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
Requires:	kde4-kdelibs-devel >= %{version}

%description devel
This package contains header files needed to develop KDE applications.

%description devel -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe niezbędne do programowania aplikacji
KDE.

%description devel -l pt_BR.UTF-8
Este pacote contém os arquivos de inclusão que são necessários para
compilar aplicativos que usem bibliotecas do kdebase.

%package common
Summary:	KDE4 common directories
Summary(pl.UTF-8):   Wspólne pliki KDE4.
Group:		X11/Libraries

%description common
KDE4 common directories.

%description common -l pl.UTF-8
Wspólne katalogi KDE4.

%package common-konsole
Summary:	Common files for konsole and konsolepart
Summary(pl.UTF-8):   Pliki wspólne dla konsole i konsolepart
Group:		X11/Applications
#Requires(post,postun):	fontpostinst
Requires:	kde4-kdelibs >= %{version}

%description common-konsole
Color schemes, icons, fonts and shell profiles for konsole.

%description common-konsole -l pl.UTF-8
Schematy kolorów, ikony, czcionki oraz profile sesji dla konsole.

%package core
Summary:	KDE Core Apps
Summary(pl.UTF-8):   Podstawowe aplikacje KDE
Group:		X11/Applications
Requires:	kde4-kdelibs >= %{version}
#Requires:	sudo
#Requires:	xdg-menus
#Conflicts:	kttsd <= 040609

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

%package infocenter
Summary:	KDE Info Center
Summary(pl.UTF-8):	Centrum informacji o systemie dla KDE
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
#Requires:	pciutils

%description infocenter
Application for displaying information about your system.

%description infocenter -l pl.UTF-8
Centrum informacji o systemie dla KDE.


%package kappfinder
Summary:	Menu Updating Tool
Summary(pl.UTF-8):   Narzędzie do aktualizacji menu
Group:		X11/Applications
Requires:	kde4-kdelibs >= %{version}

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
Requires:	kde4-kdelibs >= %{version}

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
Requires:	konqueror-libs = %{version}-%{release}

%description kfind
A tool for find files for KDE.

%description kfind -l pl.UTF-8
Narzędzie do wyszukiwania plików dla KDE.

%package konsole
Summary:	KDE Terminal Emulator
Summary(pl.UTF-8):   Emulator terminala dla KDE
Group:		X11/Applications
Requires:	%{name}-common-konsole = %{version}-%{release}
Requires:	%{name}-core = %{version}-%{release}
#Obsoletes:	konsole

%description konsole
KDE Terminal Emulator.

%description konsole -l pl.UTF-8
Emulator terminala dla KDE.

%package kwrite
Summary:	KDE Text Editor
Summary(pl.UTF-8):   Edytor tekstu dla KDE
Group:		X11/Applications/Editors
Requires:	%{name}-core = %{version}-%{release}
#Obsoletes:	kwrite

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
Requires:	%{name}-core = %{version}-%{release}
#Obsoletes:	kdebase < 8:3.5.5

%description kwrited
A kde daeomn that watches for messages from local users sent with
write or wall.

%description kwrited -l pl.UTF-8
Demon KDE, który monitoruje wiadomości jakie lokalni użytkownicy
wysyłają za pomocą komend write lub wall.

%package useraccount
Summary:	User Account
Summary(pl.UTF-8):   Konto użytkownika
Group:		X11/Applications
#Obsoletes:	kdeutils-kdepasswd
#Obsoletes:	kdeutils-userinfo

%description useraccount
useraccount changes user account information. This module contains
kdepasswd program functionality.

%description useraccount -l pl.UTF-8
useraccount zmienia informacje o koncie użytkownika. Ten moduł zawiera
funkcjonalność programu kdepasswd.

%package -n dolphin
Summary:	Dolphin - KDE4 file manager
Summary(pl.UTF-8):   Dolphin - menadżer plików KDE4
Requires:	konqueror-libs = %{version}-%{release}
Group:		X11/Applications

%description -n dolphin
Dolphin - KDE4 file manager.

%package -n konqueror
Summary:	Konqueror - web browser and file manager
Summary(pl.UTF-8):   Konqueror - przeglądarka WWW i zarządca plików
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}
#Requires:	konqueror-libs = %{version}-%{release}
Provides:	wwwbrowser

%description -n konqueror
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

%description -n konqueror -l pl.UTF-8
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

%package -n konqueror-libs
Summary:	konqueror shared libraries
Summary(pl.UTF-8):   Biblioteki współdzielone konquerora
Group:		X11/Libraries
Requires(post,postun):	/sbin/ldconfig
Requires:	kde4-kdelibs >= %{version}

%description -n konqueror-libs
Konqueror shared libraries.

%description -n konqueror-libs -l pl.UTF-8
Biblioteki współdzielone konquerora.

%prep
%setup -q -n %{orgname}-%{version}

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
install -d build
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
	$RPM_BUILD_ROOT%{_datadir}/apps/kcontrol \
	$RPM_BUILD_ROOT%{_libdir}/kde4/plugins/konqueror \
	$RPM_BUILD_ROOT%{_kdedocdir}/en/kinfocenter

%clean
rm -rf $RPM_BUILD_ROOT

%post common-konsole
%{_bindir}/fontpostinst misc

%postun common-konsole
%{_bindir}/fontpostinst misc

%post core -p /sbin/ldconfig
%postun core -p /sbin/ldconfig

%post	-n konqueror-libs	-p /sbin/ldconfig
%postun	-n konqueror-libs	-p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdolphinprivate.so
%attr(755,root,root) %{_libdir}/libkonq.so
%attr(755,root,root) %{_libdir}/libkonqsidebarplugin.so
%attr(755,root,root) %{_libdir}/libkonquerorprivate.so
%{_includedir}/*.h

%files -n dolphin
%defattr(644,root,root,755)
%{_kdedocdir}/en/dolphin
%attr(755,root,root) %{_bindir}/dolphin
%attr(755,root,root) %{_libdir}/libdolphinprivate.so.*
%attr(755,root,root) %{_libdir}/kde4/dolphinpart.so
%{_datadir}/config.kcfg/dolphin_columnmodesettings.kcfg
%{_datadir}/config.kcfg/dolphin_detailsmodesettings.kcfg
%{_datadir}/config.kcfg/dolphin_directoryviewpropertysettings.kcfg
%{_datadir}/config.kcfg/dolphin_generalsettings.kcfg
%{_datadir}/config.kcfg/dolphin_iconsmodesettings.kcfg
%{_datadir}/config.kcfg/keditbookmarks.kcfg
%dir %{_datadir}/apps/dolphin
%{_datadir}/apps/dolphin/dolphinui.rc
%{_datadir}/apps/dolphin/icons
%dir %{_datadir}/apps/dolphinpart
%{_datadir}/apps/dolphinpart/dolphinpart.rc
%{_desktopdir}/kde4/dolphin.desktop
%{_datadir}/kde4/services/dolphinpart.desktop

%files common
%defattr(644,root,root,755)
%dir %{_desktopdir}/kde4
%dir %{_datadir}/kde4/services/ServiceMenus

%files common-konsole
%defattr(644,root,root,755)
%{_datadir}/apps/konsole

%files core
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/libkcminit_nsplugins.so
%attr(755,root,root) %{_libdir}/kde4/libkhtmlkttsdplugin.so

%dir %{_datadir}/apps/kcontrol
%dir %{_datadir}/apps/kcontrol/pics
%{_datadir}/apps/kcontrol/pics/onlyone.png
%{_datadir}/apps/kcontrol/pics/overlapping.png

%{_datadir}/apps/khtml/kpartplugins/khtmlkttsd.desktop
%{_datadir}/apps/khtml/kpartplugins/khtmlkttsd.rc

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
%dir %{_iconsdir}/oxygen/scalable/apps

%files infocenter
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kinfocenter
%attr(755,root,root) %{_libdir}/libkdeinit4_kinfocenter.so
%dir %{_kdedocdir}/en/kinfocenter
%{_datadir}/apps/kinfocenter
%{_desktopdir}/kde4/kinfocenter.desktop

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
%{_kdedocdir}/en/kfind
%attr(755,root,root) %{_bindir}/kfind
%attr(755,root,root) %{_libdir}/kde4/libkfindpart.so
%{_desktopdir}//kde4/kfind.desktop
%{_datadir}/kde4/services/kfindpart.desktop

%files konsole
%defattr(644,root,root,755)
%{_kdedocdir}/en/konsole
%attr(755,root,root) %{_bindir}/konsole
%attr(755,root,root) %{_bindir}/konsoleprofile
%attr(755,root,root) %{_libdir}/libkdeinit4_konsole.so
%attr(755,root,root) %{_libdir}/kde4/libkonsolepart.so
%{_desktopdir}/kde4/konsole.desktop
#%{_iconsdir}/*/*/apps/konsole.png
#%{_iconsdir}/*/*/apps/konsole.svgz
#%{_datadir}/kde4/services/konsole-script.desktop
%{_datadir}/kde4/services/ServiceMenus/konsolehere.desktop
%{_datadir}/kde4/services/konsolepart.desktop

%files kwrite
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwrite
%{_kdedocdir}/en/kwrite
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
%dir %{_datadir}/apps/kdm
%dir %{_datadir}/apps/kdm/pics
%{_datadir}/apps/kdm/pics/users
%{_datadir}/config.kcfg/kcm_useraccount.kcfg
%{_datadir}/kde4/services/kcm_useraccount.desktop

%files -n konqueror
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/keditbookmarks
%attr(755,root,root) %{_bindir}/keditfiletype
%attr(755,root,root) %{_bindir}/kfmclient
%attr(755,root,root) %{_bindir}/konqueror
%attr(755,root,root) %{_bindir}/nspluginscan
%attr(755,root,root) %{_bindir}/nspluginviewer
%attr(755,root,root) %{_libdir}/kde4/kcm_css.so
%attr(755,root,root) %{_libdir}/kde4/kcm_filetypes.so
%attr(755,root,root) %{_libdir}/kde4/kcm_history.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kio.so
%attr(755,root,root) %{_libdir}/kde4/kcm_konq.so
%attr(755,root,root) %{_libdir}/kde4/kcm_konqhtml.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kurifilt.so
%attr(755,root,root) %{_libdir}/kde4/kcm_performance.so
%attr(755,root,root) %{_libdir}/kde4/kded_favicons.so
%attr(755,root,root) %{_libdir}/kde4/kded_konqy_preloader.so
%attr(755,root,root) %{_libdir}/kde4/konq_aboutpage.so
%attr(755,root,root) %{_libdir}/kde4/libnsplugin.so
%attr(755,root,root) %{_libdir}/libkdeinit4_konqueror.so
%{_desktopdir}/kde4/konqbrowser.desktop
%{_desktopdir}/kde4/konquerorsu.desktop
%{_datadir}/apps/kconf_update/konqsidebartng.upd
%{_datadir}/apps/kconf_update/move_konqsidebartng_entries.sh
%{_datadir}/apps/kbookmark
%{_datadir}/apps/kcmcss
%{_datadir}/apps/keditbookmarks
%{_datadir}/apps/konqiconview
%{_datadir}/apps/konqlistview
%{_datadir}/apps/konqueror/about
%{_datadir}/apps/konqueror/icons
%{_datadir}/apps/konqueror/pics
%{_datadir}/apps/konqueror/profiles
%dir %{_datadir}/apps/konqueror
%{_datadir}/apps/konqueror/konqueror.rc
%dir %{_datadir}/apps/plugin
%{_datadir}/apps/plugin/nspluginpart.rc
%{_datadir}/apps/konqueror/konq-filemanagement.rc
%{_datadir}/apps/konqueror/konq-webbrowsing.rc
%{_datadir}/kde4/servicetypes/findpart.desktop
%{_datadir}/kde4/servicetypes/konqaboutpage.desktop
%{_datadir}/kde4/servicetypes/konqpopupmenuplugin.desktop
%{_datadir}/kde4/servicetypes/terminalemulator.desktop
%{_datadir}/kde4/servicetypes/uasprovider.desktop
%{_datadir}/kde4/services/useragentstrings
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
%{_datadir}/autostart/konqy_preload.desktop
%{_datadir}/config/konqsidebartng.rc
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
%{_datadir}/apps/konqsidebartng
%{_kdedocdir}/en/konqueror
# testing
%attr(755,root,root) %{_libdir}/kde4/konq_sidebar.so
%attr(755,root,root) %{_libdir}/kde4/konq_sidebartree_bookmarks.so
%attr(755,root,root) %{_libdir}/kde4/konq_sidebartree_dirtree.so
%attr(755,root,root) %{_libdir}/kde4/konq_sidebartree_history.so
%attr(755,root,root) %{_libdir}/kde4/konq_sound.so
%attr(755,root,root) %{_libdir}/kde4/konqsidebar_tree.so
%attr(755,root,root) %{_libdir}/kde4/konqsidebar_web.so
%attr(755,root,root) %{_libdir}/kde4/konq_remoteencoding.so
%attr(755,root,root) %{_libdir}/kde4/konq_shellcmdplugin.so


%files -n konqueror-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkonq.so.*
%attr(755,root,root) %{_libdir}/libkonqsidebarplugin.so.*
%attr(755,root,root) %{_libdir}/libkonquerorprivate.so.*
%attr(755,root,root) %{_libdir}/libkdeinit4_keditbookmarks.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kfmclient.so
