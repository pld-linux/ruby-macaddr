
%define gitrev 053e94b
%define gitauthor assaf
%define gitname macaddr

Summary:	Ruby library for dealing with MAC addresses
Name:		ruby-macaddr
Version:	1.0.0
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	http://codeforpeople.com/lib/ruby/macaddr/macaddr-1.0.0.tgz
# Source0-md5:	46827e2c3bef03b37f7558050e502ecf
URL:		http://codeforpeople.com/lib/ruby/macaddr/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby
BuildRequires:	ruby-modules
BuildRequires:	setup.rb = 3.4.1
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby library to interpret MAC addresses.

%prep
%setup -q -n macaddr-%{version}
cp %{_datadir}/setup.rb .
ruby setup.rb config \
	--installdirs=std
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/macaddr.rb
