Name: mdvinput          
Version: 1.5       
Release: %mkrel 1
Summary:  Small programm for set keyboard, mouse and touchpad      

Group: Graphical desktop/Other          
License: GPLv2+            
Source0: %{name}-%{version}.tar.gz        
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: python, pygtk2.0
Suggests: x11-driver-input-synaptics
Obsoletes: lxinput      
BuildArch: noarch

%description

It's small utilites for replace lxinput and other on lightweight DE.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p %buildroot/{etc,usr}

cp -rf ./etc %buildroot/
cp -rf ./usr %buildroot/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_sysconfdir}/skel/.config/mdvinput/*
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/locale/*
/usr/lib/mdk/%{name}/*

