Summary:	Fully compatible client and server for Wolfenstein: Enemy Territory
Name:		etlegacy
Version:	2.81.1
Release:	1
License:	GPL3
Group:		Games/Other
Url:		http://www.etlegacy.com/
Source0:	https://github.com/etlegacy/etlegacy/archive/refs/tags/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(libcjson)
BuildRequires:	pkgconfig(minizip)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(ogg)
Requires:	shared-mime-info

%description
ET: Legacy is based on the source code of Wolfenstein: Enemy Territory
which was released under the GPLv3 license. The main goal of this project
is to fix bugs, remove old dependencies and make it playable on all major
operating systems while still remaining compatible with the ET 2.60b 
version and as many of its mods as possible...

%prep
%autosetup -p1

# Use system flags for all products
sed -e 's,^\s*SET(CMAKE_BUILD_TYPE "Release"),# &,' -i cmake/ETLCommon.cmake

%build
%cmake \
	-DBUNDLED_LIBS=OFF \
	-DCROSS_COMPILE32=OFF \
	-DBUILD_MOD=ON \
	-DCLIENT_GLVND=ON \
	-DFEATURE_RENDERER2=OFF \
	-DFEATURE_AUTOUPDATE=OFF \
	-DINSTALL_EXTRA=OFF \
	-DINSTALL_DEFAULT_BINDIR=%{_gamesbindir} \
	-DINSTALL_DEFAULT_BASEDIR=%{_gamesdatadir}/%{name} \
	-DINSTALL_DEFAULT_MODDIR=%{_gamesdatadir}/%{name}

%make_build

%install
%make_install -C build

%files
%license %{_datadir}/licenses/etlegacy/COPYING.txt
%doc %{_docdir}/%{name}
%dir %{_gamesdatadir}/%{name}
%{_gamesbindir}/etl*
%{_gamesdatadir}/%{name}/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/scalable/apps/*.svg
%doc %{_mandir}/man6/etl*.6*
%{_datadir}/metainfo/*.xml
%{_datadir}/mime/packages/*.xml
