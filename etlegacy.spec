Summary:	Fully compatible client and server for Wolfenstein: Enemy Territory
Name:		etlegacy
Version:	2.78.0
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
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(glew)

%description
ET: Legacy is based on the source code of Wolfenstein: Enemy Territory
which was released under the GPLv3 license. The main goal of this project
is to fix bugs, remove old dependencies and make it playable on all major
operating systems while still remaining compatible with the ET 2.60b 
version and as many of its mods as possible...

%prep
%autosetup -p1

%build
%cmake \
%ifarch %{armx}
		-DARM=ON \
		-DFEATURE_RENDERER_GLES=ON \
%endif
		-DCROSS_COMPILE32=OFF \
		-DBUNDLED_LIBS=OFF \
		-DCLIENT_GLVND=ON \
		-DINSTALL_DEFAULT_BINDIR=%{_gamesbindir} \
		-DINSTALL_DEFAULT_BASEDIR=%{_gamesdatadir}/%{name} \
		-DINSTALL_DEFAULT_MODDIR=%{_gamesdatadir}/%{name}


%make_build

%install
%make_install -C build

%files
%doc README.md
%dir %{_gamesdatadir}/%{name}
%{_gamesbindir}/etl
%{_gamesbindir}/etlded
%{_gamesdatadir}/%{name}/*
