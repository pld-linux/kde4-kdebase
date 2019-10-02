# TODO:
# - new descriptions
#
%define		_state		stable
%define		orgname		kde-baseapps
%define		qtver		4.8.3
%define		kdeworkspacever	4.11.0

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
Version:	4.14.3
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	20ffb374b03bdab5ee761b272f839fea
Patch100:	%{name}-branch.diff
URL:		http://www.kde.org/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	cyrus-sasl-devel
BuildRequires:	db-devel
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	kde4-baloo-widgets-devel >= %{version}
BuildRequires:	kde4-kdebase-workspace-devel >= %{kdeworkspacever}
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-nepomuk-widgets-devel >= %{version}
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel >= 0.9.7c
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	shared-desktop-ontologies-devel >= 0.5
BuildRequires:	soprano-devel >= 2.4.64
BuildRequires:	strigi-devel >= 0.7.2
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildConflicts:	kdebase-konqueror-libs
Provides:	kde4-kdebase-common
Provides:	kde4-kdebase-core
Obsoletes:	kde4-kdebase-common
Obsoletes:	kde4-kdebase-core
Obsoletes:	kde4-kdebase-kappfinder
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
KDEデスクトップ環境用の基本アプリケーション。 以下のようなパッケージが入っています。

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
kfontmanager, kmenuedit).

%description -l uk.UTF-8
Базові програми для K Desktop Environment. Включені: kwin (віконный
менеджер), konqueror (файловий менеджер, web-браузер, ftp-кліент,
...), konsole (заміна xterm), kicker (запускалка програм та пейджер
робочого столу), kaudio (аудіосервер), kdehelp (програма для перегляду
файлів довідки kde, файлів info та man), kthememgr (система для
керування альтернативними пакетами тем) та інші компоненти KDE
(kcheckpass, kikbd, kscreensaver, kcontrol, kfind, kfontmanager,
kmenuedit).

%package devel
Summary:	Include files to develop KDE applications
Summary(pl.UTF-8):	Pliki nagłówkowe potrzebne do tworzenia aplikacji KDE
Summary(pt_BR.UTF-8):	Arquivos de inclusão para compilar aplicativos que usem bibliotecas do kdebase
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
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
Requires:	browser-plugins >= 2.0
Requires:	kde-common-dirs >= 0.5
Requires:	kde4-konqueror-libs = %{version}-%{release}
Provides:	wwwbrowser
Obsoletes:	konqueror < 9:3.0.0
Obsoletes:	konqueror >= 4.0.0
Obsoletes:	kde4-kdegraphics-kfile < 4.6.100-1

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

for f in $(find . -name '*.desktop'); do
	if grep -q '\[ven\]' $f; then
		sed -i -e 's/\[ven\]/[ve]/' $f
	fi
done

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d \
	$RPM_BUILD_ROOT%{_datadir}/apps/kcontrol \
	$RPM_BUILD_ROOT%{_libdir}/kde4/plugins/konqueror

%browser_plugins_add_browser konqueror -p %{_libdir}/kde4/plugins/konqueror

%clean
rm -rf $RPM_BUILD_ROOT

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
%{_datadir}/templates
%{_desktopdir}/kde4/Home.desktop
%{_desktopdir}/kde4/kfmclient.desktop
%{_desktopdir}/kde4/kfmclient_dir.desktop
%{_desktopdir}/kde4/kfmclient_html.desktop
%{_desktopdir}/kde4/kfmclient_war.desktop
%exclude %{_iconsdir}/*/scalable
%{_iconsdir}/*/*/apps/*.png
%exclude %{_iconsdir}/*/*/apps/konqueror.png
%{_iconsdir}/*/*/apps/*.svgz
%{_mandir}/man1/kbookmarkmerger.1.*

%{_datadir}/config/servicemenu.knsrc
%{_datadir}/kde4/servicetypes/fileviewversioncontrolplugin.desktop

#?
%{_datadir}/kde4/services/ServiceMenus

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkbookmarkmodel_private.so
%attr(755,root,root) %{_libdir}/libdolphinprivate.so
%attr(755,root,root) %{_libdir}/libkonq.so
%attr(755,root,root) %{_libdir}/libkonqsidebarplugin.so
%{_includedir}/*.h

%files kdialog
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdialog
%{_datadir}/dbus-1/interfaces/org.kde.kdialog.ProgressDialog.xml

%files kfind
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfind
%{_desktopdir}/kde4/kfind.desktop
%{_kdedocdir}/en/kfind
%{_mandir}/man1/kfind.1.*

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
%attr(755,root,root) %{_libdir}/libkdeinit4_dolphin.so
%attr(755,root,root) %{_libdir}/kde4/kcm_dolphingeneral.so
%attr(755,root,root) %{_libdir}/kde4/kcm_dolphinnavigation.so
%attr(755,root,root) %{_libdir}/kde4/kcm_dolphinservices.so
%attr(755,root,root) %{_libdir}/kde4/kcm_dolphinviewmodes.so
%attr(755,root,root) %{_libdir}/kde4/kio_filenamesearch.so
%attr(755,root,root) %{_libdir}/kde4/dolphinpart.so
%{_datadir}/appdata/dolphin.appdata.xml
%dir %{_datadir}/apps/dolphin
%{_datadir}/apps/dolphin/dolphinui.rc
%dir %{_datadir}/apps/dolphinpart
%{_datadir}/apps/dolphinpart/dolphinpart.rc
%dir %{_datadir}/apps/dolphinpart/kpartplugins
%{_datadir}/apps/dolphinpart/kpartplugins/dirfilterplugin.desktop
%{_datadir}/apps/dolphinpart/kpartplugins/dirfilterplugin.rc
%{_datadir}/apps/dolphinpart/kpartplugins/kimgalleryplugin.desktop
%{_datadir}/apps/dolphinpart/kpartplugins/kimgalleryplugin.rc
%{_datadir}/apps/dolphinpart/kpartplugins/kshellcmdplugin.desktop
%{_datadir}/apps/dolphinpart/kpartplugins/kshellcmdplugin.rc
%{_datadir}/config.kcfg/dolphin_compactmodesettings.kcfg
%{_datadir}/config.kcfg/dolphin_versioncontrolsettings.kcfg
%{_datadir}/config.kcfg/dolphin_detailsmodesettings.kcfg
%{_datadir}/config.kcfg/dolphin_directoryviewpropertysettings.kcfg
%{_datadir}/config.kcfg/dolphin_generalsettings.kcfg
%{_datadir}/config.kcfg/dolphin_iconsmodesettings.kcfg
%{_datadir}/kde4/services/dolphinpart.desktop
%{_datadir}/kde4/services/kcmdolphingeneral.desktop
%{_datadir}/kde4/services/kcmdolphinnavigation.desktop
%{_datadir}/kde4/services/kcmdolphinservices.desktop
%{_datadir}/kde4/services/kcmdolphinviewmodes.desktop
%{_datadir}/kde4/services/filenamesearch.protocol
%{_desktopdir}/kde4/dolphin.desktop
%{_kdedocdir}/en/dolphin

%files -n kde4-konqueror
%defattr(644,root,root,755)
%{_browserpluginsconfdir}/browsers.d/konqueror.*
%config(noreplace) %verify(not md5 mtime size) %{_browserpluginsconfdir}/blacklist.d/konqueror.*.blacklist
%attr(755,root,root) %{_bindir}/fsview
%attr(755,root,root) %{_bindir}/keditbookmarks
%attr(755,root,root) %{_bindir}/kfmclient
%attr(755,root,root) %{_bindir}/konqueror
%attr(755,root,root) %{_bindir}/nspluginscan
%attr(755,root,root) %{_bindir}/nspluginviewer
%attr(755,root,root) %{_libdir}/libkdeinit4_konqueror.so
%attr(755,root,root) %{_libdir}/kde4/adblock.so
%attr(755,root,root) %{_libdir}/kde4/akregatorkonqfeedicon.so
%attr(755,root,root) %{_libdir}/kde4/autorefresh.so
%attr(755,root,root) %{_libdir}/kde4/babelfishplugin.so
%attr(755,root,root) %{_libdir}/kde4/dirfilterplugin.so
%attr(755,root,root) %{_libdir}/kde4/domtreeviewerplugin.so
%attr(755,root,root) %{_libdir}/kde4/fsviewpart.so
%attr(755,root,root) %{_libdir}/kde4/kcm_history.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kio.so
%attr(755,root,root) %{_libdir}/kde4/kcm_konq.so
%attr(755,root,root) %{_libdir}/kde4/kcm_konqhtml.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kurifilt.so
%attr(755,root,root) %{_libdir}/kde4/kcm_performance.so
%attr(755,root,root) %{_libdir}/kde4/kded_favicons.so
%attr(755,root,root) %{_libdir}/kde4/kded_konqy_preloader.so
%attr(755,root,root) %{_libdir}/kde4/khtmlsettingsplugin.so
%attr(755,root,root) %{_libdir}/kde4/kimgallery.so
%attr(755,root,root) %{_libdir}/kde4/konq_aboutpage.so
%attr(755,root,root) %{_libdir}/kde4/konqsidebar_places.so
%attr(755,root,root) %{_libdir}/kde4/libnsplugin.so
%attr(755,root,root) %{_libdir}/kde4/minitoolsplugin.so
%attr(755,root,root) %{_libdir}/kde4/rellinksplugin.so
%attr(755,root,root) %{_libdir}/kde4/searchbarplugin.so
%attr(755,root,root) %{_libdir}/kde4/uachangerplugin.so
%attr(755,root,root) %{_libdir}/kde4/validatorsplugin.so
%attr(755,root,root) %{_libdir}/kde4/webarchiverplugin.so
%attr(755,root,root) %{_libdir}/kde4/webarchivethumbnail.so
%dir %{_libdir}/kde4/plugins/konqueror
%{_datadir}/apps//akregator/pics/feed.png
%{_datadir}/apps/domtreeviewer
%{_datadir}/apps/fsview
%{_datadir}/apps/nsplugin
%{_datadir}/apps/khtml/kpartplugins/akregator_konqfeedicon.desktop
%{_datadir}/apps/khtml/kpartplugins/akregator_konqfeedicon.rc
%{_datadir}/apps/khtml/kpartplugins/autorefresh.desktop
%{_datadir}/apps/khtml/kpartplugins/autorefresh.rc
%{_datadir}/apps/khtml/kpartplugins/khtmlsettingsplugin.desktop
%{_datadir}/apps/khtml/kpartplugins/khtmlsettingsplugin.rc
%{_datadir}/apps/khtml/kpartplugins/minitoolsplugin.desktop
%{_datadir}/apps/khtml/kpartplugins/minitoolsplugin.rc
%{_datadir}/apps/khtml/kpartplugins/plugin_adblock.desktop
%{_datadir}/apps/khtml/kpartplugins/plugin_adblock.rc
%{_datadir}/apps/khtml/kpartplugins/plugin_babelfish.rc
%{_datadir}/apps/khtml/kpartplugins/plugin_domtreeviewer.desktop
%{_datadir}/apps/khtml/kpartplugins/plugin_domtreeviewer.rc
%{_datadir}/apps/khtml/kpartplugins/plugin_rellinks.desktop
%{_datadir}/apps/khtml/kpartplugins/plugin_rellinks.rc
%{_datadir}/apps/khtml/kpartplugins/plugin_translator.desktop
%{_datadir}/apps/khtml/kpartplugins/plugin_validators.desktop
%{_datadir}/apps/khtml/kpartplugins/plugin_validators.rc
%{_datadir}/apps/khtml/kpartplugins/plugin_webarchiver.desktop
%{_datadir}/apps/khtml/kpartplugins/plugin_webarchiver.rc
%{_datadir}/apps/khtml/kpartplugins/uachangerplugin.desktop
%{_datadir}/apps/khtml/kpartplugins/uachangerplugin.rc
%{_datadir}/apps/kbookmark
%{_datadir}/apps/kcmcss
%{_datadir}/apps/keditbookmarks
%{_datadir}/apps/konqueror/about
%{_datadir}/apps/konqueror/icons
%{_datadir}/apps/konqueror/kpartplugins
%{_datadir}/apps/konqueror/opensearch
%{_datadir}/apps/konqueror/pics
%{_datadir}/apps/konqueror/profiles
%{_datadir}/apps/konqueror/konqueror.rc
%{_datadir}/apps/konqsidebartng
%{_datadir}/apps/kwebkitpart
%{_datadir}/autostart/konqy_preload.desktop
%{_datadir}/config/konqsidebartngrc
%{_datadir}/config/translaterc
%{_datadir}/config.kcfg/keditbookmarks.kcfg
%{_datadir}/config.kcfg/konqueror.kcfg
%{_datadir}/config.kcfg/validators.kcfg
%{_datadir}/kde4/servicetypes/konqaboutpage.desktop
%{_datadir}/kde4/servicetypes/konqpopupmenuplugin.desktop
%{_datadir}/kde4/servicetypes/konqdndpopupmenuplugin.desktop
%{_datadir}/kde4/servicetypes/uasprovider.desktop
%{_datadir}/kde4/services/useragentstrings
%{_datadir}/kde4/services/bookmarks.desktop
%{_datadir}/kde4/services/cache.desktop
%{_datadir}/kde4/services/cookies.desktop
%{_datadir}/kde4/services/ebrowsing.desktop
%{_datadir}/kde4/services/filebehavior.desktop
%{_datadir}/kde4/services/fsview_part.desktop
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
%{_datadir}/kde4/services/netpref.desktop
%{_datadir}/kde4/services/proxy.desktop
%{_datadir}/kde4/services/smb.desktop
%{_datadir}/kde4/services/useragent.desktop
%{_datadir}/kde4/services/webarchivethumbnail.desktop
%{_datadir}/dbus-1/interfaces/org.kde.FavIcon.xml
%{_datadir}/dbus-1/interfaces/org.kde.Konqueror.Main.xml
%{_datadir}/dbus-1/interfaces/org.kde.Konqueror.MainWindow.xml
%{_datadir}/dbus-1/interfaces/org.kde.konqueror.Preloader.xml
%{_datadir}/dbus-1/interfaces/org.kde.nsplugins.CallBack.xml
%{_datadir}/dbus-1/interfaces/org.kde.nsplugins.class.xml
%{_datadir}/dbus-1/interfaces/org.kde.nsplugins.instance.xml
%{_datadir}/dbus-1/interfaces/org.kde.nsplugins.viewer.xml
%{_desktopdir}/kde4/keditbookmarks.desktop
%{_desktopdir}/kde4/konqbrowser.desktop
%{_desktopdir}/kde4/konquerorsu.desktop
%{_iconsdir}/*/*/apps/konqueror.*
%{_iconsdir}/*/*/actions/babelfish.*
%{_iconsdir}/*/*/actions/cssvalidator.*
%{_iconsdir}/*/*/actions/htmlvalidator.*
%{_iconsdir}/*/*/actions/imagegallery.*
%{_iconsdir}/*/*/actions/validators.*
%{_iconsdir}/*/*/actions/webarchiver.*
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
%attr(755,root,root) %{_libdir}/libkbookmarkmodel_private.so.*
%attr(755,root,root) %{_libdir}/libkdeinit4_keditbookmarks.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kfmclient.so
