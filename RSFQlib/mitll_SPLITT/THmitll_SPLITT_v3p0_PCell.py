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
    __name_prefix__ = "THmitll_SPLITT_v3p0"
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
        elems += spira.Label(text='PB1 M6 M4',position=(0.65*tp,4.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J4 M6 M5',position=(1.275*tp,1.43*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J2 M6 M5',position=(0.500*tp,3.405*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J3 M6 M5',position=(1.385*tp,2.565*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P3 M6 M4',position=(1.715*tp,1.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P1 M6 M4',position=(0.500*tp,6.15*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J1 M6 M5',position=(0.500*tp,5.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB2 M6 M4',position=(1.500*tp,3.26*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P2 M6 M4',position=(1.715*tp,2.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB3 M6 M4',position=(1.565*tp,0.625*tp),layer=spira.Layer(number=182,datatype=0))
        
        # LVS Labels
        elems += spira.Label(text='q1',position=(2.500*tp,1.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='q0',position=(2.500*tp,2.505*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='a',position=(0.500*tp,6.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='RIB1',position=(0.975*tp,4.495*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB4',position=(0.985*tp,1.43*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB2',position=(0.765*tp,3.405*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB3',position=(1.385*tp,2.28*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RD2',position=(1.815*tp,1.500*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB1',position=(0.775*tp,5.500*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB2',position=(1.500*tp,3.735*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RD1',position=(1.82*tp,2.500*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB3',position=(2.06*tp,0.62*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='VDD',position=(1.500*tp,6.96*tp),layer=spira.Layer(number=50,datatype=0))
        elems += spira.Label(text='VDD',position=(2.500*tp,0.04*tp),layer=spira.Layer(number=50,datatype=0))
        elems += spira.Label(text='GND',position=(1.335*tp,6.96*tp),layer=spira.Layer(number=40,datatype=0))
        return elems
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(2.285*tp,2.280*tp),(2.065*tp,2.500*tp),(2.285*tp,2.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.280*tp,1.280*tp),(2.060*tp,1.500*tp),(2.280*tp,1.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.500*tp,6.060*tp),(0.280*tp,6.280*tp),(0.720*tp,6.280*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.500*tp,4.430*tp),(0.500*tp,4.570*tp),(0.740*tp,4.570*tp),(0.740*tp,4.430*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.265*tp,4.430*tp),(1.265*tp,4.570*tp),(1.500*tp,4.570*tp),(1.500*tp,4.430*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.440*tp,4.500*tp),(0.440*tp,5.400*tp),(0.560*tp,5.400*tp),(0.560*tp,4.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.555*tp,3.505*tp),(0.555*tp,3.705*tp),(0.385*tp,3.705*tp),(0.385*tp,4.025*tp),(0.620*tp,4.025*tp),(0.620*tp,4.205*tp),(0.455*tp,4.205*tp),(0.455*tp,4.500*tp),(0.545*tp,4.500*tp),(0.545*tp,4.295*tp),(0.710*tp,4.295*tp),(0.710*tp,3.935*tp),(0.475*tp,3.935*tp),(0.475*tp,3.795*tp),(0.645*tp,3.795*tp),(0.645*tp,3.505*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.420*tp,2.380*tp),(0.420*tp,3.385*tp),(0.580*tp,3.385*tp),(0.580*tp,2.380*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.500*tp,2.3225*tp),(0.500*tp,2.4375*tp),(1.270*tp,2.4375*tp),(1.270*tp,2.3225*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.030*tp,1.550*tp),(1.030*tp,1.640*tp),(0.390*tp,1.640*tp),(0.390*tp,2.400*tp),(0.610*tp,2.400*tp),(0.610*tp,1.860*tp),(1.250*tp,1.860*tp),(1.250*tp,1.550*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.420*tp,4.095*tp),(1.420*tp,6.570*tp),(1.580*tp,6.570*tp),(1.580*tp,4.095*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.505*tp,0.560*tp),(1.505*tp,0.940*tp),(1.285*tp,0.940*tp),(1.285*tp,1.310*tp),(1.405*tp,1.310*tp),(1.405*tp,1.060*tp),(1.625*tp,1.060*tp),(1.625*tp,0.560*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.389*tp,1.455*tp),(1.389*tp,1.555*tp),(1.775*tp,1.555*tp),(1.775*tp,1.455*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.420*tp,0.300*tp),(2.420*tp,0.690*tp),(2.580*tp,0.690*tp),(2.580*tp,0.300*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.340*tp,2.670*tp),(1.340*tp,3.060*tp),(1.440*tp,3.060*tp),(1.440*tp,3.325*tp),(1.560*tp,3.325*tp),(1.560*tp,2.940*tp),(1.460*tp,2.940*tp),(1.460*tp,2.670*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.490*tp,2.450*tp),(1.490*tp,2.550*tp),(1.775*tp,2.550*tp),(1.775*tp,2.450*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.855*tp,2.420*tp),(1.855*tp,2.580*tp),(2.150*tp,2.580*tp),(2.150*tp,2.420*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.855*tp,1.420*tp),(1.855*tp,1.580*tp),(2.150*tp,1.580*tp),(2.150*tp,1.420*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.420*tp,5.600*tp),(0.420*tp,6.150*tp),(0.580*tp,6.150*tp),(0.580*tp,5.600*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.400*tp,0.000*tp),(2.400*tp,0.455*tp),(2.600*tp,0.455*tp),(2.600*tp,0.000*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.400*tp,6.415*tp),(1.400*tp,7.000*tp),(1.600*tp,7.000*tp),(1.600*tp,6.415*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.730*tp,6.305*tp),(1.730*tp,6.705*tp),(2.570*tp,6.705*tp),(2.570*tp,6.305*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.730*tp,5.295*tp),(1.730*tp,5.695*tp),(2.570*tp,5.695*tp),(2.570*tp,5.295*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.730*tp,4.305*tp),(1.730*tp,4.705*tp),(2.570*tp,4.705*tp),(2.570*tp,4.305*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.730*tp,3.295*tp),(1.730*tp,3.695*tp),(2.570*tp,3.695*tp),(2.570*tp,3.295*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.500*tp,0.290*tp),(0.500*tp,0.690*tp),(1.340*tp,0.690*tp),(1.340*tp,0.290*tp)])
        return elems         

class M6M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=0.840*tp,height=0.400*tp,center=(2.150*tp,6.505*tp))
        elems += spira.Box(layer=ls.M5,width=0.840*tp,height=0.400*tp,center=(2.150*tp,5.495*tp))
        elems += spira.Box(layer=ls.M5,width=0.840*tp,height=0.400*tp,center=(2.150*tp,4.505*tp))
        elems += spira.Box(layer=ls.M5,width=0.840*tp,height=0.400*tp,center=(2.150*tp,3.495*tp))
        elems += spira.Box(layer=ls.M5,width=0.840*tp,height=0.400*tp,center=(0.920*tp,0.490*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0.160*tp,height=0.000*tp,center=(0.500*tp,6.150*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.050*tp,center=(1.715*tp,1.500*tp))
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.050*tp,center=(0.650*tp,4.500*tp))
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.050*tp,center=(1.500*tp,3.260*tp))
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.055*tp,center=(1.715*tp,2.4975*tp))
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.050*tp,center=(1.560*tp,0.625*tp))
       
        return elems

class M0M4M7_tracks(spira.Cell):
    __name_prefix__ = "M0M4M7_tracks"
    def create_elements(self, elems):
        shape=spira.Shape(points=[(0.720*tp,1.720*tp),(0.720*tp,1.960*tp),(0.875*tp,1.960*tp),(0.875*tp,1.875*tp),(0.960*tp,1.875*tp),(0.960*tp,1.720*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape=spira.Shape(points=[(1.040*tp,1.720*tp),(1.040*tp,1.875*tp),(1.125*tp,1.875*tp),(1.125*tp,1.960*tp),(1.280*tp,1.960*tp),(1.280*tp,1.720*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,1.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,1.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,2.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.93*tp,4.505*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.37*tp,6.505*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.37*tp,4.505*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.93*tp,3.495*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.37*tp,5.495*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.37*tp,3.495*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.93*tp,5.495*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.93*tp,6.505*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.14*tp,0.49*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.700*tp,0.49*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,1.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,6.000*tp),transformation=ls.r180)
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.335*tp,2.955*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.27*tp,2.325*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.875*tp,6.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.565*tp,0.795*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,5.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.88*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.57*tp,4.84*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.88*tp,4.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.88*tp,3.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.655*tp,0.12*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.33*tp,0.325*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,3.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.875*tp,0.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.265*tp,4.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.22*tp,6.59*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.665*tp,2.06*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.175*tp,0.44*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.53*tp,1.56*tp),transformation=ls.r180)
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(1.415*tp,6.415*tp))
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.585*tp,0.285*tp),transformation=ls.r90)
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_231(),midpoint=(0.600*tp,4.500*tp),transformation=ls.r270)
        elems += spira.SRef(bias.ib_175(),midpoint=(1.500*tp,3.205*tp))
        elems += spira.SRef(bias.ib_175(),midpoint=(2.51*tp,0.625*tp),transformation=ls.r90)
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_136_sg(),midpoint=(0.505*tp,3.44*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(1.275*tp,1.43*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(1.385*tp,2.57*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_160_sg(),midpoint=(0.505*tp,5.500*tp),transformation=ls.r270)
        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(res.res_1p36(),midpoint=(1.97*tp,1.500*tp),transformation=ls.r90,alias='R2')
        elems += spira.SRef(res.res_1p36(),midpoint=(1.66*tp,2.500*tp),transformation=ls.r270,alias='R1')
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 3):
                if (x == 0 and y == 6) or (x == 2 and y in [1,2]):
                    pass
                else:
                    elems += spira.SRef(tb.tr_u_M4(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(tb.tr_M7(),midpoint=(0+x*tp,0+y*tp))
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(0.000*tp,6.000*tp),alias='A')
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(2.000*tp,1.000*tp),alias='Q1')
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(2.000*tp,2.000*tp),alias='Q0')
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