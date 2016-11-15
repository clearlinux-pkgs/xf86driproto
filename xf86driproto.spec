#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xf86driproto
Version  : 2.1.1
Release  : 10
URL      : http://xorg.freedesktop.org/releases/individual/proto/xf86driproto-2.1.1.tar.bz2
Source0  : http://xorg.freedesktop.org/releases/individual/proto/xf86driproto-2.1.1.tar.bz2
Summary  : XF86DRI extension headers
Group    : Development/Tools
License  : MIT
BuildRequires : pkgconfig(xorg-macros)

%description
XFree86 Direct Rendering Infrastructure Extension
This extension defines a protocol to allow user applications to access
the video hardware without requiring data to be passed through the X server.

%package dev
Summary: dev components for the xf86driproto package.
Group: Development

%description dev
dev components for the xf86driproto package.


%prep
%setup -q -n xf86driproto-2.1.1

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/dri/xf86dri.h
/usr/include/X11/dri/xf86driproto.h
/usr/include/X11/dri/xf86dristr.h
/usr/lib64/pkgconfig/*.pc
