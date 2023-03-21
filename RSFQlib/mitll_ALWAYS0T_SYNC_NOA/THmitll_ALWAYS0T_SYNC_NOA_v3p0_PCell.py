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
    __name_prefix__ = "THmitll_ALWAYS0T_SYNC_NOA_v3p0"
    def create_elements(self, elems):
        ix_ports = spira.SRef(IX_ports())
        m5m6_strips = spira.SRef(M6M5_strips())
        jfill = spira.SRef(junction_fill())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        rs = spira.SRef(resistors())
        ind = spira.SRef(inductors())
        tblocks = spira.SRef(trackblocks())
        elems += [ix_ports, m5m6_strips, jfill, M4M5M6M7conns, rs, ind, tblocks]
        
        # Text Labels
        elems += spira.Label(text="P1 M6 M4",position=(0.500*tp,3.150*tp),layer=TEXT)
        elems += spira.Label(text="PR1 M6 M4",position=(0.500*tp,2.595*tp),layer=TEXT)
        elems += spira.Label(text="P2 M6 M4",position=(0.500*tp,0.850*tp),layer=TEXT)
        elems += spira.Label(text="PR2 M6 M4",position=(0.500*tp,1.410*tp),layer=TEXT)

        # LVS Labels
        elems += spira.Label(text='R1',position=(0.500*tp,2.490*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='R2',position=(0.500*tp,1.510*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='GND',position=(0.500*tp,0.100*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='clk',position=(0.500*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='q',position=(0.500*tp,0.500*tp),layer=spira.Layer(number=60,datatype=5))
        sys.stdout.write("Constructing layout.\n")
        return elems
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(0.500*tp,3.060*tp),(0.280*tp,3.280*tp),(0.720*tp,3.280*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.280*tp,0.720*tp),(0.500*tp,0.940*tp),(0.720*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.430*tp,1.555*tp),(0.430*tp,1.825*tp),(0.570*tp,1.825*tp),(0.570*tp,1.555*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.420*tp,0.720*tp),(0.420*tp,1.470*tp),(0.580*tp,1.470*tp),(0.580*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.430*tp,2.175*tp),(0.430*tp,2.445*tp),(0.570*tp,2.445*tp),(0.570*tp,2.175*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.420*tp,2.530*tp),(0.420*tp,3.280*tp),(0.580*tp,3.280*tp),(0.580*tp,2.530*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.300*tp,6.065*tp),(0.300*tp,6.895*tp),(0.700*tp,6.895*tp),(0.700*tp,6.065*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.300*tp,4.100*tp),(0.300*tp,5.360*tp),(0.700*tp,5.360*tp),(0.700*tp,4.100*tp)])
        return elems         
        
class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0.160*tp,height=0.000*tp,center=(0.500*tp,0.850*tp),alias='Q')
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.050*tp,center=(0.500*tp,1.4075*tp))
        elems += spira.Box(layer=IXPORT,width=0.160*tp,height=0.000*tp,center=(0.500*tp,3.150*tp),alias='CLK')
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.050*tp,center=(0.500*tp,2.595*tp))
        return elems            
        
class M6M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=0.400*tp,height=0.830*tp,center=(0.5*tp,6.480*tp))
        elems += spira.Box(layer=ls.M5,width=0.400*tp,height=1.260*tp,center=(0.5*tp,4.730*tp))

        return elems            

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding 3um junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,6.265*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,6.695*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,5.160*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,4.730*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,4.300*tp),transformation=ls.r180)
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.560*tp,5.490*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.335*tp,5.750*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.560*tp,2.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.880*tp,2.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.260*tp,1.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.880*tp,1.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.665*tp,2.205*tp),transformation=ls.r180,alias='CLKZERO')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.665*tp,1.935*tp),transformation=ls.r180,alias='QZERO')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.660*tp,3.985*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.435*tp,5.630*tp),transformation=ls.r180)

        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        sys.stdout.write("Adding resistors.\n")
        elems += spira.SRef(res.res_2(),midpoint=(0.5*tp,1.675*tp),transformation=ls.r180,alias='R2')
        elems += spira.SRef(res.res_2(),midpoint=(0.5*tp,2.650*tp),transformation=ls.r180,alias='R1')
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            if y != 0 or y != 3:
                elems += spira.SRef(tb.tr_u_M4(),midpoint=(0.0,0+y*tp))
                elems += spira.SRef(tb.tr_M7(),midpoint=(0.0,0+y*tp))
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(0.000,0+0.000*tp),alias='Q')
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(0.000,0+3.000*tp),alias='CLK')
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