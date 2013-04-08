Name: mdvinput          
Version: 1.6.2
Release: 3
Summary:  Small programm for set keyboard, mouse and touchpad      

Group: Graphical desktop/Other          
License: GPLv2+            
Source0: http://mandriva-lxde.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:  mdvinput-1.6.2-missing-locale.patch
URL:	http://mandriva-lxde.googlecode.com
Requires: python, pygtk2.0, python-configobj
Suggests: x11-driver-input-synaptics
Obsoletes: lxinput
BuildArch: noarch

%description

It's small utilites setup keyboard, mouse and touchpad
for replace lxinput and other on lightweight DE.

%prep
%setup -q
%patch0 -p1

%install
mkdir -p %buildroot/usr
mkdir -p %buildroot/usr/lib
mkdir -p %buildroot%{_datadir}/applications

cp -rf ./bin %buildroot/usr/
cp -rf ./share %buildroot/usr/
cp -rf ./mdvinput %buildroot/usr/lib/


%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/locale/*
%{_datadir}/%{name}
/usr/lib/%{name}

%changelog
* Tue Aug 23 2011 Александр Казанцев <kazancas@mandriva.org> 1.6.2-1mdv2011.0
+ Revision: 696319
- 1.6.2 fix error with lxsession conf dir if not exist

* Fri Aug 19 2011 Александр Казанцев <kazancas@mandriva.org> 1.6.1-1
+ Revision: 695822
- change source structure
- add working locale support
- split mdvinput to lib and share
- add simple setup script

* Fri Aug 19 2011 Александр Казанцев <kazancas@mandriva.org> 1.6-2
+ Revision: 695257
- redesign UI like lxinput
- add setting save and read to lxsession conf file
- add smart feautures for touchpad
- apply setiing when press OK button

* Thu Aug 04 2011 Александр Казанцев <kazancas@mandriva.org> 1.5-2
+ Revision: 693234
- add missing mouse.png

* Wed Aug 03 2011 Александр Казанцев <kazancas@mandriva.org> 1.5-1
+ Revision: 692971
- imported package mdvinput

