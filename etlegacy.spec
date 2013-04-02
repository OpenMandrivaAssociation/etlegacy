%define snapshot 20130402

Summary:	Fully compatible client and server for Wolfenstein: Enemy Territory
Name:		etlegacy
Version:	2.71
Release:	0.rc1.1
License:	GPL3
Group:		Games/Other
Url:		http://www.etlegacy.com/
# (tpg) prepare git snapshot
# rm -rf etlegacy && git clone git://github.com/etlegacy/etlegacy.git && cd etlegacy/
# git archive --prefix=etlegacy-$(date +%Y%m%d)/ --format=tar HEAD | xz > ../etlegacy-$(date +%Y%m%d).tar.xz
#
Source0:	%{name}-%{snapshot}.tar.xz
BuildRequires:	cmake

%description
ET: Legacy is based on the source code of Wolfenstein: Enemy Territory
which was released under the GPLv3 license. The main goal of this project
is to fix bugs, remove old dependencies and make it playable on all major
operating systems while still remaining compatible with the ET 2.60b 
version and as many of its mods as possible...

%prep
%setup -q

%build
%cmake

%make

%install
%makeinstall_std

%files
%doc README.md