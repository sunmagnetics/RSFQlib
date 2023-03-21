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
    __name_prefix__ = "THmitll_DCSFQ-PTLTX_v3p0"
    def create_elements(self, elems):
        M6M5Strips = spira.SRef(M6M5_strips())
        IXports = spira.SRef(IX_ports())
        M0M4M7tracks = spira.SRef(M0M4M7_tracks())
        jjfill = spira.SRef(junction_fill())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        vias = spira.SRef(M5M6_connections())
        ib = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        rs = spira.SRef(resistors())
        ind = spira.SRef(inductors())
        tblocks = spira.SRef(trackblocks())
        elems += [M6M5Strips, IXports, M0M4M7tracks, jjfill, M4M5M6M7conns,
                  vias, ib, jjs, rs, ind, tblocks]
        
        # Text Labels
        elems += spira.Label(text='J2 M6 M5',position=(1.425*tp,3.605*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB1 M6 M4',position=(0.500*tp,4.75*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J1 M5 M6',position=(0.500*tp,3.83*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J3 M6 M5',position=(1.15*tp,2.475*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J4 M6 M5',position=(0.500*tp,1.64*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P2 M6 M4',position=(0.500*tp,1.29*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB2 M6 M4',position=(1.500*tp,1.27*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P1 M6 M4',position=(0.000*tp,3.505*tp),layer=spira.Layer(number=182,datatype=0))
        
        # LVS Labels
        elems += spira.Label(text='q',position=(0.500*tp,0.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='a',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='RD',position=(0.505*tp,1.19*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB2',position=(1.425*tp,3.89*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB1',position=(0.500*tp,5.04*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB2',position=(1.500*tp,1.04*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB4',position=(0.500*tp,1.935*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB3',position=(0.87*tp,2.47*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB1',position=(0.495*tp,4.11*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='VDD',position=(1.500*tp,0.045*tp),layer=spira.Layer(number=50,datatype=0))
        elems += spira.Label(text='VDD',position=(0.500*tp,6.96*tp),layer=spira.Layer(number=50,datatype=0))
        elems += spira.Label(text='GND',position=(0.33*tp,6.915*tp),layer=spira.Layer(number=40,datatype=0))
        return elems
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(0.280*tp,0.720*tp),(0.500*tp,0.940*tp),(0.720*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.610*tp,3.960*tp),(0.610*tp,4.060*tp),(0.750*tp,4.060*tp),(0.750*tp,4.600*tp),(0.440*tp,4.600*tp),(0.440*tp,4.700*tp),(0.850*tp,4.700*tp),(0.850*tp,3.960*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.615*tp,1.545*tp),(0.615*tp,1.655*tp),(1.500*tp,1.655*tp),(1.500*tp,1.545*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.270*tp,2.5075*tp),(1.270*tp,2.5925*tp),(1.5775*tp,2.5925*tp),(1.5775*tp,2.8875*tp),(1.6275*tp,2.8875*tp),(1.6275*tp,3.2025*tp),(1.3025*tp,3.2025*tp),(1.3025*tp,3.485*tp),(1.3875*tp,3.485*tp),(1.3875*tp,3.2875*tp),(1.7125*tp,3.2875*tp),(1.7125*tp,2.8025*tp),(1.6625*tp,2.8025*tp),(1.6625*tp,2.5075*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.6975*tp,3.5075*tp),(0.6975*tp,3.6775*tp),(0.610*tp,3.6775*tp),(0.610*tp,3.8825*tp),(0.9025*tp,3.8825*tp),(0.9025*tp,3.7125*tp),(1.310*tp,3.7125*tp),(1.310*tp,3.5075*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.435*tp,1.600*tp),(1.435*tp,2.285*tp),(1.190*tp,2.285*tp),(1.190*tp,2.415*tp),(1.565*tp,2.415*tp),(1.565*tp,1.600*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.000*tp,3.400*tp),(0.000*tp,3.600*tp),(0.570*tp,3.600*tp),(0.570*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.420*tp,0.850*tp),(0.420*tp,1.155*tp),(0.580*tp,1.155*tp),(0.580*tp,0.850*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.450*tp,1.230*tp),(0.450*tp,1.530*tp),(0.550*tp,1.530*tp),(0.550*tp,1.230*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.440*tp,0.430*tp),(1.440*tp,0.865*tp),(1.560*tp,0.865*tp),(1.560*tp,0.430*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.440*tp,1.195*tp),(1.440*tp,1.600*tp),(1.560*tp,1.600*tp),(1.560*tp,1.195*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.430*tp,5.275*tp),(0.430*tp,6.570*tp),(0.570*tp,6.570*tp),(0.570*tp,5.275*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.430*tp,3.415*tp),(0.430*tp,3.700*tp),(0.570*tp,3.700*tp),(0.570*tp,3.415*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.290*tp,2.600*tp),(0.290*tp,3.150*tp),(0.595*tp,3.150*tp),(0.595*tp,3.330*tp),(0.415*tp,3.330*tp),(0.415*tp,3.430*tp),(0.695*tp,3.430*tp),(0.695*tp,3.050*tp),(0.390*tp,3.050*tp),(0.390*tp,2.600*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.400*tp,6.415*tp),(0.400*tp,7.000*tp),(0.600*tp,7.000*tp),(0.600*tp,6.415*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.400*tp,0.000*tp),(1.400*tp,0.585*tp),(1.600*tp,0.585*tp),(1.600*tp,0.000*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.300*tp,4.775*tp),(1.300*tp,6.895*tp),(1.700*tp,6.895*tp),(1.700*tp,4.775*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.870*tp,5.300*tp),(0.870*tp,5.700*tp),(1.335*tp,5.700*tp),(1.335*tp,5.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.875*tp,6.300*tp),(0.875*tp,6.700*tp),(1.325*tp,6.700*tp),(1.325*tp,6.300*tp)])
        return elems        

class M6M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=0.400*tp,height=2.120*tp,center=(1.500*tp,5.835*tp))
        elems += spira.Box(layer=ls.M5,width=0.465*tp,height=0.400*tp,center=(1.1025*tp,5.500*tp))
        elems += spira.Box(layer=ls.M5,width=0.450*tp,height=0.400*tp,center=(1.100*tp,6.500*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0.000*tp,height=0.110*tp,center=(0.000*tp,3.500*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.050*tp,center=(0.500*tp,4.750*tp))
        elems += spira.Box(layer=IXPORT,width=0.060*tp,height=0.055*tp,center=(1.500*tp,1.2675*tp))
        elems += spira.Box(layer=IXPORT,width=0.060*tp,height=0.050*tp,center=(0.500*tp,1.290*tp))
       
        return elems

class M0M4M7_tracks(spira.Cell):
    __name_prefix__ = "M0M4M7_tracks"
    def create_elements(self, elems):
        shape=spira.Shape(points=[(0.720*tp,4.040*tp),(0.720*tp,4.280*tp),(0.960*tp,4.280*tp),(0.960*tp,4.125*tp),(0.875*tp,4.125*tp),(0.875*tp,4.040*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape=spira.Shape(points=[(0.720*tp,3.720*tp),(0.720*tp,3.960*tp),(0.875*tp,3.960*tp),(0.875*tp,3.875*tp),(0.960*tp,3.875*tp),(0.960*tp,3.720*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,1.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,2.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.07*tp,5.500*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,6.695*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,6.265*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,5.835*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,5.405*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,4.975*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.075*tp,6.500*tp),transformation=ls.r270)
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.89*tp,0.435*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.265*tp,5.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.88*tp,2.35*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.265*tp,4.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.22*tp,4.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.56*tp,4.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.875*tp,4.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.44*tp,2.77*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.875*tp,3.385*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.265*tp,6.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.300*tp,2.355*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.875*tp,1.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.88*tp,0.335*tp),transformation=ls.r90)
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(0.415*tp,6.415*tp))
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(0.415*tp,3.415*tp))
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(1.415*tp,0.415*tp))
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_275(),midpoint=(0.500*tp,5.395*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_350(),midpoint=(1.500*tp,1.325*tp),transformation=ls.r180)
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(0.500*tp,1.645*tp))
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(1.155*tp,2.47*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_225_s(),midpoint=(0.500*tp,3.825*tp))
        elems += spira.SRef(jj.jj_225_sg(),midpoint=(1.425*tp,3.600*tp))
        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(res.res_1p36(),midpoint=(0.500*tp,1.04*tp),alias='R1')
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 2):
                if (x == 0 and y == 0):
                    pass
                else:
                    elems += spira.SRef(tb.tr_u_M4(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(tb.tr_M7(),midpoint=(0+x*tp,0+y*tp))
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(0.000*tp,0.000*tp),alias='Q')
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