%global packname  ROCR
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.0_5
Release:          1
Summary:          Visualizing the performance of scoring classifiers
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-5.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-gplots R-methods 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-gplots R-methods

%description
ROC graphs, sensitivity/specificity curves, lift charts, and
precision/recall plots are popular examples of trade-off visualizations
for specific pairs of performance measures. ROCR is a flexible tool for
creating cutoff-parametrized 2D performance curves by freely combining two
from over 25 performance measures (new performance measures can be added
using a standard interface). Curves from different cross-validation or
bootstrapping runs can be averaged by different methods, and standard
deviations, standard errors or box plots can be used to visualize the
variability across the runs. The parametrization can be visualized by
printing cutoff values at the corresponding curve positions, or by
coloring the curve according to cutoff. All components of a performance
plot can be quickly adjusted using a flexible parameter dispatching
mechanism. Despite its flexibility, ROCR is easy to use, with only three
commands and reasonable default values for all optional parameters.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help


%changelog
* Sun Feb 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0_4-1
+ Revision: 777441
- Import R-ROCR
- Import R-ROCR

