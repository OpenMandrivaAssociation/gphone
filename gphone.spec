%define name gphone
%define version 0.5.2
%define release 16

Summary: Internet telephone
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

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Gphone
Comment=Internet telephone
Exec=%{_bindir}/%{name} 
Icon=other_networking
Terminal=false
Type=Application
Categories=GNOME;GTK;AudioVideo;Audio;X-MandrivaLinux-Multimedia-Sound;
EOF

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog NEWS README TODO AUTHORS
%{_bindir}/*
%{_datadir}/applications/mandriva-%{name}.desktop



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.2-15mdv2011.0
+ Revision: 619235
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.5.2-14mdv2010.0
+ Revision: 429293
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.5.2-13mdv2009.0
+ Revision: 246535
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.5.2-11mdv2008.1
+ Revision: 170874
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Herton Ronaldo Krzesinski <herton@mandriva.com.br>
    - Switch to XDG menu.
    - Import gphone



* Thu Dec 15 2005 Lenny Cartier <lenny@mandriva.com> 0.5.2-9mdk
- rebuild

* Fri Jul 23 2004 Marcel Pol <mpol@mandrake.org> 0.5.2-8mdk
- again build against new slang

* Wed Jul 21 2004 Marcel Pol <mpol@mandrake.org> 0.5.2-7mdk
- build against new slang
- quiet setup

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.5.2-6mdk
- rebuild

* Tue Jan 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.5.2-5mdk
- rebuild

* Wed Jan 30 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.5.2-4mdk
- icon

* Fri Jul 20 2001  Lenny Cartier <lenny@mandrakesoft.com> 0.5.2-3mdk
- rebuild

* Wed Jan 10 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.5.2-2mdk
- rebuild
- url

* Fri Oct 20 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.5.2-1mdk
- first version

# gphone.spec ends here
