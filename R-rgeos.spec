#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rgeos
Version  : 0.5.5
Release  : 23
URL      : https://cran.r-project.org/src/contrib/rgeos_0.5-5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rgeos_0.5-5.tar.gz
Summary  : Interface to Geometry Engine - Open Source ('GEOS')
Group    : Development/Tools
License  : GPL-2.0+ LGPL-2.1
Requires: R-rgeos-lib = %{version}-%{release}
Requires: R-XML
Requires: R-sp
BuildRequires : R-XML
BuildRequires : R-sp
BuildRequires : buildreq-R
BuildRequires : geos-dev

%description
For OSX Mavericks+, Bill Behrman suggests:
https://stat.ethz.ch/pipermail/r-sig-mac/2015-March/011317.html

%package lib
Summary: lib components for the R-rgeos package.
Group: Libraries

%description lib
lib components for the R-rgeos package.


%prep
%setup -q -c -n rgeos
cd %{_builddir}/rgeos

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1599608491

%install
export SOURCE_DATE_EPOCH=1599608491
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rgeos
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rgeos
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rgeos
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rgeos || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rgeos/ChangeLog
/usr/lib64/R/library/rgeos/DESCRIPTION
/usr/lib64/R/library/rgeos/INDEX
/usr/lib64/R/library/rgeos/Meta/Rd.rds
/usr/lib64/R/library/rgeos/Meta/features.rds
/usr/lib64/R/library/rgeos/Meta/hsearch.rds
/usr/lib64/R/library/rgeos/Meta/links.rds
/usr/lib64/R/library/rgeos/Meta/nsInfo.rds
/usr/lib64/R/library/rgeos/Meta/package.rds
/usr/lib64/R/library/rgeos/NAMESPACE
/usr/lib64/R/library/rgeos/R/rgeos
/usr/lib64/R/library/rgeos/R/rgeos.rdb
/usr/lib64/R/library/rgeos/R/rgeos.rdx
/usr/lib64/R/library/rgeos/README
/usr/lib64/R/library/rgeos/SVN_VERSION
/usr/lib64/R/library/rgeos/help/AnIndex
/usr/lib64/R/library/rgeos/help/aliases.rds
/usr/lib64/R/library/rgeos/help/paths.rds
/usr/lib64/R/library/rgeos/help/rgeos.rdb
/usr/lib64/R/library/rgeos/help/rgeos.rdx
/usr/lib64/R/library/rgeos/html/00Index.html
/usr/lib64/R/library/rgeos/html/R.css
/usr/lib64/R/library/rgeos/poly-ex-gpc/ex-poly1.txt
/usr/lib64/R/library/rgeos/poly-ex-gpc/ex-poly2.txt
/usr/lib64/R/library/rgeos/poly-ex-gpc/hole-poly.txt
/usr/lib64/R/library/rgeos/test_cases/polys.RData
/usr/lib64/R/library/rgeos/tests/leak_by_exception.R
/usr/lib64/R/library/rgeos/tests/leak_by_exception.Rout.save
/usr/lib64/R/library/rgeos/tests/test-all.R
/usr/lib64/R/library/rgeos/tests/testthat/process_testxml.R
/usr/lib64/R/library/rgeos/tests/testthat/test-jts-xml.R
/usr/lib64/R/library/rgeos/tests/testthat/test-linearref.R
/usr/lib64/R/library/rgeos/tests/testthat/test-misc.R
/usr/lib64/R/library/rgeos/tests/testthat/test-translate-empty.R
/usr/lib64/R/library/rgeos/tests/testthat/test-translate-lines.R
/usr/lib64/R/library/rgeos/tests/testthat/test-translate-points.R
/usr/lib64/R/library/rgeos/tests/testthat/test-translate-polygon-collection.R
/usr/lib64/R/library/rgeos/tests/testthat/test-translate-polygons.R
/usr/lib64/R/library/rgeos/tests/testthat/test-translate-rings.R
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestBoundary.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestCentroid.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestConvexHull-big.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestConvexHull.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestFunctionAA.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestFunctionAAPrec.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestFunctionLA.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestFunctionLAPrec.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestFunctionLL.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestFunctionLLPrec.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestFunctionPA.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestFunctionPL.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestFunctionPLPrec.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestFunctionPP.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestInteriorPoint.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestRectanglePredicate.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestRelateAA.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestRelateAC.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestRelateLA.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestRelateLC.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestRelateLL.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestRelatePA.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestRelatePL.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestRelatePP.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestSimple.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestValid.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestValid2-big.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestValid2.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/general/TestWithinDistance.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/robust/ExternalRobustness.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/robust/TestRobustOverlayFixed.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/robust/TestRobustOverlayFloat.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/robust/TestRobustRelate.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/validate/TestRelateAA-big.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/validate/TestRelateAA.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/validate/TestRelateAC.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/validate/TestRelateLA.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/validate/TestRelateLC.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/validate/TestRelateLL.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/validate/TestRelatePA.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/validate/TestRelatePL.xml
/usr/lib64/R/library/rgeos/tests/testthat/testxml/validate/TestRelatePP.xml
/usr/lib64/R/library/rgeos/wkts/sline1.wkt
/usr/lib64/R/library/rgeos/wkts/sline2.wkt
/usr/lib64/R/library/rgeos/wkts/sppsp.wkt

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/rgeos/libs/rgeos.so
/usr/lib64/R/library/rgeos/libs/rgeos.so.avx2
/usr/lib64/R/library/rgeos/libs/rgeos.so.avx512
