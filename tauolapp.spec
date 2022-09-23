### RPM external tauolapp 1.1.8
Source: http://tauolapp.web.cern.ch/tauolapp/resources/TAUOLA.%{realversion}/TAUOLA.%{realversion}-LHC.tar.gz
Requires: hepmc
Requires: pythia8
Requires: lhapdf

%define keep_archives true

%prep
%setup -q -n TAUOLA

export HEPMCLOCATION=${HEPMC_ROOT}
export HEPMCVERSION=${HEPMC_VERSION}
export LHAPDF_LOCATION=${LHAPDF_ROOT}
export PYTHIA8_LOCATION=${PYTHIA8_ROOT}

# Update to detect aarch64 and ppc64le
rm -f ./config/config.{sub,guess}
%get_config_sub ./config/config.sub
%get_config_guess ./config/config.guess
chmod +x ./config/config.{sub,guess}

./configure --prefix=%{i} --without-hepmc3 --with-hepmc=$HEPMC_ROOT --with-pythia8=$PYTHIA8_ROOT --with-lhapdf=$LHAPDF_ROOT CPPFLAGS="-I${BOOST_ROOT}/include"

%ifos darwin
perl -p -i -e "s|-shared|-dynamiclib -undefined dynamic_lookup|" make.inc
%endif

%build
make

%install
make install

mkdir %{i}/share
cp TauSpinner/examples/CP-tests/Z-pi/*.txt %{i}/share/

%post
%{relocateConfig}lib/lib*.la
