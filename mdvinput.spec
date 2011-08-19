Name: mdvinput          
Version: 1.6.1
Release: %mkrel 1
Summary:  Small programm for set keyboard, mouse and touchpad      

Group: Graphical desktop/Other          
License: GPLv2+            
Source0: %{name}-%{version}.tar.gz
Source1: mdvinput.desktop
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: python, pygtk2.0, python-configobj
Suggests: x11-driver-input-synaptics
Obsoletes: lxinput
BuildArch: noarch

%description

It's small utilites setup keyboard, mouse and touchpad for replace lxinput and other on lightweight DE.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p %buildroot/usr
mkdir -p %buildroot/usr/lib
mkdir -p %buildroot%{_datadir}/applications

cp -rf ./bin %buildroot/usr/
cp -rf ./share %buildroot/usr/
cp -rf ./mdvinput %buildroot/usr/lib/
cp %SOURCE1 %buildroot%{_datadir}/applications/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/locale/*
%{_datadir}/%{name}
/usr/lib/%{name}