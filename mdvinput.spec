Summary:	Small programm for set keyboard, mouse and touchpad      
Name:		mdvinput          
Version:	1.6.2
Release:	6
Group:		Graphical desktop/Other          
License:	GPLv2+            
Url:		http://mandriva-lxde.googlecode.com
Source0:	http://mandriva-lxde.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:	mdvinput-1.6.2-missing-locale.patch
BuildArch:	noarch
Requires:	python
Requires:	pygtk2.0
Requires:	python-configobj
Suggests:	x11-driver-input-synaptics
Obsoletes:	lxinput

%description
It's small utilites setup keyboard, mouse and touchpad
for replace lxinput and other on lightweight DE.

%prep
%setup -q
%apply_patches

%install
mkdir -p %{buildroot}/usr
mkdir -p %{buildroot}/usr/lib
mkdir -p %{buildroot}%{_datadir}/applications

cp -rf ./bin %{buildroot}/usr/
cp -rf ./share %{buildroot}/usr/
cp -rf ./mdvinput %{buildroot}/usr/lib/


%files
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/locale/*
%{_datadir}/%{name}
/usr/lib/%{name}

