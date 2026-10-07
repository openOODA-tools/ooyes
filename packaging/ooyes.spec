Name:           ooyes
Version:        0.1.0
Release:        1%{?dist}
Summary:        Bounded rate or infinite byte string emitter for stress testing and stream piping.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooyes
Source0:        ooyes-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooyes is a sovereign, capability-bounded INFINITE EMITTER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooyes
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooyes-uninstall

%files
/usr/bin/ooyes
/usr/bin/ooyes-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
