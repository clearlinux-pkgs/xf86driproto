#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xf86driproto
Version  : 2.1.1
Release  : 17
URL      : http://xorg.freedesktop.org/releases/individual/proto/xf86driproto-2.1.1.tar.bz2
Source0  : http://xorg.freedesktop.org/releases/individual/proto/xf86driproto-2.1.1.tar.bz2
Summary  : XF86DRI extension headers
Group    : Development/Tools
License  : MIT
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(xorg-macros)

%description
XFree86 Direct Rendering Infrastructure Extension
This extension defines a protocol to allow user applications to access
the video hardware without requiring data to be passed through the X server.

%package dev
Summary: dev components for the xf86driproto package.
Group: Development
Provides: xf86driproto-devel

%description dev
dev components for the xf86driproto package.


%package dev32
Summary: dev32 components for the xf86driproto package.
Group: Default
Requires: xf86driproto-dev

%description dev32
dev32 components for the xf86driproto package.


%prep
%setup -q -n xf86driproto-2.1.1
pushd ..
cp -a xf86driproto-2.1.1 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507170209
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1507170209
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/dri/xf86dri.h
/usr/include/X11/dri/xf86driproto.h
/usr/include/X11/dri/xf86dristr.h
/usr/lib64/pkgconfig/xf86driproto.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/pkgconfig/32xf86driproto.pc
/usr/lib32/pkgconfig/xf86driproto.pc
