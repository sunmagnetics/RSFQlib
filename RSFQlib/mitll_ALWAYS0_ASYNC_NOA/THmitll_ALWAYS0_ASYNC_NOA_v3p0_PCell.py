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
    __name_prefix__ = "THmitll_ALWAYS0_ASYNC_NOA_v3p0"
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
        elems += spira.Label(text='P1 M6 M4',position=(1.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J1 M6 M5',position=(0.39*tp,3.565*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB1 M6 M4',position=(0.500*tp,3.900*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PR1 M6 M4',position=(0.500*tp,2.315*tp),layer=spira.Layer(number=182,datatype=0))
        
        # LVS Labels
        elems += spira.Label(text='VDD',position=(0.96*tp,6.500*tp),layer=spira.Layer(number=1,datatype=0))
        elems += spira.Label(text='GND',position=(0.96*tp,6.325*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='q',position=(1.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='RB1',position=(0.385*tp,3.275*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB1',position=(0.500*tp,4.395*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='R1',position=(0.500*tp,2.205*tp),layer=spira.Layer(number=52,datatype=11))
        return elems
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(0.900*tp,3.400*tp),(0.810*tp,3.490*tp),(0.900*tp,3.490*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.900*tp,3.400*tp),(0.900*tp,3.600*tp),(1.000*tp,3.600*tp),(1.000*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.330*tp,3.680*tp),(0.330*tp,3.970*tp),(0.575*tp,3.970*tp),(0.575*tp,3.830*tp),(0.470*tp,3.830*tp),(0.470*tp,3.680*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.400*tp,4.725*tp),(0.400*tp,6.500*tp),(0.600*tp,6.500*tp),(0.600*tp,4.725*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.500*tp,3.470*tp),(0.500*tp,3.560*tp),(0.615*tp,3.560*tp),(0.615*tp,3.695*tp),(0.900*tp,3.695*tp),(0.900*tp,3.490*tp),(0.810*tp,3.490*tp),(0.810*tp,3.605*tp),(0.705*tp,3.605*tp),(0.705*tp,3.470*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.430*tp,1.905*tp),(0.430*tp,2.165*tp),(0.570*tp,2.165*tp),(0.570*tp,1.905*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.455*tp,2.250*tp),(0.455*tp,2.545*tp),(0.720*tp,2.545*tp),(0.720*tp,2.615*tp),(0.625*tp,2.615*tp),(0.625*tp,3.3075*tp),(0.500*tp,3.3075*tp),(0.500*tp,3.3975*tp),(0.715*tp,3.3975*tp),(0.715*tp,2.705*tp),(0.810*tp,2.705*tp),(0.810*tp,2.455*tp),(0.545*tp,2.455*tp),(0.545*tp,2.250*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.300*tp,0.105*tp),(0.300*tp,1.365*tp),(0.700*tp,1.365*tp),(0.700*tp,0.105*tp)])

        return elems           

class M0M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=ls.M5,shape=[(0.300*tp,0.105*tp),(0.300*tp,1.365*tp),(0.700*tp,1.365*tp),(0.700*tp,0.105*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.000*tp,6.350*tp),(0.000*tp,6.650*tp),(1.000*tp,6.650*tp),(1.000*tp,6.350*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.125*tp,6.000*tp),(0.125*tp,6.040*tp),(0.875*tp,6.040*tp),(0.875*tp,6.000*tp)])
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=IXPORT,shape=[(0.995*tp,3.450*tp),(0.995*tp,3.550*tp),(1.005*tp,3.550*tp),(1.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.475*tp,3.875*tp),(0.475*tp,3.925*tp),(0.525*tp,3.925*tp),(0.525*tp,3.875*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.475*tp,2.290*tp),(0.475*tp,2.345*tp),(0.525*tp,2.345*tp),(0.525*tp,2.290*tp)])
       
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,1.165*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,0.735*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,0.305*tp),transformation=ls.r180)
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,5.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.88*tp,5.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,4.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.88*tp,4.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,2.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.665*tp,1.935*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.435*tp,1.63*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.895*tp,1.63*tp),transformation=ls.r180)
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_175(),midpoint=(0.500*tp,4.85*tp),transformation=ls.r180)

        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(0.385*tp,3.56*tp),transformation=ls.r180)

        return elems
        
class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(res.res_2(),midpoint=(0.500*tp,2.37*tp),transformation=ls.r180)
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 1):
                if ((x == 0 and y == 6)):
                    elems += spira.SRef(tb.tr_bias_pillar_M0M6(),midpoint=(0+x*tp,0+y*tp))
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