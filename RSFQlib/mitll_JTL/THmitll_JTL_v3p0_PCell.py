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
    __name_prefix__ = "THmitll_JTL_v3p0"
    def create_elements(self, elems):
        M0M5Strips = spira.SRef(M0M5_strips())
        IXports = spira.SRef(IX_ports())
        jjfill = spira.SRef(junction_fill())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        ib = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        ind = spira.SRef(inductors())
        tblocks = spira.SRef(trackblocks())
        elems += [M0M5Strips, IXports, jjfill, M4M5M6M7conns, ib, jjs, ind, tblocks]

        # Text Labels
        elems += spira.Label(text='PB1 M6 M4',position=(0.500*tp,5.13*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P1 M6 M4',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P2 M6 M4',position=(2.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J1 M6 M5',position=(0.615*tp,3.56*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J2 M6 M5',position=(1.39*tp,3.555*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='a',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='q',position=(2.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        
        # LVS Labels
        elems += spira.Label(text='VDD',position=(1.900*tp,6.500*tp),layer=spira.Layer(number=1,datatype=0))
        elems += spira.Label(text='GND',position=(1.915*tp,6.69*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='RIB1',position=(0.51*tp,5.375*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB1',position=(0.605*tp,3.285*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB2',position=(1.395*tp,3.265*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='a',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='q',position=(2.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        return elems
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(0.000*tp,3.400*tp),(0.000*tp,3.600*tp),(0.200*tp,3.600*tp),(0.200*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.800*tp,3.400*tp),(1.800*tp,3.600*tp),(2.000*tp,3.600*tp),(2.000*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.110*tp,3.310*tp),(0.110*tp,3.455*tp),(0.000*tp,3.455*tp),(0.000*tp,3.545*tp),(0.200*tp,3.545*tp),(0.200*tp,3.400*tp),(0.495*tp,3.400*tp),(0.495*tp,3.310*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.505*tp,3.310*tp),(1.505*tp,3.400*tp),(1.800*tp,3.400*tp),(1.800*tp,3.545*tp),(2.000*tp,3.545*tp),(2.000*tp,3.455*tp),(1.890*tp,3.455*tp),(1.890*tp,3.310*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.430*tp,5.530*tp),(0.430*tp,6.305*tp),(0.570*tp,6.305*tp),(0.570*tp,5.530*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.930*tp,4.355*tp),(0.930*tp,4.575*tp),(0.430*tp,4.575*tp),(0.430*tp,5.200*tp),(0.570*tp,5.200*tp),(0.570*tp,4.715*tp),(1.070*tp,4.715*tp),(1.070*tp,4.355*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.3275*tp,3.680*tp),(1.3275*tp,4.2875*tp),(1.000*tp,4.2875*tp),(1.000*tp,4.4425*tp),(1.4825*tp,4.4425*tp),(1.4825*tp,3.680*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.525*tp,3.675*tp),(0.525*tp,4.440*tp),(1.000*tp,4.440*tp),(1.000*tp,4.290*tp),(0.675*tp,4.290*tp),(0.675*tp,3.675*tp)])

        return elems        

class M0M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=ls.M0,shape=[(0.000*tp,6.350*tp),(0.000*tp,6.650*tp),(2.000*tp,6.650*tp),(2.000*tp,6.350*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.125*tp,6.000*tp),(0.125*tp,6.040*tp),(0.875*tp,6.040*tp),(0.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.125*tp,6.000*tp),(1.125*tp,6.040*tp),(1.875*tp,6.040*tp),(1.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.300*tp,0.110*tp),(0.300*tp,2.230*tp),(0.700*tp,2.230*tp),(0.700*tp,0.110*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.300*tp,0.110*tp),(1.300*tp,2.230*tp),(1.700*tp,2.230*tp),(1.700*tp,0.110*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.690*tp,0.300*tp),(0.690*tp,0.700*tp),(1.310*tp,0.700*tp),(1.310*tp,0.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.690*tp,1.300*tp),(0.690*tp,1.700*tp),(1.310*tp,1.700*tp),(1.310*tp,1.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.300*tp,5.200*tp),(1.300*tp,6.890*tp),(1.700*tp,6.890*tp),(1.700*tp,5.200*tp)])
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=IXPORT,shape=[(-0.005*tp,3.450*tp),(-0.005*tp,3.550*tp),(0.005*tp,3.550*tp),(0.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.995*tp,3.450*tp),(1.995*tp,3.550*tp),(2.005*tp,3.550*tp),(2.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.475*tp,5.105*tp),(0.475*tp,5.155*tp),(0.525*tp,5.155*tp),(0.525*tp,5.105*tp)])
       
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,5.400*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,5.83*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,6.26*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,6.69*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.025*tp,2.51*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.000*tp,0.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.000*tp,1.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,2.03*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,1.600*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,1.17*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,0.74*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,0.31*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,2.03*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,1.600*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,1.17*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,0.74*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,0.31*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,6.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,5.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,4.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,3.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,2.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,1.000*tp),transformation=ls.r180)
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,2.37*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.875*tp,4.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.265*tp,4.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.265*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.875*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.165*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.665*tp,5.08*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.83*tp,2.495*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.68*tp,2.785*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.715*tp,2.81*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.72*tp,2.49*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.615*tp,4.755*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.93*tp,3.665*tp),transformation=ls.r270)
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_350(),midpoint=(0.500*tp,5.655*tp),transformation=ls.r180)
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(1.39*tp,3.56*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(0.61*tp,3.56*tp),transformation=ls.r180)

        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 2):
                if ((x == 0 and y == 6)):
                    elems += spira.SRef(tb.tr_bias_pillar_M0M6(),midpoint=(0+x*tp,0+y*tp))
                elif (x == 1 and y == 6):
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