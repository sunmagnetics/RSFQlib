import sys
# Change this to the location that contains the subcells.py folder
subcell_path = '..\\subcells'
if subcell_path not in sys.path:
    sys.path.append(subcell_path)
import subcells as sc
import os
import spira.all as spira
from spira.technologies.mit.process.database import RDD

IXPORT = spira.RDD.PLAYER.IXPORT
TEXT = spira.Layer(number=182)

## Parameterization
# Trackpitch in microns
tp = 10
sc.tp = tp

# Inductor widths
Scaling = (1+(tp-10)*0.25)
L1_width = 0.2105*tp*Scaling
L4_width = L1_width
L2L3_width = 0.115*tp*Scaling
L2L3n_width = 0.165*tp*Scaling
LBias_width = 0.20228260869565218*tp*Scaling

class JTL(spira.PCell):
    __name_prefix__ = "LSmitll_JTL_v2p1"
    def create_elements(self, elems):
        p1, p2, pb1 = self.get_ports()
        elems += spira.SRef(M4M5M6M7_connections())
        elems += spira.SRef(junction_fill())
        tblocks = spira.SRef(trackblocks())
        pbps = spira.Port(name='PBPS', midpoint=tblocks.ports['M6:E2'].midpoint, orientation=180, process=spira.RDD.PROCESS.M6)
        elems += tblocks
        elems += spira.SRef(M0_blocks())
        elems += spira.Box(layer=sc.M0, width=3.0*tp, height=0.3*tp, center=(1.5*tp,6.5*tp))
        elems += spira.Box(layer=sc.M0, width=0.2*tp, height=2.0*tp, center=(1.5*tp,5.5*tp))
        elems += spira.Box(layer=sc.M0, width=0.75*tp, height=0.04*tp, center=(0.5*tp,6.02*tp))
        elems += spira.Box(layer=sc.M0, width=0.75*tp, height=0.04*tp, center=(2.5*tp,6.02*tp))
        elems += spira.Box(layer=sc.M0, width=0.04*tp, height=1.75*tp, center=(1.02*tp,5.0*tp))
        elems += spira.Box(layer=sc.M0, width=0.04*tp, height=1.75*tp, center=(1.98*tp,5.0*tp))
        elems += spira.Box(layer=sc.M0, width=0.75*tp, height=0.04*tp, center=(1.5*tp,4.02*tp))
        sys.stdout.write("Adding bias.\n")
        bias = spira.SRef(sc.ls_ib_350(), midpoint=(1.5*tp, 3.575*tp))
        pbs = spira.Port(name="PBN", midpoint=bias.ports[10].midpoint, process=spira.RDD.PROCESS.M6)
        pbn = spira.Port(name="PBN", midpoint=bias.ports[4].midpoint, process=spira.RDD.PROCESS.M6)
        elems += bias
        sys.stdout.write("Adding junctions.\n")
        jj1 = spira.SRef(sc.ls_jj_250_sg(), midpoint=(0.5*tp,2.555*tp), transformation=sc.spira.Rotation(180), alias="jj1")
        jj2 = spira.SRef(sc.ls_jj_250_sg(), midpoint=(2.5*tp,2.555*tp), transformation=sc.spira.Rotation(180), alias="jj2")
        pjj1n = spira.Port(name="PJJ1N", midpoint=jj1.ports[18].midpoint, process=spira.RDD.PROCESS.M6)
        pjj1e = spira.Port(name="PJJ1E", midpoint=jj1.ports[17].midpoint, process=spira.RDD.PROCESS.M6)
        pjj2n = spira.Port(name="PJJ2N", midpoint=jj2.ports[18].midpoint, process=spira.RDD.PROCESS.M6)
        pjj2w = spira.Port(name="PJJ1W", midpoint=jj2.ports[19].midpoint, orientation=180, process=spira.RDD.PROCESS.M6)
        elems += jj1
        elems += jj2
        sys.stdout.write("Adding inductors.\n")
        L1 = spira.Route90(port1=p1, port2=pjj1n, layer=sc.M6, width=L1_width)
        L4 = spira.Route90(port1=p2, port2=pjj2n, layer=sc.M6, width=L4_width)
        L2L3 = spira.Route90(port1=pjj1e, port2=pjj2w, layer=sc.M6, width=L2L3_width)
        pl2l3n = spira.Port(name="PL2L3N", midpoint=L2L3.edge_ports[3].midpoint, process=spira.RDD.PROCESS.M6)
        L2L3N = spira.Route90(port1=pl2l3n, port2=pbs, layer=sc.M6, width=L2L3n_width)
        LBias = spira.Route90(port1=pbn, port2=pbps, layer=sc.M6, width=LBias_width)
        elems += [L1, L2L3, L2L3N, L4, LBias]
        elems += spira.Box(layer=sc.M6, width=0.025*tp, height=0.315*tp, center=(0.0125*tp, 2.4925*tp))
        elems += spira.Box(layer=sc.M6, width=0.025*tp, height=0.315*tp, center=(2.9875*tp, 2.4925*tp))
        elems += spira.Box(layer=IXPORT, width=0.0, height=0.2*tp, center=(0.0,3.5*tp))
        elems += spira.Box(layer=IXPORT, width=0.0, height=0.2*tp, center=(3.0*tp,3.5*tp))
        elems += spira.Box(layer=IXPORT, width=0.05*tp, height=0.05*tp, center=(1.5*tp,3.63*tp))
        sys.stdout.write("Adding labels.\n")
        elems += spira.Label(text="bias_in", position=(0.0, 6.5*tp), layer=spira.Layer(number=182))
        elems += spira.Label(text="bias_out", position=(3.0*tp, 6.5*tp), layer=spira.Layer(number=182))
        elems += spira.Label(text="a", position=(0.0, 3.5*tp), layer=spira.Layer(number=182))
        elems += spira.Label(text="P1 M6 M4", position=(0.0, 3.5*tp), layer=spira.Layer(number=182))
        elems += spira.Label(text="PB1 M6 M4", position=(1.5*tp, 3.6325*tp), layer=spira.Layer(number=182))
        elems += spira.Label(text="Q", position=(3.0*tp, 3.5*tp), layer=spira.Layer(number=182))
        elems += spira.Label(text="P2 M6 M4", position=(3.0*tp, 3.5*tp), layer=spira.Layer(number=182))
        elems += spira.Label(text="J1 M6 M5", position=(0.5*tp, 2.555*tp), layer=spira.Layer(number=182))
        elems += spira.Label(text="J2 M6 M5", position=(2.5*tp, 2.555*tp), layer=spira.Layer(number=182))
        sys.stdout.write("Constructing layout.\n")
        return elems

    @spira.cache()
    def get_ports(self):
        p1 = spira.Port(name="P1", width=0.02*tp, length=0.2*tp, orientation=0, midpoint=(0.0,3.5*tp), process=spira.RDD.PROCESS.M6)    
        p2 = spira.Port(name="P2", width=0.02*tp, length=0.2*tp, orientation=180, midpoint=(3.0*tp,3.5*tp), process=spira.RDD.PROCESS.M6)
        pb1 = spira.Port(name="PB1", width=0.05*tp, length=0.05*tp, orientation=0, midpoint=(1.5*tp,3.63*tp), process=spira.RDD.PROCESS.M6)

        return [p1, p2, pb1]

    def create_ports(self, ports):
        ports += self.get_ports()
        return ports

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding 3um junction fill.\n")
        for y in range(0, 7):
            for x in range(0, 3): 
                if y > 1 and y < 4:
                    pass
                else:
                    if y == 4 and x == 1:
                        pass
                    else:
                        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(), midpoint=((0.5+x)*tp,(0.5+y)*tp))
        sys.stdout.write("Adding 1.5um junction fill.\n")
        for y in range (1, 7):
            for x in range(1, 3):
                elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(), midpoint=(0.0+x*tp,0.0+y*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        for x in range(0, 3):
            for y in range(1, 7):
                if y > 1 and y < 5:
                    if y == 3 and x != 1:
                        elems += spira.SRef(sc.ls_conn_M4M5M6M7(), midpoint=((0.665+x)*tp,(0.93+y)*tp), transformation=sc.r180)
                else:
                    elems += spira.SRef(sc.ls_conn_M4M5M6M7(), midpoint=((0.665+x)*tp,(0.07+y)*tp), transformation=sc.r180)
        for x in range(1, 3):
            for y in range(0, 7):
                if y > 1 and y < 4:
                    pass
                else:
                    elems += spira.SRef(sc.ls_conn_M4M5M6M7(), midpoint=((0.07+x)*tp,(0.335+y)*tp), transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(), midpoint=(0.875*tp,3.335*tp), transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(), midpoint=(1.265*tp,3.335*tp), transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(), midpoint=(1.875*tp,3.335*tp), transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(), midpoint=(2.265*tp,3.335*tp), transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(), midpoint=(0.165*tp,2.335*tp), transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(), midpoint=(2.975*tp,2.335*tp), transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(), midpoint=(1.57*tp,1.95*tp), transformation=sc.r90)
        return elems

class M0_blocks(spira.Cell):
    __name_prefix__ = "M0_blocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding M0 trackblocks.\n")
        for y in range(0, 6):
            for x in range(0, 3):
                if x == 1 and y > 3:
                    pass
                else:
                    elems += spira.SRef(sc.ls_tr_M0(), midpoint=(0+x*tp,0+y*tp))
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 3):
                if x == 1 and y == 4:
                    elems += spira.SRef(sc.ls_tr_bias_pillar_M0M6(), midpoint=(0+x*tp,0+y*tp))
                else:
                    elems += spira.SRef(sc.ls_tr_u_M4_alt(), midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(sc.ls_tr_M7(), midpoint=(0+x*tp,0+y*tp))
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

D = JTL()
sys.stdout.write("Writing output.\n")
D.gdsii_output('./LSmitll_JTL_v2p1_PCell')