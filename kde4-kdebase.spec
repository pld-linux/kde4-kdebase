# TODO:
# - check BR list
# - more file moves between packages; what's with dozen of messy -core/-common/-common* packages?
# - Req, Obsolets and Conflicts for every package
# - new descriptions
#
%define		_state		stable
%define		orgname		kdebase
%define		qtver		4.6.2

Summary:	K Desktop Environment - core files
Summary(es.UTF-8):	K Desktop Environment - archivos básicos
Summary(ja.UTF-8):	KDEデスクトップ環境 - 基本ファイル
Summary(ko.UTF-8):	KDE - 기본 파일
Summary(pl.UTF-8):	K Desktop Environment - pliki środowiska
Summary(pt_BR.UTF-8):	K Desktop Environment - arquivos básicos
Summary(ru.UTF-8):	K Desktop Environment - базовые файлы
Summary(uk.UTF-8):	K Desktop Environment - базові файли
Summary(zh_CN.UTF-8):	KDE核心
Name:		kde4-kdebase
Version:	4.4.3
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	034eaeaafc1fb0c48fc54336283891ce
Patch100:	%{name}-branch.diff
Patch0:		%{name}-wordchars.patch
URL:		http://www.kde.org/
BuildRequires:	OpenEXR-devel >= 1.2.2
BuildRequires:	OpenGL-devel
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	audiofile-devel
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	bzip2-devel
BuildRequires:	cdparanoia-III-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	cups-devel
BuildRequires:	cyrus-sasl-devel
BuildRequires:	db-devel
#BuildRequires:	dbus-qt-devel >= 0.70
BuildRequires:	gettext-devel
BuildRequires:	hal-devel
BuildRequires:	jasper-devel
BuildRequires:	kde4-kdebase-workspace-devel >= %{version}
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
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
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel >= 0.9.7c
BuildRequires:	pam-devel
BuildRequires:	pciutils-devel
BuildRequires:	pkgconfig
BuildRequires:	qimageblitz-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	samba-devel
BuildRequires:	shared-desktop-ontologies-devel >= 0.2
BuildRequires:	soprano-devel
BuildRequires:	strigi-devel
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-lib-libXScrnSaver-devel
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
Provides:	kde4-kdebase-common
Provides:	kde4-kdebase-core
Obsoletes:	kde4-kdebase-common
Obsoletes:	kde4-kdebase-core
Obsoletes:	kdebase4
Conflicts:	kdebase4
Conflicts:	kdelibs < 9:3.1.94.040110-1
# TODO: sensors
#BuildRequires:	sensors-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains KDE base system which includes:
- KDE Control Centre with modules
- KDesktop (a desktop) and Kicker (a panel)
- KWin window manager and several decorations
- KDE splash themes and plugins
- thumbnail creation, mail, news and terminal emulation support
- many more.

%description -l ja.UTF-8
KDEデスクトップ環境用の基本アプリケーション〄1�7以下のようなパッケージが入っています〄1�7
%description -l pl.UTF-8
Ten pakiet zawiera podstawowe aplikacje KDE:
- Centrum sterowania z modułami
- KDesktop (pulpit) i Kicker (panel)
- menedżer okien Kwin i dekoracje
- ekrany startowe KDE
- obsługę podglądu plików, protokołów poczty i news oraz emulacji
  terminala

%description -l ru.UTF-8
Базовые программы для K Desktop Environment. Включены: kwin (оконный
менеджер), konqueror (файловый менеджер, web-браузер, ftp-клиент,
...), konsole (замена xterm), kicker (запускалка программ и пейджер
рабочего стола), kaudio (аудиосервер), kdehelp (программа для
просмотра справочных файлов kde, файлов info и man), kthememgr
(система для управления альтернативными пакетами тем) и другие
компоненты KDE (kcheckpass, kikbd, kscreensaver, kcontrol, kfind,
kfontmanager, kmenuedit, kappfinder).

%description -l uk.UTF-8
Базові програми для K Desktop Environment. Включені: kwin (віконный
менеджер), konqueror (файловий менеджер, web-браузер, ftp-кліент,
...), konsole (заміна xterm), kicker (запускалка програм та пейджер
робочого столу), kaudio (аудіосервер), kdehelp (програма для перегляду
файлів довідки kde, файлів info та man), kthememgr (система для
керування альтернативними пакетами тем) та інші компоненти KDE
(kcheckpass, kikbd, kscreensaver, kcontrol, kfind, kfontmanager,
kmenuedit, kappfinder).

%package devel
Summary:	Include files to develop KDE applications
Summary(pl.UTF-8):	Pliki nagłówkowe potrzebne do tworzenia aplikacji KDE
Summary(pt_BR.UTF-8):	Arquivos de inclusão para compilar aplicativos que usem bibliotecas do kdebase
Group:		X11/Development/Libraries
Requires:	kde4-dolphin
Requires:	kde4-kdelibs-devel >= %{version}
Requires:	kde4-konqueror-libs

%description devel
This package contains header files needed to develop KDE applications.

%description devel -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe niezbędne do programowania aplikacji
KDE.

%description devel -l pt_BR.UTF-8
Este pacote contém os arquivos de inclusão que são necessários para
compilar aplicativos que usem bibliotecas do kdebase.

%package infocenter
Summary:	KDE Info Center
Summary(pl.UTF-8):	Centrum informacji o systemie dla KDE
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
#Requires:	pciutils
Obsoletes:	kde4-kdebase-workspace-infocenter

%description infocenter
Application for displaying information about your system.

%description infocenter -l pl.UTF-8
Centrum informacji o systemie dla KDE.

%package kappfinder
Summary:	Menu Updating Tool
Summary(pl.UTF-8):	Narzędzie do aktualizacji menu
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
Summary(pl.UTF-8):	Wersja KDE dialogu
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
Summary(pl.UTF-8):	Narzędzie do wyszukiwania plików dla KDE
Group:		X11/Applications
Requires:	kde4-konqueror-libs = %{version}-%{release}

%description kfind
A tool for find files for KDE.

%description kfind -l pl.UTF-8
Narzędzie do wyszukiwania plików dla KDE.

%package konsole
Summary:	KDE Terminal Emulator
Summary(pl.UTF-8):	Emulator terminala dla KDE
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	fontpostinst
Provides:	%{name}-common-konsole
Obsoletes:	kde4-kdebase-common-konsole

%description konsole
KDE Terminal Emulator.

%description konsole -l pl.UTF-8
Emulator terminala dla KDE.

%package kwrite
Summary:	KDE Text Editor
Summary(pl.UTF-8):	Edytor tekstu dla KDE
Group:		X11/Applications/Editors
Requires:	%{name} = %{version}-%{release}

%description kwrite
KWrite is a simple texteditor, with syntaxhighlighting, codefolding,
dynamic word wrap and more, it's the lightweight version of Kate,
providing more speed for minor tasks.

%description kwrite -l pl.UTF-8
KWrite to prosty edytor tekstu z podświetlaniem składni, zwijaniem
kodu, dynamicznym zawijaniem wierszy itp. Jest lżejszą wersją Kate,
szybszą dla mniejszych zadań.

%package useraccount
Summary:	User Account management
Summary(pl.UTF-8):	Zarządzanie kontem użytkownika
Group:		X11/Applications

%description useraccount
useraccount changes user account information. This module contains
kdepasswd program functionality.

%description useraccount -l pl.UTF-8
useraccount zmienia informacje o koncie użytkownika. Ten moduł zawiera
funkcjonalność programu kdepasswd.

%package -n kde4-dolphin
Summary:	Dolphin - KDE 4 file manager
Summary(pl.UTF-8):	Dolphin - zarządca plików KDE 4
Group:		X11/Applications
Requires:	kde4-konqueror-libs = %{version}-%{release}
Suggests:	eject
Obsoletes:	dolphin

%description -n kde4-dolphin
Dolphin - KDE 4 file manager.

%description -n kde4-dolphin -l pl.UTF-8
Dolphin - zarządca plików KDE 4.

%package -n kde4-konqueror
Summary:	Konqueror - web browser and file manager
Summary(pl.UTF-8):	Konqueror - przeglądarka WWW i zarządca plików
Group:		X11/Applications
Requires:	browser-plugins
Requires:	kde-common-dirs >= 0.5
Requires:	kde4-konqueror-libs = %{version}-%{release}
Provides:	wwwbrowser
Obsoletes:	konqueror < 9:3.0.0
Obsoletes:	konqueror >= 4.0.0

%description -n kde4-konqueror
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

%description -n kde4-konqueror -l pl.UTF-8
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

%package -n kde4-konqueror-libs
Summary:	konqueror shared libraries
Summary(pl.UTF-8):	Biblioteki współdzielone konquerora
Group:		X11/Libraries
Requires(post,postun):	/sbin/ldconfig
Requires:	kde4-kdelibs >= %{version}
Obsoletes:	konqueror-libs < 9:3.0.0
Obsoletes:	konqueror-libs >= 4.0.0

%description -n kde4-konqueror-libs
Konqueror shared libraries.

%description -n kde4-konqueror-libs -l pl.UTF-8
Biblioteki współdzielone konquerora.

%prep
%setup -q -n %{orgname}-%{version}
#%patch100 -p0
%patch0 -p1

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
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
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

%find_lang kinfocenter --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post konsole
%{_bindir}/fontpostinst misc

%postun konsole
%{_bindir}/fontpostinst misc

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post -n kde4-konqueror
%update_browser_plugins

%postun -n kde4-konqueror
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

%post	-n kde4-konqueror-libs	-p /sbin/ldconfig
%postun	-n kde4-konqueror-libs	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbookmarkmerger
%attr(755,root,root) %{_bindir}/servicemenudeinstallation
%attr(755,root,root) %{_bindir}/servicemenuinstallation
%attr(755,root,root) %{_libdir}/kde4/libkcminit_nsplugins.so
%attr(755,root,root) %{_libdir}/kde4/khtmlkttsdplugin.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_folderview.so
%{_datadir}/kde4/services/plasma-applet-folderview.desktop
%dir %{_datadir}/apps/kcontrol
%dir %{_datadir}/apps/kcontrol/pics
%{_datadir}/apps/kcontrol/pics/onlyone.png
%{_datadir}/apps/kcontrol/pics/overlapping.png
%{_datadir}/apps/khtml/kpartplugins/khtmlkttsd.desktop
%{_datadir}/apps/khtml/kpartplugins/khtmlkttsd.rc
%{_datadir}/apps/kconf_update/favicons.upd
%{_datadir}/apps/kconf_update/kfmclient_3_2.upd
%{_datadir}/apps/kconf_update/kfmclient_3_2_update.sh
%{_datadir}/apps/kconf_update/move_favicons.sh
%{_datadir}/templates
%{_desktopdir}/kde4/Home.desktop
%{_desktopdir}/kde4/kfmclient.desktop
%{_desktopdir}/kde4/kfmclient_dir.desktop
%{_desktopdir}/kde4/kfmclient_html.desktop
%{_desktopdir}/kde4/kfmclient_war.desktop
%exclude %{_iconsdir}/*/scalable
%{_iconsdir}/*/*/apps/*.png
%{_iconsdir}/*/*/apps/*.svgz
%{_mandir}/man1/kbookmarkmerger.1.*

# view svn plugin - where to put??
%attr(755,root,root) %{_libdir}/kde4/fileviewsvnplugin.so
%{_datadir}/kde4/services/fileviewsvnplugin.desktop
%{_datadir}/config/servicemenu.knsrc
%{_datadir}/kde4/servicetypes/fileviewversioncontrolplugin.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdolphinprivate.so
%attr(755,root,root) %{_libdir}/libkonq.so
%attr(755,root,root) %{_libdir}/libkonqsidebarplugin.so
%attr(755,root,root) %{_libdir}/libkonquerorprivate.so
%{_includedir}/*.h

%files infocenter -f kinfocenter.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kinfocenter
%attr(755,root,root) %{_libdir}/libkdeinit4_kinfocenter.so
%attr(755,root,root) %{_libdir}/kde4/kcm_usb.so
%attr(755,root,root) %{_libdir}/kde4/kcm_nic.so
%attr(755,root,root) %{_libdir}/kde4/kcm_info.so
%attr(755,root,root) %{_libdir}/kde4/kcm_opengl.so
%attr(755,root,root) %{_libdir}/kde4/kcm_solidproc.so
%attr(755,root,root) %{_libdir}/kde4/kcm_ioslaveinfo.so
%attr(755,root,root) %{_libdir}/kde4/kcm_memory.so
%attr(755,root,root) %{_libdir}/kde4/kcm_pci.so
%attr(755,root,root) %{_libdir}/kde4/kcm_samba.so
%attr(755,root,root) %{_libdir}/kde4/kcm_partition.so
%{_datadir}/apps/kinfocenter
%{_datadir}/kde4/services/kcmview1394.desktop
%{_datadir}/kde4/services/kcmusb.desktop
%{_datadir}/kde4/services/nic.desktop
%{_datadir}/kde4/services/opengl.desktop
%{_datadir}/kde4/services/kcm_partition.desktop
%{_datadir}/kde4/services/scsi.desktop
%{_datadir}/kde4/services/sound.desktop
%{_datadir}/kde4/services/xserver.desktop
%{_datadir}/kde4/services/devices.desktop
%{_datadir}/kde4/services/dma.desktop
%{_datadir}/kde4/services/interrupts.desktop
%{_datadir}/kde4/services/ioports.desktop
%{_datadir}/kde4/services/kcmsolidproc.desktop
%{_datadir}/kde4/services/ioslaveinfo.desktop
%{_datadir}/kde4/services/kcm_memory.desktop
%{_datadir}/kde4/services/kcm_pci.desktop
%{_datadir}/kde4/services/smbstatus.desktop
%{_desktopdir}/kde4/kinfocenter.desktop
%dir %{_datadir}/apps/kcmview1394
%dir %{_datadir}/apps/kcmusb
%{_datadir}/apps/kcmview1394/oui.db
%{_datadir}/apps/kcmusb/usb.ids

%files kappfinder
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kappfinder
%{_datadir}/apps/kappfinder
%{_desktopdir}/kde4/kappfinder.desktop
%{_iconsdir}/*/*/apps/kappfinder.png
%{_mandir}/man1/kappfinder.1.*

%files kdialog
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdialog
%{_datadir}/dbus-1/interfaces/org.kde.kdialog.ProgressDialog.xml

%files kfind
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfind
%attr(755,root,root) %{_libdir}/kde4/libkfindpart.so
%{_desktopdir}/kde4/kfind.desktop
%{_datadir}/kde4/services/kfindpart.desktop
%{_kdedocdir}/en/kfind
%{_mandir}/man1/kfind.1.*

%files konsole
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konsole
%attr(755,root,root) %{_bindir}/konsoleprofile
%attr(755,root,root) %{_libdir}/libkdeinit4_konsole.so
%attr(755,root,root) %{_libdir}/kde4/libkonsolepart.so
%attr(755,root,root) %{_libdir}/libkonsoleprivate.so
%{_datadir}/kde4/services/ServiceMenus/konsolehere.desktop
%{_datadir}/kde4/services/konsolepart.desktop
%{_datadir}/apps/konsole
%{_desktopdir}/kde4/konsole.desktop
%{_kdedocdir}/en/konsole

%files kwrite
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwrite
%attr(755,root,root) %{_libdir}/libkdeinit4_kwrite.so
%{_datadir}/apps/kwrite
%{_desktopdir}/kde4/kwrite.desktop
%{_kdedocdir}/en/kwrite

%files useraccount
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdepasswd
%attr(755,root,root) %{_libdir}/kde4/kcm_useraccount.so
%dir %{_datadir}/apps/kdm
%dir %{_datadir}/apps/kdm/pics
%{_datadir}/apps/kdm/pics/users
%{_datadir}/config.kcfg/kcm_useraccount.kcfg
%{_datadir}/config.kcfg/kcm_useraccount_pass.kcfg
%{_datadir}/kde4/services/kcm_useraccount.desktop
%{_desktopdir}/kde4/kdepasswd.desktop
%{_kdedocdir}/en/kdepasswd

%files -n kde4-dolphin
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dolphin
%attr(755,root,root) %{_libdir}/libdolphinprivate.so.*
%attr(755,root,root) %{_libdir}/kde4/kcm_dolphingeneral.so
%attr(755,root,root) %{_libdir}/kde4/kcm_dolphinnavigation.so
%attr(755,root,root) %{_libdir}/kde4/kcm_dolphinservices.so
%attr(755,root,root) %{_libdir}/kde4/kcm_dolphinviewmodes.so
%attr(755,root,root) %{_libdir}/kde4/dolphinpart.so
%dir %{_datadir}/apps/dolphin
%{_datadir}/apps/dolphin/dolphinsearchcommands.desktop
%{_datadir}/apps/dolphin/dolphinui.rc
%dir %{_datadir}/apps/dolphinpart
%{_datadir}/apps/dolphinpart/dolphinpart.rc
%{_datadir}/config.kcfg/dolphin_columnmodesettings.kcfg
%{_datadir}/config.kcfg/dolphin_versioncontrolsettings.kcfg
%{_datadir}/config.kcfg/dolphin_detailsmodesettings.kcfg
%{_datadir}/config.kcfg/dolphin_directoryviewpropertysettings.kcfg
%{_datadir}/config.kcfg/dolphin_generalsettings.kcfg
%{_datadir}/config.kcfg/dolphin_iconsmodesettings.kcfg
%{_datadir}/config.kcfg/keditbookmarks.kcfg
%{_datadir}/kde4/services/dolphinpart.desktop
%{_datadir}/kde4/services/kcmdolphingeneral.desktop
%{_datadir}/kde4/services/kcmdolphinnavigation.desktop
%{_datadir}/kde4/services/kcmdolphinservices.desktop
%{_datadir}/kde4/services/kcmdolphinviewmodes.desktop
%{_desktopdir}/kde4/dolphin.desktop
%{_kdedocdir}/en/dolphin
%dir %{_datadir}/apps/dolphinpart/kpartplugins
%{_datadir}/apps/dolphinpart/kpartplugins/kshellcmdplugin.desktop
%{_datadir}/apps/dolphinpart/kpartplugins/kshellcmdplugin.rc

%files -n kde4-konqueror
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/keditbookmarks
%attr(755,root,root) %{_bindir}/kfmclient
%attr(755,root,root) %{_bindir}/konqueror
%attr(755,root,root) %{_bindir}/nspluginscan
%attr(755,root,root) %{_bindir}/nspluginviewer
%attr(755,root,root) %{_libdir}/libkdeinit4_konqueror.so
%attr(755,root,root) %{_libdir}/kde4/kcm_history.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kio.so
%attr(755,root,root) %{_libdir}/kde4/kcm_konq.so
%attr(755,root,root) %{_libdir}/kde4/kcm_konqhtml.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kurifilt.so
%attr(755,root,root) %{_libdir}/kde4/kcm_performance.so
%attr(755,root,root) %{_libdir}/kde4/kcm_view1394.so
%attr(755,root,root) %{_libdir}/kde4/kded_favicons.so
%attr(755,root,root) %{_libdir}/kde4/kded_konqy_preloader.so
%attr(755,root,root) %{_libdir}/kde4/konq_aboutpage.so
%attr(755,root,root) %{_libdir}/kde4/libnsplugin.so
%{_datadir}/apps/kbookmark
%{_datadir}/apps/kcmcss
%{_datadir}/apps/keditbookmarks
%{_datadir}/apps/konqueror/about
%{_datadir}/apps/konqueror/pics
%{_datadir}/apps/konqueror/profiles
%{_datadir}/apps/konqueror/konqueror.rc
%{_datadir}/apps/konqsidebartng
%dir %{_datadir}/apps/plugin
%{_datadir}/apps/plugin/nspluginpart.rc
%{_datadir}/autostart/konqy_preload.desktop
%{_datadir}/config/konqsidebartngrc
%{_datadir}/config.kcfg/konqueror.kcfg
%{_datadir}/kde4/servicetypes/findpart.desktop
%{_datadir}/kde4/servicetypes/konqaboutpage.desktop
%{_datadir}/kde4/servicetypes/konqpopupmenuplugin.desktop
%{_datadir}/kde4/servicetypes/konqdndpopupmenuplugin.desktop
%{_datadir}/kde4/servicetypes/terminalemulator.desktop
%{_datadir}/kde4/servicetypes/uasprovider.desktop
%{_datadir}/kde4/services/useragentstrings
%{_datadir}/kde4/services/bookmarks.desktop
%{_datadir}/kde4/services/cache.desktop
%{_datadir}/kde4/services/cookies.desktop
%{_datadir}/kde4/services/desktoppath.desktop
%{_datadir}/kde4/services/ebrowsing.desktop
%{_datadir}/kde4/services/filebehavior.desktop
%{_datadir}/kde4/services/kcmhistory.desktop
%{_datadir}/kde4/services/kcmkonqyperformance.desktop
%{_datadir}/kde4/services/kcmperformance.desktop
%{_datadir}/kde4/services/kded/favicons.desktop
%{_datadir}/kde4/services/kded/konqy_preloader.desktop
%{_datadir}/kde4/services/khtml_appearance.desktop
%{_datadir}/kde4/services/khtml_behavior.desktop
%{_datadir}/kde4/services/khtml_filter.desktop
%{_datadir}/kde4/services/khtml_general.desktop
%{_datadir}/kde4/services/khtml_java_js.desktop
%{_datadir}/kde4/services/khtml_plugins.desktop
%{_datadir}/kde4/services/konq_aboutpage.desktop
%{_datadir}/kde4/services/konq_sidebartng.desktop
%{_datadir}/kde4/services/konqueror.desktop
#%{_datadir}/kde4/services/lanbrowser.desktop
%{_datadir}/kde4/services/netpref.desktop
%{_datadir}/kde4/services/proxy.desktop
%{_datadir}/kde4/services/smb.desktop
%{_datadir}/kde4/services/useragent.desktop
%{_datadir}/dbus-1/interfaces/org.kde.FavIcon.xml
%{_datadir}/dbus-1/interfaces/org.kde.Konqueror.Main.xml
%{_datadir}/dbus-1/interfaces/org.kde.Konqueror.MainWindow.xml
%{_datadir}/dbus-1/interfaces/org.kde.konqueror.Preloader.xml
%{_datadir}/dbus-1/interfaces/org.kde.nsplugins.CallBack.xml
%{_datadir}/dbus-1/interfaces/org.kde.nsplugins.class.xml
%{_datadir}/dbus-1/interfaces/org.kde.nsplugins.instance.xml
%{_datadir}/dbus-1/interfaces/org.kde.nsplugins.viewer.xml
%{_desktopdir}/kde4/konqbrowser.desktop
%{_desktopdir}/kde4/konquerorsu.desktop
%{_iconsdir}/*/*/apps/konqueror.*
%{_kdedocdir}/en/konqueror
# testing
%attr(755,root,root) %{_libdir}/kde4/konq_sidebar.so
%attr(755,root,root) %{_libdir}/kde4/konq_sidebartree_bookmarks.so
%attr(755,root,root) %{_libdir}/kde4/konq_sidebartree_dirtree.so
%attr(755,root,root) %{_libdir}/kde4/konq_sound.so
%attr(755,root,root) %{_libdir}/kde4/konqsidebar_history.so
%attr(755,root,root) %{_libdir}/kde4/konqsidebar_tree.so
%attr(755,root,root) %{_libdir}/kde4/konqsidebar_web.so
%attr(755,root,root) %{_libdir}/kde4/konq_shellcmdplugin.so

%files -n kde4-konqueror-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkonq.so.*
%attr(755,root,root) %{_libdir}/libkonqsidebarplugin.so.*
%attr(755,root,root) %{_libdir}/libkonquerorprivate.so.*
%attr(755,root,root) %{_libdir}/libkdeinit4_keditbookmarks.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kfmclient.so
