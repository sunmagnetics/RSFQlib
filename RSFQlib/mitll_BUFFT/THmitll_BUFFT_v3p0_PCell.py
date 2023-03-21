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
    __name_prefix__ = "THmitll_BUFFT_v3p0"
    def create_elements(self, elems):
        M6M5Strips = spira.SRef(M6M5_strips())
        IXports = spira.SRef(IX_ports())
        jjs = spira.SRef(junctions())
        ib = spira.SRef(biasing())
        jj_fill = spira.SRef(junction_fill())
        m4m5m6m7 = spira.SRef(M4M5M6M7_connections())
        m5m6 = spira.SRef(M5M6_connections())
        rs =  spira.SRef(resistors())
        ind = spira.SRef(inductors())
        tblocks = spira.SRef(trackblocks())
        elems += [M6M5Strips, IXports, jjs, ib, jj_fill, m4m5m6m7, m5m6, rs, ind, tblocks]
        
        # Text Labels
        elems += spira.Label(text="P1 M6 M4",position=(1.150*tp,4.500*tp),layer=TEXT)
        elems += spira.Label(text="PB1 M6 M4",position=(0.370*tp,4.895*tp),layer=TEXT)
        elems += spira.Label(text="J1 M6 M5",position=(0.615*tp,4.445*tp),layer=TEXT)
        elems += spira.Label(text="J2 M6 M5",position=(0.490*tp,2.395*tp),layer=TEXT)
        elems += spira.Label(text="PB2 M6 M4",position=(0.375*tp,1.420*tp),layer=TEXT)
        elems += spira.Label(text="J3 M6 M5",position=(1.470*tp,1.500*tp),layer=TEXT)
        elems += spira.Label(text="P2 M6 M4",position=(1.500*tp,1.230*tp),layer=TEXT)

        # LVS Labels
        elems += spira.Label(text='VDD',position=(0.500*tp,0.045*tp),layer=spira.Layer(number=50,datatype=0))
        elems += spira.Label(text='VDD',position=(0.500*tp,6.960*tp),layer=spira.Layer(number=50,datatype=0))
        elems += spira.Label(text='GND',position=(0.345*tp,6.935*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='RB1',position=(0.610*tp,4.795*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB2',position=(0.895*tp,2.400*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB3',position=(1.470*tp,1.805*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB1',position=(0.370*tp,5.570*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB2',position=(0.370*tp,1.080*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RD',position=(1.500*tp,1.130*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='a',position=(1.500*tp,4.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='q',position=(1.500*tp,0.500*tp),layer=spira.Layer(number=60,datatype=5))
        return elems
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(1.280*tp,4.280*tp),(1.060*tp,4.500*tp),(1.280*tp,4.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.280*tp,0.720*tp),(1.500*tp,0.940*tp),(1.720*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.700*tp,4.420*tp),(0.700*tp,4.580*tp),(1.290*tp,4.580*tp),(1.290*tp,4.420*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.300*tp,6.200*tp),(0.300*tp,6.570*tp),(0.570*tp,6.570*tp),(0.570*tp,6.430*tp),(0.440*tp,6.430*tp),(0.440*tp,6.200*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.300*tp,4.5325*tp),(0.300*tp,4.965*tp),(0.440*tp,4.965*tp),(0.440*tp,4.6725*tp),(0.520*tp,4.6725*tp),(0.520*tp,4.5325*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.535*tp,1.565*tp),(0.535*tp,1.655*tp),(0.955*tp,1.655*tp),(0.955*tp,1.705*tp),(1.355*tp,1.705*tp),(1.355*tp,1.615*tp),(1.045*tp,1.615*tp),(1.045*tp,1.565*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.300*tp,0.430*tp),(0.300*tp,0.755*tp),(0.440*tp,0.755*tp),(0.440*tp,0.570*tp),(0.570*tp,0.570*tp),(0.570*tp,0.430*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.300*tp,1.340*tp),(0.300*tp,1.680*tp),(0.535*tp,1.680*tp),(0.535*tp,1.540*tp),(0.440*tp,1.540*tp),(0.440*tp,1.340*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.4475*tp,1.540*tp),(0.4475*tp,2.320*tp),(0.6225*tp,2.320*tp),(0.6225*tp,1.540*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.430*tp,1.170*tp),(1.430*tp,1.385*tp),(1.570*tp,1.385*tp),(1.570*tp,1.170*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.3925*tp,2.480*tp),(0.3925*tp,2.7425*tp),(0.6325*tp,2.7425*tp),(0.6325*tp,2.8425*tp),(0.2875*tp,2.8425*tp),(0.2875*tp,3.1075*tp),(0.6275*tp,3.1075*tp),(0.6275*tp,3.2125*tp),(0.3325*tp,3.2125*tp),(0.3325*tp,3.4625*tp),(0.6225*tp,3.4625*tp),(0.6225*tp,3.5775*tp),(0.3325*tp,3.5775*tp),(0.3325*tp,3.8525*tp),(0.6275*tp,3.8525*tp),(0.6275*tp,3.9525*tp),(0.2875*tp,3.9525*tp),(0.2875*tp,4.2375*tp),(0.6275*tp,4.2375*tp),(0.6275*tp,4.345*tp),(0.7125*tp,4.345*tp),(0.7125*tp,4.1525*tp),(0.3725*tp,4.1525*tp),(0.3725*tp,4.0375*tp),(0.7125*tp,4.0375*tp),(0.7125*tp,3.7675*tp),(0.4175*tp,3.7675*tp),(0.4175*tp,3.6625*tp),(0.7075*tp,3.6625*tp),(0.7075*tp,3.3775*tp),(0.4175*tp,3.3775*tp),(0.4175*tp,3.2975*tp),(0.7125*tp,3.2975*tp),(0.7125*tp,3.0225*tp),(0.3725*tp,3.0225*tp),(0.3725*tp,2.9275*tp),(0.7175*tp,2.9275*tp),(0.7175*tp,2.6575*tp),(0.4775*tp,2.6575*tp),(0.4775*tp,2.480*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.420*tp,0.720*tp),(1.420*tp,1.095*tp),(1.580*tp,1.095*tp),(1.580*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.400*tp,6.400*tp),(0.400*tp,7.000*tp),(0.600*tp,7.000*tp),(0.600*tp,6.400*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.400*tp,0.000*tp),(0.400*tp,0.600*tp),(0.600*tp,0.600*tp),(0.600*tp,0.000*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.300*tp,5.205*tp),(1.300*tp,6.895*tp),(1.700*tp,6.895*tp),(1.700*tp,5.205*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.875*tp,3.300*tp),(0.875*tp,3.700*tp),(1.390*tp,3.700*tp),(1.390*tp,3.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.880*tp,5.300*tp),(0.880*tp,5.700*tp),(1.340*tp,5.700*tp),(1.340*tp,5.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.875*tp,6.300*tp),(0.875*tp,6.700*tp),(1.325*tp,6.700*tp),(1.325*tp,6.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.300*tp,2.840*tp),(1.300*tp,4.100*tp),(1.700*tp,4.100*tp),(1.700*tp,2.840*tp)])
        return elems           

class M6M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=0.400*tp,height=1.690*tp,center=(1.500*tp,6.050*tp))
        elems += spira.Box(layer=ls.M5,width=0.515*tp,height=0.400*tp,center=(1.1325*tp,3.500*tp))
        elems += spira.Box(layer=ls.M5,width=0.460*tp,height=0.400*tp,center=(1.110*tp,5.500*tp))
        elems += spira.Box(layer=ls.M5,width=0.450*tp,height=0.400*tp,center=(1.100*tp,6.500*tp))
        elems += spira.Box(layer=ls.M5,width=0.400*tp,height=1.260*tp,center=(1.500*tp,3.470*tp))

        return elems
        
class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.16*tp,center=(1.150*tp,4.5*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.055*tp,height=0.050*tp,center=(1.4975*tp,1.230*tp))
        elems += spira.Box(layer=IXPORT,width=0.055*tp,height=0.045*tp,center=(0.3725*tp,4.8975*tp))
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.050*tp,center=(0.370*tp,1.415*tp))
        return elems        
        
class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_092_sg(),midpoint=(0.485*tp,2.4*tp),transformation=ls.r270,alias='J1')
        elems += spira.SRef(jj.jj_160_sg(),midpoint=(0.615*tp,4.440*tp),alias='J3')
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(1.470*tp,1.5*tp),alias='J2')
        return elems
        
class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_112(),midpoint=(0.370*tp,6.330*tp),transformation=ls.r180,alias='bias1')
        elems += spira.SRef(bias.ib_218(),midpoint=(0.370*tp,0.630*tp),alias='bias2')
        return elems
        
        
class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,5.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,6.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,4.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,3.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,2.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,1.000*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,6.265*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,5.405*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,5.835*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,6.695*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.075*tp,6.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.080*tp,5.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,3.040*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,3.470*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,3.900*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.075*tp,3.500*tp),transformation=ls.r90)
        return elems       
        
class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.330*tp,4.935*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.695*tp,5.830*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.740*tp,5.330*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.695*tp,0.855*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.880*tp,1.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.860*tp,0.330*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.140*tp,0.330*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.120*tp,1.440*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.260*tp,2.385*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.585*tp,2.400*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.875*tp,2.305*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.260*tp,3.380*tp),transformation=ls.r90)
        return elems        
        
class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(0.585*tp,6.585*tp),transformation=ls.r180,alias='via1')
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(0.585*tp,0.585*tp),transformation=ls.r180,alias='via2')
        return elems
        
class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(res.res_1p36(),midpoint=(1.5*tp,1.285*tp),transformation=ls.r180,alias='R1')
        return elems
        
class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 2):
                if (x == 1 and y in [0,4]):
                    elems += spira.SRef(tb.tr_PTL_conn(),midpoint=(0+x*tp,0+y*tp))
                else:
                    elems += spira.SRef(tb.tr_u_M4(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(tb.tr_M7(),midpoint=(0+x*tp,0+y*tp))
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