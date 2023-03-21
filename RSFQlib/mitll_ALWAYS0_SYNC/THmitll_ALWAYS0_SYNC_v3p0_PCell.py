import sys
# Change this to the location that contains the subcells folder
subcell_path = '..\\..\\PCell_Subcells'
if subcell_path not in sys.path:
    sys.path.append(subcell_path)
import layer_setup as ls
import bias
import connectors as conns
import fill
import jj
import resistors as res
import trackblocks as tb
import os
import spira.all as spira
from spira.technologies.mit.process.database import RDD

IXPORT = spira.RDD.PLAYER.IXPORT
TEXT = spira.Layer(number=182)

## Parameterization
# Trackpitch in microns
tp = 10
ls.tp = tp

class PCELL(spira.PCell):
    __name_prefix__ = "THmitll_ALWAYS0_SYNC_NOA_v3p0"
    def create_elements(self, elems):
        M0M5Strips = spira.SRef(M0M5_strips())
        IXports = spira.SRef(IX_ports())
        jjfill = spira.SRef(junction_fill())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        ib = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        rs = spira.SRef(resistors())
        ind = spira.SRef(inductors())
        tblocks = spira.SRef(trackblocks())
        elems += [M0M5Strips, IXports, jjfill, M4M5M6M7conns, ib, jjs, rs, ind, tblocks]
        
        # Text Labels
        elems += spira.Label(text='PR1 M6 M4',position=(0.500*tp,2.36*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PR2 M6 M4',position=(1.375*tp,1.505*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J2 M6 M5',position=(1.56*tp,0.63*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB2 M6 M4',position=(0.495*tp,0.175*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P2 M6 M4',position=(1.500*tp,0.000*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PR3 M6 M4',position=(1.505*tp,2.285*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J3 M6 M5',position=(1.385*tp,3.555*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB3 M6 M4',position=(1.355*tp,3.905*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P3 M6 M4',position=(2.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB1 M6 M4',position=(0.645*tp,3.905*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P1 M6 M4',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J1 M6 M5',position=(0.62*tp,3.56*tp),layer=spira.Layer(number=182,datatype=0))
        
        # LVS Labels
        elems += spira.Label(text='GND',position=(1.935*tp,6.32*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='VDD',position=(1.96*tp,6.500*tp),layer=spira.Layer(number=1,datatype=0))
        elems += spira.Label(text='clk',position=(1.500*tp,0.000*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='a',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='q',position=(2.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='R1',position=(0.500*tp,2.255*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='R2',position=(1.26*tp,1.495*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB2',position=(1.26*tp,0.62*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB2',position=(0.500*tp,0.700*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='R3',position=(1.500*tp,2.175*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB3',position=(1.385*tp,3.275*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB3',position=(1.355*tp,4.325*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB1',position=(0.65*tp,4.305*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB1',position=(0.615*tp,3.275*tp),layer=spira.Layer(number=52,datatype=11))
        return elems
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(1.400*tp,0.100*tp),(1.490*tp,0.190*tp),(1.490*tp,0.100*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.900*tp,3.400*tp),(1.810*tp,3.490*tp),(1.900*tp,3.490*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.100*tp,3.400*tp),(0.100*tp,3.490*tp),(0.190*tp,3.490*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.400*tp,0.000*tp),(1.400*tp,0.100*tp),(1.600*tp,0.100*tp),(1.600*tp,0.000*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.490*tp,0.100*tp),(1.490*tp,0.190*tp),(1.580*tp,0.190*tp),(1.580*tp,0.2775*tp),(1.4775*tp,0.2775*tp),(1.4775*tp,0.5025*tp),(1.5675*tp,0.5025*tp),(1.5675*tp,0.3675*tp),(1.670*tp,0.3675*tp),(1.670*tp,0.100*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.430*tp,1.005*tp),(0.430*tp,1.500*tp),(0.570*tp,1.500*tp),(0.570*tp,1.005*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.455*tp,0.125*tp),(0.455*tp,0.405*tp),(1.3025*tp,0.405*tp),(1.3025*tp,0.500*tp),(1.3925*tp,0.500*tp),(1.3925*tp,0.315*tp),(0.545*tp,0.315*tp),(0.545*tp,0.125*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.430*tp,1.960*tp),(0.430*tp,2.210*tp),(0.570*tp,2.210*tp),(0.570*tp,1.960*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.455*tp,2.2975*tp),(0.455*tp,2.595*tp),(0.595*tp,2.595*tp),(0.595*tp,2.685*tp),(0.450*tp,2.685*tp),(0.450*tp,2.725*tp),(0.285*tp,2.725*tp),(0.285*tp,3.3975*tp),(0.500*tp,3.3975*tp),(0.500*tp,3.3075*tp),(0.375*tp,3.3075*tp),(0.375*tp,2.815*tp),(0.540*tp,2.815*tp),(0.540*tp,2.775*tp),(0.685*tp,2.775*tp),(0.685*tp,2.505*tp),(0.545*tp,2.505*tp),(0.545*tp,2.2975*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.965*tp,1.430*tp),(0.965*tp,1.570*tp),(1.2225*tp,1.570*tp),(1.2225*tp,1.430*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.405*tp,0.730*tp),(1.405*tp,0.915*tp),(1.605*tp,0.915*tp),(1.605*tp,1.005*tp),(1.290*tp,1.005*tp),(1.290*tp,1.320*tp),(1.510*tp,1.320*tp),(1.510*tp,1.455*tp),(1.3125*tp,1.455*tp),(1.3125*tp,1.545*tp),(1.600*tp,1.545*tp),(1.600*tp,1.230*tp),(1.380*tp,1.230*tp),(1.380*tp,1.095*tp),(1.695*tp,1.095*tp),(1.695*tp,0.825*tp),(1.495*tp,0.825*tp),(1.495*tp,0.730*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.900*tp,3.400*tp),(1.900*tp,3.600*tp),(2.000*tp,3.600*tp),(2.000*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.000*tp,3.400*tp),(0.000*tp,3.600*tp),(0.100*tp,3.600*tp),(0.100*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.290*tp,3.675*tp),(1.290*tp,3.975*tp),(1.430*tp,3.975*tp),(1.430*tp,3.675*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.575*tp,3.675*tp),(0.575*tp,3.970*tp),(0.715*tp,3.970*tp),(0.715*tp,3.675*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.575*tp,4.530*tp),(0.575*tp,4.875*tp),(0.715*tp,4.875*tp),(0.715*tp,4.670*tp),(1.290*tp,4.670*tp),(1.290*tp,4.870*tp),(1.430*tp,4.870*tp),(1.430*tp,4.530*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.400*tp,5.100*tp),(0.400*tp,6.500*tp),(0.540*tp,6.500*tp),(0.540*tp,5.100*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.575*tp,4.730*tp),(0.575*tp,5.030*tp),(0.400*tp,5.030*tp),(0.400*tp,5.170*tp),(0.715*tp,5.170*tp),(0.715*tp,4.730*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.500*tp,3.470*tp),(1.500*tp,3.560*tp),(1.635*tp,3.560*tp),(1.635*tp,3.685*tp),(1.900*tp,3.685*tp),(1.900*tp,3.490*tp),(1.810*tp,3.490*tp),(1.810*tp,3.595*tp),(1.725*tp,3.595*tp),(1.725*tp,3.470*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.270*tp,3.470*tp),(0.270*tp,3.595*tp),(0.190*tp,3.595*tp),(0.190*tp,3.490*tp),(0.100*tp,3.490*tp),(0.100*tp,3.685*tp),(0.360*tp,3.685*tp),(0.360*tp,3.560*tp),(0.500*tp,3.560*tp),(0.500*tp,3.470*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.455*tp,2.2175*tp),(1.455*tp,2.425*tp),(1.360*tp,2.425*tp),(1.360*tp,2.705*tp),(1.460*tp,2.705*tp),(1.460*tp,2.815*tp),(1.625*tp,2.815*tp),(1.625*tp,3.3075*tp),(1.500*tp,3.3075*tp),(1.500*tp,3.3975*tp),(1.715*tp,3.3975*tp),(1.715*tp,2.725*tp),(1.550*tp,2.725*tp),(1.550*tp,2.615*tp),(1.450*tp,2.615*tp),(1.450*tp,2.515*tp),(1.545*tp,2.515*tp),(1.545*tp,2.2175*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.430*tp,1.880*tp),(1.430*tp,2.130*tp),(1.570*tp,2.130*tp),(1.570*tp,1.880*tp)])

        return elems         

class M0M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=ls.M0,shape=[(0.350*tp,1.500*tp),(0.350*tp,6.500*tp),(0.650*tp,6.500*tp),(0.650*tp,1.500*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.000*tp,6.350*tp),(0.000*tp,6.650*tp),(2.000*tp,6.650*tp),(2.000*tp,6.350*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.125*tp,6.000*tp),(1.125*tp,6.040*tp),(1.875*tp,6.040*tp),(1.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.125*tp,1.000*tp),(0.125*tp,1.040*tp),(0.875*tp,1.040*tp),(0.875*tp,1.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,1.125*tp),(0.960*tp,1.875*tp),(1.000*tp,1.875*tp),(1.000*tp,1.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,2.125*tp),(0.960*tp,2.875*tp),(1.000*tp,2.875*tp),(1.000*tp,2.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,3.125*tp),(0.960*tp,3.875*tp),(1.000*tp,3.875*tp),(1.000*tp,3.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,4.125*tp),(0.960*tp,4.875*tp),(1.000*tp,4.875*tp),(1.000*tp,4.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,5.125*tp),(0.960*tp,5.875*tp),(1.000*tp,5.875*tp),(1.000*tp,5.125*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.300*tp,5.205*tp),(1.300*tp,6.895*tp),(1.700*tp,6.895*tp),(1.700*tp,5.205*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.875*tp,5.300*tp),(0.875*tp,5.700*tp),(1.325*tp,5.700*tp),(1.325*tp,5.300*tp)])
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=IXPORT,shape=[(1.450*tp,-0.005*tp),(1.450*tp,0.005*tp),(1.550*tp,0.005*tp),(1.550*tp,-0.005*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.995*tp,3.450*tp),(1.995*tp,3.550*tp),(2.005*tp,3.550*tp),(2.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(-0.005*tp,3.450*tp),(-0.005*tp,3.550*tp),(0.005*tp,3.550*tp),(0.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.335*tp,3.875*tp),(1.335*tp,3.925*tp),(1.385*tp,3.925*tp),(1.385*tp,3.875*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.620*tp,3.875*tp),(0.620*tp,3.925*tp),(0.670*tp,3.925*tp),(0.670*tp,3.875*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.475*tp,2.330*tp),(0.475*tp,2.385*tp),(0.530*tp,2.385*tp),(0.530*tp,2.330*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.475*tp,2.250*tp),(1.475*tp,2.305*tp),(1.535*tp,2.305*tp),(1.535*tp,2.250*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.350*tp,1.475*tp),(1.350*tp,1.525*tp),(1.400*tp,1.525*tp),(1.400*tp,1.475*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.470*tp,0.150*tp),(0.470*tp,0.205*tp),(0.525*tp,0.205*tp),(0.525*tp,0.150*tp)])
       
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,1.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,2.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,6.695*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,6.265*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,5.835*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,5.405*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.075*tp,5.500*tp),transformation=ls.r180)
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.385*tp,4.945*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.33*tp,1.835*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.88*tp,1.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.755*tp,5.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.975*tp,1.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.27*tp,0.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.265*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.455*tp,4.615*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.445*tp,3.84*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.07*tp,3.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.865*tp,4.705*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.435*tp,4.455*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.865*tp,4.425*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.665*tp,1.895*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.15*tp,4.44*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.84*tp,2.655*tp),transformation=ls.r270)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.74*tp,2.62*tp),transformation=ls.r270)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.12*tp,2.62*tp),transformation=ls.r270)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.555*tp,4.145*tp),transformation=ls.r270)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.115*tp,2.66*tp),transformation=ls.r270)
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_175(),midpoint=(1.36*tp,3.845*tp))
        elems += spira.SRef(bias.ib_175(),midpoint=(0.645*tp,3.845*tp))
        elems += spira.SRef(bias.ib_175(),midpoint=(0.500*tp,1.13*tp),transformation=ls.r180)

        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(1.555*tp,0.615*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(1.385*tp,3.56*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(0.615*tp,3.56*tp),transformation=ls.r180)

        return elems
        
class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(res.res_2(),midpoint=(1.43*tp,1.500*tp),transformation=ls.r90)
        elems += spira.SRef(res.res_2(),midpoint=(1.500*tp,2.335*tp),transformation=ls.r180)
        elems += spira.SRef(res.res_2(),midpoint=(0.500*tp,2.415*tp),transformation=ls.r180)
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 2):
                if ((x == 0 and y in [1,6])):
                    elems += spira.SRef(tb.tr_bias_pillar_M0M6(),midpoint=(0+x*tp,0+y*tp))
                elif ((x == 0 and y in [2,3,4,5]) or (x == 1 and y == 6)):
                    elems += spira.SRef(tb.tr_u_M4_alt(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(tb.tr_M7(),midpoint=(0+x*tp,0+y*tp))
                else:
                    elems += spira.SRef(tb.tr_u_M4_NPTL(),midpoint=(0+x*tp,0+y*tp))
        return elems

sys.stdout.write("Adjusting settings.\n")
F = RDD.FILTERS.OUTPUT.PORTS
F['cell_ports'] = False
F['edge_ports'] = False
F['contact_ports'] = False
F = RDD.FILTERS.PCELL.DEVICE
F['boolean'] = True
F['contact_attach'] = True
F = RDD.FILTERS.PCELL.CIRCUIT
F['boolean'] = False

D = PCELL()
sys.stdout.write("Writing output.\n")
D.gdsii_output(os.path.splitext(__file__)[0])