#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-oshi
Version  : 4.0.0
Release  : 1
URL      : https://github.com/oshi/oshi/archive/oshi-parent-4.0.0.tar.gz
Source0  : https://github.com/oshi/oshi/archive/oshi-parent-4.0.0.tar.gz
Source1  : https://repo.maven.apache.org/maven2/com/github/oshi/oshi-core/3.4.0/oshi-core-3.4.0.jar
Source2  : https://repo.maven.apache.org/maven2/com/github/oshi/oshi-core/3.4.0/oshi-core-3.4.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: mvn-oshi-data = %{version}-%{release}
Requires: mvn-oshi-license = %{version}-%{release}

%description
![OSHI](https://dl.dropboxusercontent.com/s/c82qboyvvudpvdp/oshilogo.png)
[![Maven central](https://maven-badges.herokuapp.com/maven-central/com.github.oshi/oshi-core/badge.svg?)](https://search.maven.org/search?q=com.github.oshi)
[![Travis Build Status](https://travis-ci.org/oshi/oshi.svg)](https://travis-ci.org/oshi/oshi)
[![Appveyor Build status](https://ci.appveyor.com/api/projects/status/v489i8xoyfspxx7s?svg=true)](https://ci.appveyor.com/project/dbwiddis/oshi)
[![Coverage Status](https://coveralls.io/repos/github/oshi/oshi/badge.svg?branch=master)](https://coveralls.io/github/oshi/oshi?branch=master)
[![codecov.io](https://codecov.io/github/oshi/oshi/coverage.svg?branch=master)](https://codecov.io/github/oshi/oshi?branch=master)
[![Coverity Scan Build Status](https://img.shields.io/coverity/scan/9332.svg)](https://scan.coverity.com/projects/dblock-oshi)
[![Codacy Grade](https://api.codacy.com/project/badge/Grade/5370178ae91d4f56b43de2f26f7c5e7a)](https://www.codacy.com/app/widdis/oshi?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=oshi/oshi&amp;utm_campaign=Badge_Grade)
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![SonarQube Bugs](https://sonarcloud.io/api/project_badges/measure?project=com.github.oshi%3Aoshi-parent&metric=bugs)](https://sonarcloud.io/dashboard?id=com.github.oshi%3Aoshi-parent)
[![SonarQube Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=com.github.oshi%3Aoshi-parent&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=com.github.oshi%3Aoshi-parent)
[![SonarQube Maintainability](https://sonarcloud.io/api/project_badges/measure?project=com.github.oshi%3Aoshi-parent&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=com.github.oshi%3Aoshi-parent)
[![SonarQube Reliability](https://sonarcloud.io/api/project_badges/measure?project=com.github.oshi%3Aoshi-parent&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=com.github.oshi%3Aoshi-parent)
[![SonarQube Security](https://sonarcloud.io/api/project_badges/measure?project=com.github.oshi%3Aoshi-parent&metric=security_rating)](https://sonarcloud.io/dashboard?id=com.github.oshi%3Aoshi-parent)
[![Code Quality: Java](https://img.shields.io/lgtm/grade/java/g/oshi/oshi.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/oshi/oshi/context:java)
[![LGTM Stats](https://www.openhub.net/p/oshi/widgets/project_thin_badge.gif)](https://www.openhub.net/p/oshi?ref=github)
[![first-timers-only](https://img.shields.io/badge/first--timers--only-friendly-blue.svg?style=flat-square)](https://www.firsttimersonly.com/)
[![Join the chat at https://gitter.im/oshi/oshi](https://badges.gitter.im/oshi/oshi.svg)](https://gitter.im/oshi/oshi?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

%package data
Summary: data components for the mvn-oshi package.
Group: Data

%description data
data components for the mvn-oshi package.


%package license
Summary: license components for the mvn-oshi package.
Group: Default

%description license
license components for the mvn-oshi package.


%prep
%setup -q -n oshi-oshi-parent-4.0.0

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-oshi
cp LICENSE_HEADER %{buildroot}/usr/share/package-licenses/mvn-oshi/LICENSE_HEADER
cp oshi-dist/LICENSE_MIT %{buildroot}/usr/share/package-licenses/mvn-oshi/oshi-dist_LICENSE_MIT
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/oshi/oshi-core/3.4.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/github/oshi/oshi-core/3.4.0/oshi-core-3.4.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/oshi/oshi-core/3.4.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/github/oshi/oshi-core/3.4.0/oshi-core-3.4.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/github/oshi/oshi-core/3.4.0/oshi-core-3.4.0.jar
/usr/share/java/.m2/repository/com/github/oshi/oshi-core/3.4.0/oshi-core-3.4.0.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-oshi/LICENSE_HEADER
/usr/share/package-licenses/mvn-oshi/oshi-dist_LICENSE_MIT
