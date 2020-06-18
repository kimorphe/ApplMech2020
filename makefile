main.pdf: main.dvi
	dvipdfmx -p a4 main.dvi
main.dvi: main.tex \
	1_intro.tex 2_method.tex 3_model.tex 4_results.tex \
	Figs/samples.eps Figs/ut_setup.eps Figs/fig3.eps Figs/cod.eps \
	Figs/snapshot.eps
#	Figs/fig0.eps Figs/fig1.eps Figs/fig2.eps Figs/fig3.eps Figs/fig4.eps \
#	Figs/fig5.eps Figs/fig6.eps Figs/fig7.eps Figs/fig8.eps Figs/fig9.eps \
#	Figs/fig10.eps Figs/fig11.eps Figs/fig12.eps Figs/fig13.eps 
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
