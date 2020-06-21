main.pdf: main.dvi
	dvipdfmx -p a4 main.dvi
main.dvi: main.tex \
	1_intro.tex 2_measurement.tex 3_data.tex 4_processing.tex \
	Figs/samples.eps Figs/ut_setup.eps Figs/fig3.eps Figs/cod.eps \
	Figs/snapshot.eps Figs/phase_xy.eps Figs/fkplot_Al.eps Figs/fkplot_bar2.eps \
	Figs/pdf_kw_Al.eps Figs/pdf_kw_bar.eps Figs/phi_R.eps Figs/tof_hist.eps \
	Figs/sigma_t.eps Figs/sigma_y.eps Figs/unwrap.eps Figs/tof1d.eps
	platex main.tex
Figs/samples.eps: Figs/samples.svgz
	inkscape -z -f Figs/samples.svgz -E Figs/samples.eps
Figs/ut_setup.eps: Figs/ut_setup.svgz
	inkscape -z -f Figs/ut_setup.svgz -E Figs/ut_setup.eps
Figs/fig3.eps: Figs/fig3.svgz
	inkscape -z -f Figs/fig3.svgz -E Figs/fig3.eps
Figs/cod.eps: Figs/cod.svgz
	inkscape -z -f Figs/cod.svgz -E Figs/cod.eps
Figs/snapshot.eps: Figs/snapshot.svgz
	inkscape -z -f Figs/snapshot.svgz -E Figs/snapshot.eps
Figs/phase_xy.eps: Figs/phase_xy.svgz
	inkscape -z -f Figs/phase_xy.svgz -E Figs/phase_xy.eps
Figs/fkplot_Al.eps: Figs/fkplot_Al.svgz
	inkscape -z -f Figs/fkplot_Al.svgz -E Figs/fkplot_Al.eps
Figs/fkplot_bar2.eps: Figs/fkplot_bar2.svgz
	inkscape -z -f Figs/fkplot_bar2.svgz -E Figs/fkplot_bar2.eps
Figs/pdf_kw_Al.eps: Figs/pdf_kw_Al.svgz
	inkscape -z -f Figs/pdf_kw_Al.svgz -E Figs/pdf_kw_Al.eps
Figs/pdf_kw_bar.eps: Figs/pdf_kw_bar.svgz
	inkscape -z -f Figs/pdf_kw_bar.svgz -E Figs/pdf_kw_bar.eps
Figs/phi_R.eps: Figs/phi_R.svgz
	inkscape -z -f Figs/phi_R.svgz -E Figs/phi_R.eps
Figs/tof_hist.eps: Figs/tof_hist.svgz
	inkscape -z -f Figs/tof_hist.svgz -E Figs/tof_hist.eps
Figs/sigma_t.eps: Figs/sigma_t.svgz
	inkscape -z -f Figs/sigma_t.svgz -E Figs/sigma_t.eps
Figs/sigma_y.eps: Figs/sigma_y.svgz
	inkscape -z -f Figs/sigma_y.svgz -E Figs/sigma_y.eps
Figs/unwrap.eps: Figs/unwrap.svgz
	inkscape -z -f Figs/unwrap.svgz -E Figs/unwrap.eps
Figs/tof1d.eps: Figs/tof1d.svgz
	inkscape -z -f Figs/tof1d.svgz -E Figs/tof1d.eps
