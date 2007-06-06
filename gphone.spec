%define name gphone
%define version 0.5.2
%define release %mkrel 9

Summary: Gphone is an internet telephone
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
URL: http://gphone.sourceforge.net/
Group: Sound
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: gsm-devel gtk+-devel slang-devel popt-devel

%description
Gphone is an internet telephone.  As the name implies, it aims to be
fully gnome-groovy, but that hasn't quite happened yet.  Gphone is
definitely a work in progress and you probably shouldn't bet your
business on it.  Don't be too hard on the program, though -- although
the user interface is mighty rough, gphone does actually work pretty
well.  I've only tested the program over ethernet, but the data rate
should be low enough to work over a reasonable modem connection.

The protocol is nominally RTP/RTCP, and gphone complies well enough
with the standard to be able to talk to speakfreely.  I've only tested
the UNIX version of speakfreely, but as long as you tell sfmike to use
RTP and GSM compression, it seems to work fine.  Maybe someday I'll
add in support for other codecs; encryption is a little less likely
because I'd just as soon not open that legal can of worms.  One easy
way to get some security would be to modify my program rtptunnel to
tunnel the RTP protocol through a SSL socket instead of a straight TCP
socket.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%configure

%build

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat > $RPM_BUILD_ROOT%{_menudir}/%{name} << EOF
?package(%{name}): needs=x11 section="Multimedia/Sound" \
title=Gphone longtitle="Internet telephone" command=gphone \
icon="other_networking.png"
EOF

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog NEWS README TODO AUTHORS
%{_bindir}/*
%{_menudir}/*
