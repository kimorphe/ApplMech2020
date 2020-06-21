#! /home/kazushi/anaconda3/bin/python
import numpy as np
import matplotlib.pyplot as plt


class yStats:
    def load(self,fname):
        fp=open(fname,"r")
        cbff=fp.readline()
        time=[]
        ysig=[]
        yave=[]
        for row in fp:
            dat=row.strip().split(",")
            time.append(float(dat[0]))
            ysig.append(float(dat[1]))
            yave.append(float(dat[2]))

        self.time=np.array(time)
        self.ysig=np.array(ysig)
        self.yave=np.array(yave)
        fp.close()

if __name__=="__main__":
    fname="ystat.dat"

    fsz=14

    Tf1=yStats()
    Tf2=yStats()
    Tf3=yStats()

    fname1="Alminium/ystat.dat"
    fname2="Bar2/ystat.dat"
    fname3="CoreM_short/ystat.dat"
    Tf1.load(fname1)
    Tf2.load(fname2)
    Tf3.load(fname3)

    fig1=plt.figure()
    ax=fig1.add_subplot(111)
    ax.grid(True)

    ax.plot(Tf1.time, Tf1.ysig,"b-",label="alminium")
    ax.plot(Tf2.time, Tf2.ysig,"r-",label="bar")
    ax.plot(Tf3.time, Tf3.ysig,"g-",label="core")

    fig2=plt.figure()
    bx=fig2.add_subplot(111)
    bx.grid(True)
    bx.plot(Tf1.time, -Tf1.ysig/Tf1.yave,"b-",label="alminium")
    bx.plot(Tf2.time, -Tf2.ysig/Tf2.yave,"r-",label="bar")
    bx.plot(Tf3.time, -Tf3.ysig/Tf3.yave,"g-",label="core")


    ax.tick_params(labelsize=fsz)
    ax.set_xlim([0,5])
    ax.set_ylim([0,2])
    ax.set_xlabel("travel time $T_f$ [$\mu$s]",fontsize=fsz+2)
    ax.set_ylabel("$\delta x$[mm]",fontsize=fsz+2)


    bx.tick_params(labelsize=fsz)
    bx.set_xlim([0,5])
    bx.set_ylim([0,0.5])
    bx.set_xlabel("travel time $T_f$ [$\mu$s]",fontsize=fsz+2)
    bx.set_ylabel("$\delta x/ \overline{x} $",fontsize=fsz+2)
    #plt.legend()

    plt.show()

    fig1.savefig("delx_t.png",bbox_inches="tight")
    fig2.savefig("delx_t_nrm.png",bbox_inches="tight")

