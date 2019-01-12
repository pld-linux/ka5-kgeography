%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		kgeography
Summary:	kgeography
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	ed1b56249adbdd3b76fc80adb54861bc
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-kconfigwidgets-devel >= 5.15
BuildRequires:	kf5-kcoreaddons-devel >= 5.15
BuildRequires:	kf5-kcrash-devel >= 5.15
BuildRequires:	kf5-kdoctools-devel >= 5.15
BuildRequires:	kf5-ki18n-devel >= 5.15
BuildRequires:	kf5-kiconthemes-devel >= 5.15
BuildRequires:	kf5-kitemviews-devel >= 5.15
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.15
BuildRequires:	kf5-kxmlgui-devel >= 5.15
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KGeography is a geography learning tool, which allows you to learn
about the political divisions of some countries (divisions, capitals
of those divisions and their associated flags if there are some).

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kgeography
%{_desktopdir}/org.kde.kgeography.desktop
%{_datadir}/config.kcfg/kgeography.kcfg
%{_iconsdir}/hicolor/128x128/apps/kgeography.png
%{_iconsdir}/hicolor/16x16/apps/kgeography.png
%{_iconsdir}/hicolor/22x22/apps/kgeography.png
%{_iconsdir}/hicolor/32x32/apps/kgeography.png
%{_iconsdir}/hicolor/48x48/apps/kgeography.png
%{_iconsdir}/hicolor/64x64/apps/kgeography.png
%{_iconsdir}/hicolor/scalable/apps/kgeography.svgz
%{_datadir}/kgeography
%{_datadir}/kxmlgui5/kgeography
#%{_localedir}/fi/LC_SCRIPTS/kgeography/kgeography.js
#%{_localedir}/fi/LC_SCRIPTS/kgeography/kgeography.pmap
#%{_localedir}/fi/LC_SCRIPTS/kgeography/kgeography.pmapc
#%{_localedir}/fr/LC_SCRIPTS/kgeography/kgeography.js
#%{_localedir}/ja/LC_SCRIPTS/kgeography/kgeography.js
#%{_localedir}/pl/LC_SCRIPTS/kgeography/general.pmap
#%{_localedir}/pl/LC_SCRIPTS/kgeography/general.pmapc
#%{_localedir}/pl/LC_SCRIPTS/kgeography/kgeography.js
#%{_localedir}/uk/LC_SCRIPTS/kgeography/general.pmap
#%{_localedir}/uk/LC_SCRIPTS/kgeography/general.pmapc
#%{_localedir}/uk/LC_SCRIPTS/kgeography/kgeography.js
%{_datadir}/metainfo/org.kde.kgeography.appdata.xml
