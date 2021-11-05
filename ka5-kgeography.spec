%define		kdeappsver	21.08.3
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kgeography
Summary:	kgeography
Name:		ka5-%{kaname}
Version:	21.08.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	5dcc1cf23e1d0779e3d154bf1ec0cfa6
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kitemviews-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{name}-data = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KGeography is a geography learning tool, which allows you to learn
about the political divisions of some countries (divisions, capitals
of those divisions and their associated flags if there are some).

%description -l pl.UTF-8
KGeography to narzędzi do nauki geografii, które pozwala uczyć się
o podziałach administracyjnych różnych krajów, ich stolicach i flagach.

%package data
Summary:	Data files for %{kaname}
Summary(pl.UTF-8):	Dane dla %{kaname}
Group:		X11/Applications
BuildArch:	noarch

%description data
Data files for %{kaname}.

%description data -l pl.UTF-8
Dane dla %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kgeography

%files data -f %{kaname}.lang
%defattr(644,root,root,755)
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
