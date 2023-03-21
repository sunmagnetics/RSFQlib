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
    __name_prefix__ = "THmitll_DCSFQ_v3p0"
    def create_elements(self, elems):
        M0M4M7strips = spira.SRef(M0M4M7_strips())
        M0M5Strips = spira.SRef(M0M5_strips())
        IXports = spira.SRef(IX_ports())
        jjfill = spira.SRef(junction_fill())
        vias = spira.SRef(M0M6_connections())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        ib = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        ind = spira.SRef(inductors())
        tblocks = spira.SRef(trackblocks())
        elems += [M0M4M7strips, M0M5Strips, IXports, jjfill, vias, M4M5M6M7conns, ib, jjs, ind, tblocks]

        # Text Labels
        elems += spira.Label(text='J2 M6 M5',position=(0.74*tp,4.545*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J3 M6 M5',position=(1.43*tp,3.3588*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='a',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='q',position=(1.9975*tp,3.5075*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P1 M6 M4',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P2 M6 M4',position=(2.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J1 M5 M6',position=(0.500*tp,3.775*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB1 M6 M4',position=(0.500*tp,4.995*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB2 M6 M4',position=(1.565*tp,4.475*tp),layer=spira.Layer(number=182,datatype=0))
        
        # LVS Labels
        elems += spira.Label(text='RB2',position=(1.025*tp,4.54*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB3',position=(1.43*tp,3.0388*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB1',position=(0.795*tp,3.78*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB1',position=(0.500*tp,5.300*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB2',position=(1.565*tp,4.895*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='GND',position=(1.485*tp,6.895*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='VDD',position=(1.955*tp,6.500*tp),layer=spira.Layer(number=1,datatype=0))
        elems += spira.Label(text='q',position=(2.0025*tp,3.4925*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='a',position=(0.000*tp,3.495*tp),layer=spira.Layer(number=60,datatype=5))
        return elems
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(0.100*tp,3.400*tp),(0.100*tp,3.450*tp),(0.150*tp,3.450*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.100*tp,3.550*tp),(0.100*tp,3.600*tp),(0.150*tp,3.550*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.805*tp,3.400*tp),(1.805*tp,3.600*tp),(2.000*tp,3.600*tp),(2.000*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.500*tp,3.185*tp),(1.500*tp,3.275*tp),(1.625*tp,3.275*tp),(1.625*tp,3.400*tp),(1.805*tp,3.400*tp),(1.805*tp,3.545*tp),(2.000*tp,3.545*tp),(2.000*tp,3.455*tp),(1.895*tp,3.455*tp),(1.895*tp,3.310*tp),(1.715*tp,3.310*tp),(1.715*tp,3.185*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.000*tp,3.400*tp),(0.000*tp,3.600*tp),(0.100*tp,3.600*tp),(0.100*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.000*tp,3.450*tp),(0.000*tp,3.550*tp),(0.500*tp,3.550*tp),(0.500*tp,3.450*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.5325*tp,3.880*tp),(0.5325*tp,4.450*tp),(0.7175*tp,4.450*tp),(0.7175*tp,3.880*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.4525*tp,3.390*tp),(1.4525*tp,3.590*tp),(1.470*tp,3.590*tp),(1.470*tp,3.750*tp),(1.520*tp,3.750*tp),(1.520*tp,4.530*tp),(1.620*tp,4.530*tp),(1.620*tp,3.650*tp),(1.570*tp,3.650*tp),(1.570*tp,3.490*tp),(1.5525*tp,3.490*tp),(1.5525*tp,3.390*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.215*tp,3.375*tp),(1.215*tp,3.715*tp),(1.295*tp,3.715*tp),(1.295*tp,3.945*tp),(1.355*tp,3.945*tp),(1.355*tp,4.285*tp),(0.895*tp,4.285*tp),(0.895*tp,4.445*tp),(0.985*tp,4.445*tp),(0.985*tp,4.375*tp),(1.445*tp,4.375*tp),(1.445*tp,3.855*tp),(1.385*tp,3.855*tp),(1.385*tp,3.625*tp),(1.305*tp,3.625*tp),(1.305*tp,3.465*tp),(1.340*tp,3.465*tp),(1.340*tp,3.375*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.335*tp,3.780*tp),(0.335*tp,5.040*tp),(0.565*tp,5.040*tp),(0.565*tp,4.920*tp),(0.455*tp,4.920*tp),(0.455*tp,3.780*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.440*tp,5.600*tp),(1.440*tp,6.500*tp),(1.560*tp,6.500*tp),(1.560*tp,5.600*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.435*tp,5.510*tp),(0.435*tp,5.650*tp),(1.500*tp,5.650*tp),(1.500*tp,5.510*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.490*tp,5.300*tp),(1.490*tp,5.510*tp),(1.500*tp,5.510*tp),(1.500*tp,5.650*tp),(1.630*tp,5.650*tp),(1.630*tp,5.300*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.660*tp,4.300*tp),(0.660*tp,4.450*tp),(0.760*tp,4.450*tp),(0.760*tp,4.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.415*tp,3.420*tp),(0.415*tp,3.650*tp),(0.585*tp,3.650*tp),(0.585*tp,3.420*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.4475*tp,2.195*tp),(0.4475*tp,3.500*tp),(0.5525*tp,3.500*tp),(0.5525*tp,2.195*tp)])

        return elems         
        
class M0M4M7_strips(spira.Cell):
    __name_prefix__ = "M0M4M7_strips"
    def create_elements(self, elems):
        shape = spira.Shape(points=[(0.720*tp,3.720*tp),(0.720*tp,3.960*tp),(0.875*tp,3.960*tp),(0.875*tp,3.875*tp),(0.960*tp,3.875*tp),(0.960*tp,3.720*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(1.040*tp,3.720*tp),(1.040*tp,3.875*tp),(1.125*tp,3.875*tp),(1.125*tp,3.960*tp),(1.280*tp,3.960*tp),(1.280*tp,3.720*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        return elems        

class M0M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=ls.M5,shape=[(1.300*tp,0.685*tp),(1.300*tp,2.415*tp),(1.700*tp,2.415*tp),(1.700*tp,0.685*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.155*tp,0.300*tp),(0.155*tp,0.700*tp),(1.845*tp,0.700*tp),(1.845*tp,0.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.300*tp,0.685*tp),(0.300*tp,1.555*tp),(0.700*tp,1.555*tp),(0.700*tp,0.685*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.300*tp,6.060*tp),(0.300*tp,6.890*tp),(0.700*tp,6.890*tp),(0.700*tp,6.060*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.000*tp,6.350*tp),(0.000*tp,6.650*tp),(2.000*tp,6.650*tp),(2.000*tp,6.350*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.125*tp,6.000*tp),(0.125*tp,6.040*tp),(0.875*tp,6.040*tp),(0.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.125*tp,6.000*tp),(1.125*tp,6.040*tp),(1.875*tp,6.040*tp),(1.875*tp,6.000*tp)])
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=IXPORT,shape=[(-0.005*tp,3.450*tp),(-0.005*tp,3.550*tp),(0.005*tp,3.550*tp),(0.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.995*tp,3.450*tp),(1.995*tp,3.550*tp),(2.005*tp,3.550*tp),(2.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.540*tp,4.445*tp),(1.540*tp,4.500*tp),(1.590*tp,4.500*tp),(1.590*tp,4.445*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.475*tp,4.965*tp),(0.475*tp,5.020*tp),(0.525*tp,5.020*tp),(0.525*tp,4.965*tp)])
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,6.69*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,6.26*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,1.355*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,0.925*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,2.215*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,1.785*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,1.355*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,0.925*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.645*tp,0.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.215*tp,0.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.785*tp,0.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.355*tp,0.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,5.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,6.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,3.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,2.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,1.000*tp),transformation=ls.r180)
        return elems
        
class M0M6_connections(spira.Cell):
    __name_prefix__ = "M0M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(0.585*tp,3.545*tp),transformation=ls.r180)
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.265*tp,5.295*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,4.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.88*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.88*tp,4.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.185*tp,2.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.875*tp,2.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.265*tp,2.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.57*tp,1.935*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.665*tp,5.92*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.135*tp,3.48*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.665*tp,1.82*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.165*tp,1.57*tp),transformation=ls.r180)
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_175(),midpoint=(1.565*tp,5.435*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_275(),midpoint=(0.500*tp,5.635*tp),transformation=ls.r180)
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_225_s(),midpoint=(0.500*tp,3.785*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_225_sg(),midpoint=(0.74*tp,4.55*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(1.425*tp,3.335*tp),transformation=ls.r180)
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 2):
                if ((x == 1 and y == 6)):
                    elems += spira.SRef(tb.tr_bias_pillar_M0M6(),midpoint=(0+x*tp,0+y*tp))
                elif (x == 0 and y == 6):
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