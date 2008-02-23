Summary:	A city simulation game
Summary(pl.UTF-8):	Gra z symulacją miasta
Name:		micropolis
Version:	0.1
Release:	1
License:	GPL v3
Group:		Applications/Games
Source0:	http://www.donhopkins.com/home/micropolis/%{name}-activity-source.tgz
# Source0-md5:	50a62417cdee6b7c1ed333d794f5107d
URL:		http://wiki.laptop.org/go/Micropolis
BuildRequires:	tcl-devel
BuildRequires:	tclx-devel
BuildRequires:	tk-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Micropolis is one of the oldest and grandest of city simulation games.

%description -l pl.UTF-8
Micropolis to jedna z najstarszych i najwspanialszych gier z symulacją
miasta.

%prep
%setup -q -n %{name}-activity

%build
%{__make} -C src \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}" \
	OPTIMIZE_FLAG="%{rpmcflags} -DIS_LINUX"

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
