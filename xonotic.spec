%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	A free multi-player first person shooter
Name:		xonotic
Version:	0.8.5
Release:	1
Url:		http://www.xonotic.org/
Source0:	http://dl.xonotic.org/%{name}-%{version}.zip
License:	GPLv2+
Group:		Games/Arcade
Patch0:		xonotic-ldflags.patch
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(xxf86dga)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(libjpeg)
Requires:	%{name}-data = %{version}

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
%autosetup -p1 -n Xonotic

%build
%set_build_flags
%make_build -C source/darkplaces sv-release cl-release sdl-release \
	CPUOPTIMIZATIONS="%{optflags}" STRIP=: \
	LDFLAGS_RELEASE="%{build_ldflags}" \
	DP_FS_BASEDIR=%{_gamesdatadir}/%{name}

%install
install -d %{buildroot}%{_gamesdatadir}/%{name}
cp -R data %{buildroot}%{_gamesdatadir}/%{name}/

install -D -m755 source/darkplaces/darkplaces-dedicated %{buildroot}%{_gamesbindir}/%{name}-dedicated
install -D -m755 source/darkplaces/darkplaces-sdl %{buildroot}%{_gamesbindir}/%{name}-sdl
install -D -m755 source/darkplaces/darkplaces-glx %{buildroot}%{_gamesbindir}/%{name}-glx

for size in 16 32 64 128; do
    install -D -m644 misc/logos/icons_png/%{name}_${size}.png %{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps/%{name}.png
done
install -D -m644 misc/logos/%{name}_icon.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/%{name}.svg

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
%{_gamesbindir}/%{name}-dedicated
%{_gamesbindir}/%{name}-sdl
%{_gamesbindir}/%{name}-glx
%{_datadir}/applications/%{name}-sdl.desktop
%{_datadir}/applications/%{name}-glx.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*

%files data
%dir %{_gamesdatadir}/%{name}/data
%{_gamesdatadir}/%{name}/data/*

