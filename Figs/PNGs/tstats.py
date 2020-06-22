#! /home/kazushi/anaconda3/bin/python
import numpy as np
import matplotlib.pyplot as plt


class tStats:
    def load(self,fname):
        fp=open(fname,"r")
        cbff=fp.readline()
        ycod=[]
        tsig=[]
        tave=[]
        tmax=[]
        for row in fp:
            dat=row.strip().split(",")
            ycod.append(float(dat[0]))
            tsig.append(float(dat[1]))
            tave.append(float(dat[2]))
            tmax.append(float(dat[3]))

        self.ycod=np.array(ycod)
        self.tsig=np.array(tsig)
        self.tave=np.array(tave)
        self.tmax=np.array(tmax)
        fp.close()
    def fit(self,deg):
        ycod=self.ycod
        tave=self.tave
        tmax=self.tmax

        C0=np.polyfit(tmax,ycod,deg)
        C1=np.polyder(C0)
        P0=np.poly1d(C0)
        P1=np.poly1d(C1)
        y_peak=P0(tmax)
        c_peak=P1(tmax)

        C0=np.polyfit(tave,ycod,deg)
        C1=np.polyder(C0)
        P0=np.poly1d(C0)
        P1=np.poly1d(C1)
        y_ave=P0(tave)
        c_ave=P1(tave)

        self.c_peak=c_peak
        self.y_peak=y_peak
        self.c_ave=c_ave
        self.y_ave=y_ave


if __name__=="__main__":
    fname="tstat.dat"

    fsz=14

    Tf1=tStats()
    Tf2=tStats()
    Tf3=tStats()

    fname1="Alminium/tstat.dat"
    fname2="Bar2/tstat.dat"
    fname3="CoreM_short/tstat.dat"
    Tf1.load(fname1)
    Tf2.load(fname2)
    Tf3.load(fname3)

    fig1=plt.figure()
    ax=fig1.add_subplot(111)
    ax.grid(True)

    ax.plot(-Tf1.ycod, Tf1.tsig,"b-",label="alminium")
    ax.plot(-Tf2.ycod, Tf2.tsig,"r-",label="bar")
    ax.plot(-Tf3.ycod, Tf3.tsig,"g-",label="core")

    fig2=plt.figure()
    bx=fig2.add_subplot(111)
    bx.grid(True)
    bx.plot(-Tf1.ycod, Tf1.tsig/Tf1.tave,"b-",label="alminium")
    bx.plot(-Tf2.ycod, Tf2.tsig/Tf2.tave,"r-",label="bar")
    bx.plot(-Tf3.ycod, Tf3.tsig/Tf3.tave,"g-",label="core")


    ax.tick_params(labelsize=fsz)
    ax.set_xlim([0,20])
    ax.set_ylim([0,0.8])
    #ax.set_xlabel("$\overline{x}$ [mm]",fontsize=fsz+2)
    ax.set_xlabel("$x$ [mm]",fontsize=fsz+2)
    ax.set_ylabel("$\delta T_f$ [$\mu$s]",fontsize=fsz+2)


    bx.tick_params(labelsize=fsz)
    bx.set_xlim([0,20])
    bx.set_ylim([0,0.8])
    #bx.set_xlabel("$\overline{x}$ [mm]",fontsize=fsz+2)
    bx.set_xlabel("$x$ [mm]",fontsize=fsz+2)
    bx.set_ylabel("$\delta T_f/\overline{T}_f$ ",fontsize=fsz+2)

    #plt.legend()

    fig3=plt.figure()
    cx=fig3.add_subplot(111)
    cx.set_xscale('log')
    cx.set_yscale('log')
    #cx.plot(np.log(-Tf1.ycod), np.log(Tf1.tsig/Tf1.tave),"b-",label="alminium")
    #cx.plot(np.log(-Tf2.ycod), np.log(Tf2.tsig/Tf2.tave),"r-",label="bar")
    #cx.plot(np.log(-Tf3.ycod), np.log(Tf3.tsig/Tf3.tave),"g-",label="core")
    cx.plot((-Tf1.ycod), (Tf1.tsig/Tf1.tave),"b-",label="alminium")
    cx.plot((-Tf2.ycod), (Tf2.tsig/Tf2.tave),"r-",label="bar")
    cx.plot((-Tf3.ycod), (Tf3.tsig/Tf3.tave),"g-",label="core")
    cx.tick_params(labelsize=fsz)
    cx.grid(True)
    #cx.set_xlim([0,20])
    #cx.set_ylim([0.1,1.])
    #ax.set_xlabel("$\overline{x}$ [mm]",fontsize=fsz+2)
    cx.set_xlabel("$x$ [mm]",fontsize=fsz+2)
    cx.set_ylabel("$\delta T_f$ [$\mu$s]",fontsize=fsz+2)


    ylog=np.log(-Tf1.ycod[1:])
    slog=np.log(Tf1.tsig[1:]/Tf1.tave[1:])

    deg=1

    PA=np.polyfit(ylog,slog,deg)

    ylog=np.log(-Tf2.ycod[1:])
    slog=np.log(Tf2.tsig[1:]/Tf2.tave[1:])
    PB=np.polyfit(ylog,slog,deg)

    ylog=np.log(-Tf3.ycod[1:])
    slog=np.log(Tf3.tsig[1:]/Tf2.tave[1:])
    PC=np.polyfit(ylog,slog,deg)

    print("P(alminium), m=",PA,-1./PA[0])
    print("P(block), m=",PB,-1./PB[0])
    print("P(core), m=",PC,-1./PC[0])


    plt.show()

    fig1.savefig("delT_x.png",bbox_inches="tight")
    fig2.savefig("delT_x_nrm.png",bbox_inches="tight")
    fig3.savefig("delT_log.png",bbox_inches="tight")

