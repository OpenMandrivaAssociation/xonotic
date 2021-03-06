%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define		oname	Xonotic

Summary:	A free multi-player first person shooter
Name:		xonotic
Version:	0.8.2
Release:	1
Url:		http://www.xonotic.org/
Source0:	http://dl.xonotic.org/%{name}-%{version}.zip
License:	GPLv2+
Group:		Games/Arcade
Requires:	%{name}-data = %{version}
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(xxf86dga)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	jpeg-devel

%description
Xonotic is a free (GPL), fast-paced first-person shooter that works on 
Microsoft Windows, Mac OSX and Linux.

Xonotic is a direct successor of the Nexuiz Project.

It features much better quality graphics and visual effects.

Xonotic places focus on community involvement as its principal driving force
and structures itself to respect that. The aim of Xonotic is to become the 
best possible open-source FPS (first-person-shooter) of its kind.

%package data
Summary:	Xonotic data files (graphics, music, maps etc)
Requires:	%{name} = %{version}
Group:		Games/Arcade
BuildArch:	noarch

%description data
Data files used to play Xonotic.

%prep
%setup -q -n %{oname}

%build
cd source/darkplaces
make clean
make release CPUOPTIMIZATIONS="%{optflags}" DP_FS_BASEDIR=%{_gamesdatadir}/%{name}

%install
install -d %{buildroot}%{_gamesdatadir}/%{name}
cp -R data %{buildroot}%{_gamesdatadir}/%{name}/

install -D -m 755 source/darkplaces/darkplaces-sdl %{buildroot}%{_gamesbindir}/%{name}-sdl
install -D -m 755 source/darkplaces/darkplaces-glx %{buildroot}%{_gamesbindir}/%{name}-glx

install -D -m 644 misc/logos/icons_png/%{name}_16.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -D -m 644 misc/logos/icons_png/%{name}_32.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -D -m 644 misc/logos/icons_png/%{name}_64.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
install -D -m 644 misc/logos/icons_png/%{name}_128.png %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png

install -D -m 644 misc/logos/%{name}_icon.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/%{name}.svg

install -d %{buildroot}%{_datadir}/applications

cat > %{buildroot}%{_datadir}/applications/%{name}-sdl.desktop << EOF
[Desktop Entry]
Name=Xonotic-SDL
Comment=Multi-player first person shooter (SDL)
Exec=%{_gamesbindir}/%{name}-sdl
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=Game;ArcadeGame;
EOF

cat > %{buildroot}%{_datadir}/applications/%{name}-glx.desktop << EOF
[Desktop Entry]
Name=Xonotic-GLX
Comment=Multi-player first person shooter (GLX)
Exec=%{_gamesbindir}/%{name}-glx
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=Game;ArcadeGame;
EOF

%files
%{_gamesbindir}/%{name}-sdl
%{_gamesbindir}/%{name}-glx
%{_datadir}/applications/%{name}-sdl.desktop
%{_datadir}/applications/%{name}-glx.desktop
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/64x64/apps/%{name}.png
%{_iconsdir}/hicolor/128x128/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg

%files data
%dir %{_gamesdatadir}/%{name}/data
%{_gamesdatadir}/%{name}/data/*

