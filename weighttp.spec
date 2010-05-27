Summary:	lightweight and small benchmarking tool for webservers
Name:		weighttp
Version:	0.2
Release:	0.1
License:	MIT
Group:		Networking/Daemons/HTTP
Source0:	http://cgit.lighttpd.net/weighttp/snapshot/%{name}-master.tar.gz
# Source0-md5:	97b9ecd28a6f23af981956502c076de2
URL:		http://redmine.lighttpd.net/projects/weighttp
BuildRequires:	libev-devel
BuildRequires:	waf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
weighttp (pronounced weighty) is a lightweight and small benchmarking
tool for webservers.

It was designed to be very fast and easy to use and only supports a
tiny fraction of the HTTP protocol in order to be lean and simple.

weighttp supports multithreading to make good use of modern CPUs with
multiple cores as well as asynchronous i/o for concurrent requests
within a single thread.

For event handling, weighty relies on libev which fits the design
perfectly, being lightweight and fast itself.

Thanks to that, weighty supports all modern high-performance event
interfaces like epoll or kqueue, that the major OSs provide.

%prep
%setup -q -n %{name}-master

%build
%waf configure \
	--prefix=%{_prefix}
%waf build

%install
rm -rf $RPM_BUILD_ROOT
%waf install \
	--destdir $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README TODO
%attr(755,root,root) %{_bindir}/weighttp
