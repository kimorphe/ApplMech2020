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

    ax.plot(Tf1.tmax,-Tf1.ycod,"b-",label="alminium")
    ax.plot(Tf1.tave,-Tf1.ycod,"b--",label="alminium")
    ax.plot(Tf2.tmax,-Tf2.ycod,"r-",label="bar")
    ax.plot(Tf2.tave,-Tf2.ycod,"r--",label="bar")
    ax.plot(Tf3.tmax,-Tf3.ycod,"g-",label="core")
    ax.plot(Tf3.tave,-Tf3.ycod,"g--",label="core")
    #ax.plot(Tf.tave+Tf.tsig,-Tf.ycod,"--")
    #ax.plot(Tf.tave-Tf.tsig,-Tf.ycod,"--")

    #plt.legend()

    fsz=14
    ax.tick_params(labelsize=fsz)
    ax.set_xlim([0,10])
    ax.set_ylim([0,20])
    ax.set_xlabel("time [$\mu$s]",fontsize=fsz+2)
    ax.set_ylabel("x [mm]",fontsize=fsz+2)


    fig2=plt.figure()
    bx=fig2.add_subplot(111)
    bx.grid(True)
    deg=2
    Tf1.fit(deg)
    Tf2.fit(deg)
    Tf3.fit(deg)

    bx.plot(-Tf1.y_peak,-Tf1.c_peak,"b-",label="alminium")
    bx.plot(-Tf1.y_ave,-Tf1.c_ave,"b--",label="alminium")
    bx.plot(-Tf2.y_peak,-Tf2.c_peak,"r-",label="bar")
    bx.plot(-Tf2.y_ave,-Tf2.c_ave,"r--",label="bar")
    bx.plot(-Tf3.y_peak,-Tf3.c_peak,"g-",label="core")
    bx.plot(-Tf3.y_ave,-Tf3.c_ave,"g--",label="core")
    bx.tick_params(labelsize=fsz)
    bx.set_xlim([0,20])
    bx.set_ylim([2.5,3.5])
    bx.set_ylabel("velocity [km/s]",fontsize=fsz+2)
    bx.set_xlabel("x [mm]",fontsize=fsz+2)

    #plt.legend()

    plt.show()

    fig1.savefig("tof1d.png",bbox_inches="tight")
    fig2.savefig("vel1d.png",bbox_inches="tight")

