# http://github.com/gonum/matrix

%global goipath         github.com/gonum/matrix
%global commit          fb1396264e2e259ff714a408a7b0142d238b198d


%gometa -i

Name:           %{goname}
Version:        0
Release:        0.11%{?dist}
Summary:        Matrix packages for the Go language
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

Patch0:         add-license.patch
Patch1:         change-internal-to-inteernal.patch

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/gonum/blas)
BuildRequires: golang(github.com/gonum/blas/blas64)
BuildRequires: golang(github.com/gonum/blas/cgo)
BuildRequires: golang(github.com/gonum/blas/testblas)
BuildRequires: golang(github.com/gonum/floats)
BuildRequires: golang(github.com/gonum/inteernal/asm)
BuildRequires: golang(github.com/gonum/lapack/lapack64)
BuildRequires: golang(gopkg.in/check.v1)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%patch0 -p1
%patch1 -p1

%install
%goinstall glide.lock glide.yaml

%check
%ifarch ppc64le s390x
%gochecks -d mat64
%else
%gochecks
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Mon Jun 11 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.11.gitfb13962
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.20150716gitfb13962
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitfb13962
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitfb13962
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.gitfb13962
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gitfb13962
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.gitfb13962
- https://fedoraproject.org/wiki/Changes/golang1.7

* Thu Jul 14 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0-0.4.gitfb13962
- Fix Exclusive arches for golang/openblas

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.gitfb13962
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitfb13962
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitfb13962
- First package for Fedora
  resolves: #1269923
