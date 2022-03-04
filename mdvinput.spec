Summary:	Small programm for set keyboard, mouse and touchpad
Name:		mdvinput
Version:	1.6.6
Release:	1
Group:		Graphical desktop/Other
License:	GPLv2+
Url:		https://sourceforge.net/projects/mdvinput
Source0:	https://sourceforge.net/projects/mdvinput/files/%{name}-%{version}.tar.gz
#Patch0:		mdvinput-1.6.2-missing-locale.patch
BuildArch:	noarch

Requires:	python3
Requires:	python-gobject3
Requires:	python-configobj
Suggests:	x11-driver-input-synaptics

Obsoletes:	lxinput

%description
It's small utilites setup keyboard, mouse and touchpad
for replace lxinput and other on lightweight DE.

%files -f %{name}.lang
%doc AUTHORS ChangeLog README TODO
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png

#----------------------------------------------------------------------

%prep
%autosetup -p1

%build
# nothing to build

%install
# launcher
install -dm 0755 %{buildroot}%{_bindir}/
install -pm 0755 bin/%{name} %{buildroot}%{_bindir}/

# libs
install -dm 0755 %{buildroot}%{_datadir}/%{name}/
install -pm 0644 share/%{name}/* %{buildroot}%{_datadir}/%{name}/

# icon
install -dm 0755 %{buildroot}%{_datadir}/pixmaps/
install -pm 0644 share/pixmaps/%{name}.png %{buildroot}%{_datadir}/pixmaps/

# .desktop
install -dm 0755 %{buildroot}%{_datadir}/applications/
install -pm 0644 share/applications/%{name}.desktop %{buildroot}%{_datadir}/applications/

# locaes
install -dm 0755 %{buildroot}%{_datadir}/locale/
cp -ra share/locale/* %{buildroot}%{_datadir}/locale/

# locales
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
