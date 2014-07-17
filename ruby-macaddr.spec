%define pkgname macaddr
Summary:	Ruby library for dealing with MAC addresses
Name:		ruby-%{pkgname}
Version:	1.6.1
Release:	2
License:	MIT
Group:		Development/Tools
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	69fa3d4572d8d49c0d6f712b3b7bc6e0
URL:		http://rubygems.org/gems/macaddr
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
Requires:	ruby-systemu >= 2.5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby library to interpret MAC addresses.

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{ruby_vendorlibdir}/macaddr.rb
