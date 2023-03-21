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
    __name_prefix__ = "THmitll_SPLIT_v3p0"
    def create_elements(self, elems):
        M0M4M7strips = spira.SRef(M0M4M7_strips())
        M0M5Strips = spira.SRef(M0M5_strips())
        IXports = spira.SRef(IX_ports())
        jjfill = spira.SRef(junction_fill())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        ib = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        ind = spira.SRef(inductors())
        tblocks = spira.SRef(trackblocks())
        elems += [M0M4M7strips, M0M5Strips, IXports, jjfill, M4M5M6M7conns, ib, jjs, ind, tblocks]

        # Text Labels
        elems += spira.Label(text='J1 M6 M5',position=(0.605*tp,2.575*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J2 M6 M5',position=(1.375*tp,3.43*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J3 M6 M5',position=(1.27*tp,1.09*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB1 M6 M4',position=(0.365*tp,1.78*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB3 M6 M4',position=(0.605*tp,1.785*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB2 M6 M4',position=(1.625*tp,4.275*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P1 M6 M4',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P2 M6 M4',position=(2.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P3 M6 M4',position=(1.500*tp,0.000*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='q1',position=(1.500*tp,0.000*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='q0',position=(2.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='a',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        
        # LVS Labels
        elems += spira.Label(text='VDD',position=(1.955*tp,6.500*tp),layer=spira.Layer(number=1,datatype=0))
        elems += spira.Label(text='GND',position=(1.97*tp,6.315*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='q1',position=(1.500*tp,0.000*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='q0',position=(2.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='a',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='RIB2',position=(1.63*tp,4.74*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB1',position=(0.37*tp,1.35*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB3',position=(0.600*tp,1.355*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB1',position=(0.615*tp,2.285*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB3',position=(1.27*tp,0.785*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB2',position=(1.39*tp,3.74*tp),layer=spira.Layer(number=52,datatype=11))
        return elems
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(1.2975*tp,1.280*tp),(1.1975*tp,1.380*tp),(1.2975*tp,1.380*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.150*tp,3.350*tp),(0.100*tp,3.400*tp),(0.150*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.100*tp,3.600*tp),(0.150*tp,3.650*tp),(0.150*tp,3.600*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.950*tp,2.315*tp),(0.950*tp,2.550*tp),(0.710*tp,2.550*tp),(0.710*tp,2.650*tp),(1.050*tp,2.650*tp),(1.050*tp,2.415*tp),(1.500*tp,2.415*tp),(1.500*tp,2.315*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.1975*tp,1.380*tp),(1.1975*tp,1.700*tp),(1.300*tp,1.700*tp),(1.300*tp,2.365*tp),(1.500*tp,2.365*tp),(1.500*tp,1.500*tp),(1.3975*tp,1.500*tp),(1.3975*tp,1.380*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.3325*tp,2.390*tp),(1.3325*tp,3.320*tp),(1.4675*tp,3.320*tp),(1.4675*tp,2.390*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.000*tp,3.400*tp),(0.000*tp,3.600*tp),(0.500*tp,3.600*tp),(0.500*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.900*tp,3.400*tp),(1.900*tp,3.600*tp),(2.000*tp,3.600*tp),(2.000*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.5925*tp,3.2875*tp),(1.5925*tp,3.4225*tp),(1.500*tp,3.4225*tp),(1.500*tp,3.5175*tp),(1.6875*tp,3.5175*tp),(1.6875*tp,3.3825*tp),(1.805*tp,3.3825*tp),(1.805*tp,3.5975*tp),(1.900*tp,3.5975*tp),(1.900*tp,3.5025*tp),(1.900*tp,3.5025*tp),(1.900*tp,3.2875*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.485*tp,3.5975*tp),(1.485*tp,3.6875*tp),(1.580*tp,3.6875*tp),(1.580*tp,4.340*tp),(1.670*tp,4.340*tp),(1.670*tp,3.5975*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.010*tp,1.130*tp),(1.010*tp,1.295*tp),(0.560*tp,1.295*tp),(0.560*tp,1.855*tp),(0.660*tp,1.855*tp),(0.660*tp,1.395*tp),(1.110*tp,1.395*tp),(1.110*tp,1.230*tp),(1.200*tp,1.230*tp),(1.200*tp,1.130*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.540*tp,0.700*tp),(0.540*tp,0.975*tp),(0.680*tp,0.975*tp),(0.680*tp,0.700*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.295*tp,0.695*tp),(0.295*tp,0.950*tp),(0.435*tp,0.950*tp),(0.435*tp,0.695*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.295*tp,1.710*tp),(0.295*tp,2.4575*tp),(0.490*tp,2.4575*tp),(0.490*tp,2.3175*tp),(0.435*tp,2.3175*tp),(0.435*tp,1.710*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.400*tp,0.135*tp),(1.400*tp,0.365*tp),(1.480*tp,0.365*tp),(1.480*tp,0.8225*tp),(1.380*tp,0.8225*tp),(1.380*tp,1.0525*tp),(1.710*tp,1.0525*tp),(1.710*tp,0.135*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.400*tp,0.000*tp),(1.400*tp,0.250*tp),(1.600*tp,0.250*tp),(1.600*tp,0.000*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.390*tp,5.105*tp),(1.390*tp,6.295*tp),(1.530*tp,6.295*tp),(1.530*tp,5.245*tp),(1.690*tp,5.245*tp),(1.690*tp,5.105*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.360*tp,2.630*tp),(0.360*tp,3.600*tp),(0.640*tp,3.600*tp),(0.640*tp,2.630*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.2925*tp,1.180*tp),(1.2925*tp,1.405*tp),(1.3975*tp,1.405*tp),(1.3975*tp,1.180*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.150*tp,3.350*tp),(0.150*tp,3.650*tp),(0.640*tp,3.650*tp),(0.640*tp,3.350*tp)])

        return elems           
        
class M0M4M7_strips(spira.Cell):
    __name_prefix__ = "M0M4M7_strips"
    def create_elements(self, elems):
        shape = spira.Shape(points=[(1.125*tp,1.040*tp),(1.125*tp,1.125*tp),(1.040*tp,1.125*tp),(1.040*tp,1.280*tp),(1.280*tp,1.280*tp),(1.280*tp,1.040*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(1.040*tp,0.720*tp),(1.040*tp,0.875*tp),(1.125*tp,0.875*tp),(1.125*tp,0.960*tp),(1.280*tp,0.960*tp),(1.280*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        return elems        

class M0M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=ls.M5,shape=[(0.300*tp,4.345*tp),(0.300*tp,6.895*tp),(0.700*tp,6.895*tp),(0.700*tp,4.345*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.300*tp,4.300*tp),(0.300*tp,4.700*tp),(1.135*tp,4.700*tp),(1.135*tp,4.300*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.000*tp,6.350*tp),(0.000*tp,6.650*tp),(2.000*tp,6.650*tp),(2.000*tp,6.350*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.350*tp,0.500*tp),(0.350*tp,6.500*tp),(0.650*tp,6.500*tp),(0.650*tp,0.500*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.125*tp,6.000*tp),(1.125*tp,6.040*tp),(1.875*tp,6.040*tp),(1.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,5.125*tp),(0.960*tp,5.875*tp),(1.000*tp,5.875*tp),(1.000*tp,5.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,4.125*tp),(0.960*tp,4.875*tp),(1.000*tp,4.875*tp),(1.000*tp,4.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,3.125*tp),(0.960*tp,3.875*tp),(1.000*tp,3.875*tp),(1.000*tp,3.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,2.125*tp),(0.960*tp,2.875*tp),(1.000*tp,2.875*tp),(1.000*tp,2.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,1.125*tp),(0.960*tp,1.875*tp),(1.000*tp,1.875*tp),(1.000*tp,1.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,0.125*tp),(0.960*tp,0.875*tp),(1.000*tp,0.875*tp),(1.000*tp,0.125*tp)])
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=IXPORT,shape=[(-0.005*tp,3.450*tp),(-0.005*tp,3.550*tp),(0.005*tp,3.550*tp),(0.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.995*tp,3.450*tp),(1.995*tp,3.550*tp),(2.005*tp,3.550*tp),(2.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.450*tp,-0.005*tp),(1.450*tp,0.005*tp),(1.550*tp,0.005*tp),(1.550*tp,-0.005*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.340*tp,1.750*tp),(0.340*tp,1.805*tp),(0.390*tp,1.805*tp),(0.390*tp,1.750*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.585*tp,1.750*tp),(0.585*tp,1.805*tp),(0.640*tp,1.805*tp),(0.640*tp,1.750*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.600*tp,4.250*tp),(1.600*tp,4.300*tp),(1.655*tp,4.300*tp),(1.655*tp,4.250*tp)])
       
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,2.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,3.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,4.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,6.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,5.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,4.545*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,4.975*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,5.405*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,5.835*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,6.265*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,6.695*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.935*tp,4.500*tp),transformation=ls.r180)
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.875*tp,2.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.875*tp,1.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.99*tp,0.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.875*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.275*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.445*tp,4.67*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.445*tp,4.22*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.965*tp,5.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.05*tp,6.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.115*tp,3.575*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.66*tp,4.185*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.66*tp,3.905*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.095*tp,1.675*tp),transformation=ls.r180)
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_175(),midpoint=(1.625*tp,4.22*tp))
        elems += spira.SRef(bias.ib_175(),midpoint=(0.61*tp,1.835*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_175(),midpoint=(0.365*tp,1.835*tp),transformation=ls.r180)
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(1.385*tp,3.435*tp))
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(0.61*tp,2.57*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(1.27*tp,1.075*tp),transformation=ls.r180)
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 2):
                if ((x == 0 and y == 0) or (x == 1 and y == 6)):
                    elems += spira.SRef(tb.tr_bias_pillar_M0M6(),midpoint=(0+x*tp,0+y*tp))
                elif (x == 0 and y in range(1,7)):
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