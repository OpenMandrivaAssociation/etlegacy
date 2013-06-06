%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define snapshot 20130606

Summary:	Fully compatible client and server for Wolfenstein: Enemy Territory
Name:		etlegacy
Version:	2.71
Release:	0.rc1.2
License:	GPL3
Group:		Games/Other
Url:		http://www.etlegacy.com/
# (tpg) prepare git snapshot
# rm -rf etlegacy && git clone git://github.com/etlegacy/etlegacy.git && cd etlegacy/
# git archive --prefix=etlegacy-$(date +%Y%m%d)/ --format=tar HEAD | xz > ../etlegacy-$(date +%Y%m%d).tar.xz
#
Source0:	%{name}-%{snapshot}.tar.xz
BuildRequires:	cmake
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(sdl)


%description
ET: Legacy is based on the source code of Wolfenstein: Enemy Territory
which was released under the GPLv3 license. The main goal of this project
is to fix bugs, remove old dependencies and make it playable on all major
operating systems while still remaining compatible with the ET 2.60b 
version and as many of its mods as possible...

%prep
%setup -qn %{name}-%{snapshot}

%build
%cmake \
	-DINSTALL_DEFAULT_BINDIR=%{_gamesbindir} \
	-DINSTALL_DEFAULT_BASEDIR=%{_gamesdatadir}/%{name} \
        -DINSTALL_DEFAULT_MODDIR=%{_gamesdatadir}/%{name} \
	-DCMAKE_BUILD_TYPE="Release" \
        -DBUILD_SERVER=1 \
        -DBUILD_CLIENT=1 \
        -DBUILD_MOD=1 \
        -DBUILD_PAK3_PK3=1 \
        -DBUNDLED_LIBS=0 \
        -DBUNDLED_SDL=0 \
        -DBUNDLED_CURL=0 \
        -DBUNDLED_JPEG=0 \
        -DBUNDLED_LUA=0 \
        -DBUNDLED_OGG_VORBIS=0 \
        -DCROSS_COMPILE32=0 \
        -DFEATURE_CURL=1 \
        -DFEATURE_OGG_VORBIS=1 \
        -DFEATURE_OPENAL=1 \
        -DFEATURE_FREETYPE=1 \
        -DFEATURE_TRACKER=1 \
        -DFEATURE_LUA= \
        -DFEATURE_MULTIVIEW=0 \
        -DFEATURE_ANTICHEAT=1 \
        -DFEATURE_CURSES=0 \
        -DFEATURE_AUTOUPDATE=1 \
        -DFEATURE_RENDERER2=0 \
        -DFEATURE_IPV6=0 \
        -DFEATURE_OMNIBOT=0 \
        -DINSTALL_OMNIBOT=0

%make

%install
%makeinstall_std -C build

%files
%doc README.md
%dir %{_gamesdatadir}/%{name}
%{_gamesbindir}/etl
%{_gamesbindir}/etlded
%{_gamesdatadir}/%{name}/*
