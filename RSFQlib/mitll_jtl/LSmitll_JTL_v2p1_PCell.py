
import sys
import spira.all as spira
from spira.technologies.mit.process.database import RDD
from spira.technologies.mit import devices as dev
from spira.yevon.geometry.coord import Coord
# Shorthand for long layer names
M0 = spira.RDD.PLAYER.M0.METAL
I0 = spira.RDD.PLAYER.I0.VIA
M1 = spira.RDD.PLAYER.M1.METAL
I1 = spira.RDD.PLAYER.I1.VIA
M2 = spira.RDD.PLAYER.M2.METAL
I2 = spira.RDD.PLAYER.I2.VIA
M3 = spira.RDD.PLAYER.M3.METAL
I3 = spira.RDD.PLAYER.I3.VIA
M4 = spira.RDD.PLAYER.M4.GND
I4 = spira.RDD.PLAYER.I4.VIA
M5 = spira.RDD.PLAYER.M5.METAL
J5 = spira.RDD.PLAYER.J5.JUNCTION
R5 = spira.RDD.PLAYER.R5.METAL
I5 = spira.RDD.PLAYER.I5.VIA
C5J = spira.RDD.PLAYER.C5J.VIA
C5R = spira.RDD.PLAYER.C5R.VIA
M6 = spira.RDD.PLAYER.M6.METAL
I6 = spira.RDD.PLAYER.I6.VIA
M7 = spira.RDD.PLAYER.M7.METAL
IXPORT = spira.RDD.PLAYER.IXPORT

## Parameterization
# Trackpitch in microns
tp = 10

# Inductor widths
Scaling = (1+(tp-10)*0.25)
L1_width = 0.2105*tp*Scaling
L4_width = L1_width
L2L3_width = 0.115*tp*Scaling
L2L3n_width = 0.165*tp*Scaling
LBias_width = 0.20228260869565218*tp*Scaling

# Common Shapes
lowerHalf = spira.Shape(points=[
    (0.0,0.0),(0.0,0.875),(0.04,0.875),(0.04,0.125),(0.125,0.125),
    (0.125,0.04),(0.875,0.04),(0.875,0.125),(1.0,0.125),(1.0,0.0)
    ])
lowerHalf = [x * tp for x in lowerHalf]
upperHalf = spira.Shape(points=[
    (0.0,1.0),(1.0,1.0),(1.0,0.125),(0.96,0.125),(0.96,0.875),
    (0.875,0.875),(0.875,0.96),(0.125,0.96),(0.125,0.875),(0.0,0.875)
    ])
upperHalf = [x * tp for x in upperHalf]
middleCross = spira.Shape(points=[
    (0.28,0.04),(0.28,0.28),(0.04,0.28),(0.04,0.72),(0.28,0.72),(0.28,0.96),
    (0.72,0.96),(0.72,0.72),(0.96,0.72),(0.96,0.28),(0.72,0.28),(0.72,0.04)
    ])
middleCross = [x * tp for x in middleCross]

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
        elems += spira.Box(layer=M0, width=3.0*tp, height=0.3*tp, center=(1.5*tp,6.5*tp))
        elems += spira.Box(layer=M0, width=0.2*tp, height=2.0*tp, center=(1.5*tp,5.5*tp))
        elems += spira.Box(layer=M0, width=0.75*tp, height=0.04*tp, center=(0.5*tp,6.02*tp))
        elems += spira.Box(layer=M0, width=0.75*tp, height=0.04*tp, center=(2.5*tp,6.02*tp))
        elems += spira.Box(layer=M0, width=0.04*tp, height=1.75*tp, center=(1.02*tp,5.0*tp))
        elems += spira.Box(layer=M0, width=0.04*tp, height=1.75*tp, center=(1.98*tp,5.0*tp))
        elems += spira.Box(layer=M0, width=0.75*tp, height=0.04*tp, center=(1.5*tp,4.02*tp))
        sys.stdout.write("Adding bias.\n")
        bias = spira.SRef(ls_ib_350(), midpoint=(1.5*tp, 3.575*tp))
        pbs = spira.Port(name="PBN", midpoint=bias.ports[10].midpoint, process=spira.RDD.PROCESS.M6)
        pbn = spira.Port(name="PBN", midpoint=bias.ports[4].midpoint, process=spira.RDD.PROCESS.M6)
        elems += bias
        sys.stdout.write("Adding junctions.\n")
        jj1 = spira.SRef(ls_jj250sg(), midpoint=(0.5*tp,2.555*tp), transformation=spira.Rotation(180), alias="jj1")
        jj2 = spira.SRef(ls_jj250sg(), midpoint=(2.5*tp,2.555*tp), transformation=spira.Rotation(180), alias="jj2")
        pjj1n = spira.Port(name="PJJ1N", midpoint=jj1.ports[18].midpoint, process=spira.RDD.PROCESS.M6)
        pjj1e = spira.Port(name="PJJ1E", midpoint=jj1.ports[17].midpoint, process=spira.RDD.PROCESS.M6)
        pjj2n = spira.Port(name="PJJ2N", midpoint=jj2.ports[18].midpoint, process=spira.RDD.PROCESS.M6)
        pjj2w = spira.Port(name="PJJ1W", midpoint=jj2.ports[19].midpoint, orientation=180, process=spira.RDD.PROCESS.M6)
        elems += jj1
        elems += jj2
        sys.stdout.write("Adding inductors.\n")
        L1 = spira.Route90(port1=p1, port2=pjj1n, layer=M6, width=L1_width)
        L4 = spira.Route90(port1=p2, port2=pjj2n, layer=M6, width=L4_width)
        L2L3 = spira.Route90(port1=pjj1e, port2=pjj2w, layer=M6, width=L2L3_width)
        pl2l3n = spira.Port(name="PL2L3N", midpoint=L2L3.edge_ports[3].midpoint, process=spira.RDD.PROCESS.M6)
        L2L3N = spira.Route90(port1=pl2l3n, port2=pbs, layer=M6, width=L2L3n_width)
        LBias = spira.Route90(port1=pbn, port2=pbps, layer=M6, width=LBias_width)
        elems += [L1, L2L3, L2L3N, L4, LBias]
        elems += spira.Box(layer=M6, width=0.025*tp, height=0.315*tp, center=(0.0125*tp, 2.4925*tp))
        elems += spira.Box(layer=M6, width=0.025*tp, height=0.315*tp, center=(2.9875*tp, 2.4925*tp))
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
                        elems += spira.SRef(ls_FakeJJ_3umx3um(), midpoint=((0.5+x)*tp,(0.5+y)*tp))
        sys.stdout.write("Adding 1.5um junction fill.\n")
        for y in range (1, 7):
            for x in range(1, 3):
                elems += spira.SRef(ls_FakeJJ_1p5umx1p5um(), midpoint=(0.0+x*tp,0.0+y*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        T1 = spira.Rotation(90)
        T2 = spira.Rotation(180)
        for x in range(0, 3):
            for y in range(1, 7):
                if y > 1 and y < 5:
                    if y == 3 and x != 1:
                        elems += spira.SRef(ls_conn_M4M5M6M7(), midpoint=((0.665+x)*tp,(0.93+y)*tp), transformation=T2)
                else:
                    elems += spira.SRef(ls_conn_M4M5M6M7(), midpoint=((0.665+x)*tp,(0.07+y)*tp), transformation=T2)
        for x in range(1, 3):
            for y in range(0, 7):
                if y > 1 and y < 4:
                    pass
                else:
                    elems += spira.SRef(ls_conn_M4M5M6M7(), midpoint=((0.07+x)*tp,(0.335+y)*tp), transformation=T1)
        elems += spira.SRef(ls_conn_M4M5M6M7(), midpoint=(0.875*tp,3.335*tp), transformation=T1)
        elems += spira.SRef(ls_conn_M4M5M6M7(), midpoint=(1.265*tp,3.335*tp), transformation=T1)
        elems += spira.SRef(ls_conn_M4M5M6M7(), midpoint=(1.875*tp,3.335*tp), transformation=T1)
        elems += spira.SRef(ls_conn_M4M5M6M7(), midpoint=(2.265*tp,3.335*tp), transformation=T1)
        elems += spira.SRef(ls_conn_M4M5M6M7(), midpoint=(0.165*tp,2.335*tp), transformation=T1)
        elems += spira.SRef(ls_conn_M4M5M6M7(), midpoint=(2.975*tp,2.335*tp), transformation=T1)
        elems += spira.SRef(ls_conn_M4M5M6M7(), midpoint=(1.57*tp,1.95*tp), transformation=T1)
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
                    elems += spira.SRef(ls_tr_M0(), midpoint=(0+x*tp,0+y*tp))
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 3):
                if x == 1 and y == 4:
                    elems += spira.SRef(ls_tr_bias_pillar_M0M6(), midpoint=(0+x*tp,0+y*tp))
                else:
                    elems += spira.SRef(ls_tr_u_M4_alt(), midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(ls_tr_M7(), midpoint=(0+x*tp,0+y*tp))
        return elems

# 1.5um junction fill cell
class ls_FakeJJ_1p5umx1p5um(spira.Device):
    __name_prefix__ = 'ls_FakeJJ_1p5umx1p5um'
    def create_elements(self, elems):
        elems += spira.Box(layer=M4,width=0.25*tp,height=0.25*tp)
        elems += spira.Box(layer=M5,width=0.25*tp,height=0.25*tp)
        elems += spira.Box(layer=J5,width=0.15*tp,height=0.15*tp)
        elems += spira.Box(layer=C5J,width=0.13*tp,height=0.13*tp)
        elems += spira.Box(layer=M6,width=0.2*tp,height=0.2*tp)

        return elems

# 3um junction fill cell
class ls_FakeJJ_3umx3um(spira.Cell):
    __name_prefix__ = 'ls_FakeJJ_3umx3um'
    def create_elements(self, elems):
        elems += spira.Box(layer=M4,width=0.4*tp,height=0.4*tp)
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.4*tp)
        elems += spira.Box(layer=J5,width=0.3*tp,height=0.3*tp)
        elems += spira.Box(layer=C5J,width=0.28*tp,height=0.28*tp)
        elems += spira.Box(layer=M6,width=0.35*tp,height=0.35*tp)

        return elems

# M4 to M7 connector cell
class ls_conn_M4M5M6M7(spira.Cell):
    __name_prefix__ = 'ls_conn_M4M5M6M7'
    def create_elements(self, elems):
        elems += spira.Box(layer=M4,width=0.14*tp,height=0.14*tp,center=(0.07*tp,0.07*tp))
        elems += spira.Box(layer=I4,width=0.08*tp,height=0.08*tp,center=(0.07*tp,0.07*tp))
        shape = spira.Shape(points=[
            [0.16,-0.015],[0.16,0.0],[0.0,0.0],[0.0,0.14],
            [0.16,0.14],[0.16,0.155],[0.33,0.155],[0.33,-0.015]
            ])
        shape = [x * tp for x in shape]
        elems += spira.Polygon(shape=shape, layer=M5)
        elems += spira.Box(layer=I5,width=0.07*tp,height=0.07*tp,center=(0.245*tp,0.07*tp))
        elems += spira.Box(layer=M6,width=0.315*tp,height=0.14*tp,center=(0.1575*tp,0.07*tp))
        elems += spira.Box(layer=I6,width=0.07*tp,height=0.07*tp,center=(0.07*tp,0.07*tp))
        elems += spira.Box(layer=M7,width=0.14*tp,height=0.14*tp,center=(0.07*tp,0.07*tp))

        return elems

# Bias cell
class ls_ib_350(spira.Cell):
    __name_prefix__ = 'ls_ib_350'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.58*tp,center=(0.0,0.29*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.525*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.52625*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems

# JJ cell
class ls_jj250sg(spira.Cell):
    __name_prefix__ = 'ls_jj250sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,4.95))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.9))
        elems += spira.Box(layer=M5,width=1.75,height=3.55,center=(0.0,4.4))
        elems += spira.Box(layer=M5,width=2.85,height=4.05,center=(0.0,0.6))
        elems += spira.Circle(layer=J5,box_size=(1.82, 1.82))
        elems += spira.Box(layer=R5,width=1.15,height=3.075,center=(0.0,2.8875))
        elems += spira.Circle(layer=C5J,box_size=(1.52, 1.52))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.9))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,3.89))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.63750))
        elems += spira.Box(layer=M6,width=2.55,height=3.8,center=(0.0,0.625))

        return elems

# M5 to M7 connector cell
class ls_conn_M5M6M7(spira.Cell):
    __name_prefix__ = 'ls_conn_M5M6M7'
    def create_elements(self, elems):
        elems += spira.Box(layer=M5,width=1.7,height=1.7,center=(0.35,0.35))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.35,0.35))
        elems += spira.Box(layer=M6,width=2.0,height=2.0,center=(0.35,0.35))
        elems += spira.Box(layer=I6,width=1.3,height=1.3,center=(0.35,0.35))
        elems += spira.Box(layer=M7,width=2.0,height=2.0,center=(0.35,0.35))

        return elems

# M0 Track block fill cell
class ls_tr_M0(spira.Cell):
    __name_prefix__ = 'ls_tr_M0'
    def create_elements(self, elems):
        elems += spira.Polygon(shape=lowerHalf, layer=M0)
        elems += spira.Polygon(shape=upperHalf, layer=M0)
        elems += spira.Polygon(shape=middleCross, layer=M0)

        return elems

# M7 Track block fill cell
class ls_tr_M7(spira.Cell):
    __name_prefix__ = 'ls_tr_M7'
    def create_elements(self, elems):
        elems += spira.Polygon(shape=lowerHalf, layer=M7)
        elems += spira.Polygon(shape=upperHalf, layer=M7)
        elems += spira.Polygon(shape=middleCross, layer=M7)

        return elems

# Track block with bias pillar cell
class ls_tr_bias_pillar_M0M6(spira.Cell):
    __name_prefix__ = 'ls_tr_bias_pillar_M0M6'
    def create_elements(self, elems):
        elems += spira.SRef(ls_tr_M7())
        elems += spira.Box(layer=M0,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=M2,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=M3,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=M6,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        
        elems += spira.Box(layer=I0,width=0.12*tp,height=0.12*tp,center=(0.39*tp,0.61*tp))
        elems += spira.Box(layer=I2,width=0.12*tp,height=0.12*tp,center=(0.39*tp,0.61*tp))
        elems += spira.Box(layer=I4,width=0.12*tp,height=0.12*tp,center=(0.39*tp,0.61*tp))

        elems += spira.Box(layer=I1,width=0.12*tp,height=0.12*tp,center=(0.61*tp,0.61*tp))
        elems += spira.Box(layer=I3,width=0.12*tp,height=0.12*tp,center=(0.61*tp,0.61*tp))
        elems += spira.Box(layer=I5,width=0.12*tp,height=0.12*tp,center=(0.61*tp,0.61*tp))
        
        elems += spira.Box(layer=I0,width=0.12*tp,height=0.12*tp,center=(0.61*tp,0.39*tp))
        elems += spira.Box(layer=I2,width=0.12*tp,height=0.12*tp,center=(0.61*tp,0.39*tp))
        elems += spira.Box(layer=I4,width=0.12*tp,height=0.12*tp,center=(0.61*tp,0.39*tp))
        
        elems += spira.Box(layer=I1,width=0.12*tp,height=0.12*tp,center=(0.39*tp,0.39*tp))
        elems += spira.Box(layer=I3,width=0.12*tp,height=0.12*tp,center=(0.39*tp,0.39*tp))
        elems += spira.Box(layer=I5,width=0.12*tp,height=0.12*tp,center=(0.39*tp,0.39*tp))

        elems += spira.Box(layer=M0,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.9375*tp))
        elems += spira.Box(layer=I0,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.935*tp))
        elems += spira.Box(layer=M2,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.9375*tp))
        elems += spira.Box(layer=I2,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.935*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.9375*tp))

        elems += spira.Box(layer=M0,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.9375*tp))
        elems += spira.Box(layer=I1,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.935*tp))
        elems += spira.Box(layer=M2,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.9375*tp))
        elems += spira.Box(layer=I3,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.935*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.9375*tp))

        elems += spira.Box(layer=M0,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.0625*tp))
        elems += spira.Box(layer=I0,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.065*tp))
        elems += spira.Box(layer=M2,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.0625*tp))
        elems += spira.Box(layer=I2,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.065*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.0625*tp))

        elems += spira.Box(layer=M0,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=I1,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.065*tp))
        elems += spira.Box(layer=M2,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=I3,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.065*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))

        top = spira.Shape(points=[
            (0.0,0.875),(0.0,1.0),(1.0,1.0),(1.0,0.125),(0.96,0.125),(0.96,0.28),
            (0.77,0.28),(0.77,0.72),(0.96,0.72),(0.96,0.875),(0.875,0.875),(0.875,0.96),
            (0.72,0.96),(0.72,0.77),(0.28,0.77),(0.28,0.96),(0.125,0.96),(0.125,0.875)
            ])
        top = [x * tp for x in top]
        bot = spira.Shape(points=[
            (0.0,0.0),(0.0,0.875),(0.04,0.875),(0.04,0.72),(0.23,0.72),(0.23,0.28),
            (0.04,0.28),(0.04,0.125),(0.125,0.125),(0.125,0.04),(0.28,0.04),(0.28,0.23),
            (0.72,0.23),(0.72,0.04),(0.875,0.04),(0.875,0.125),(1.0,0.125),(1.0,0.0)
            ])
        bot = [x * tp for x in bot]

        elems += spira.Polygon(shape=top, layer=M1)
        elems += spira.Polygon(shape=bot, layer=M1)
        elems += spira.Box(layer=M1,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Polygon(shape=top, layer=M4)
        elems += spira.Polygon(shape=bot, layer=M4)
        elems += spira.Box(layer=M4,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))

        return elems

# Track block cell
class ls_tr_u_M4_alt(spira.Cell):
    __name_prefix__ = 'ls_tr_u_M4_alt'
    def create_elements(self, elems):
        elems += spira.Box(layer=M0,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.9375*tp))
        elems += spira.Box(layer=I0,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.935*tp))
        elems += spira.Box(layer=M2,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.9375*tp))
        elems += spira.Box(layer=I2,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.935*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.9375*tp))

        elems += spira.Box(layer=M0,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.9375*tp))
        elems += spira.Box(layer=I1,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.935*tp))
        elems += spira.Box(layer=M2,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.9375*tp))
        elems += spira.Box(layer=I3,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.935*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.9375*tp))

        elems += spira.Box(layer=M0,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.0625*tp))
        elems += spira.Box(layer=I0,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.065*tp))
        elems += spira.Box(layer=M2,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.0625*tp))
        elems += spira.Box(layer=I2,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.065*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.0625*tp))

        elems += spira.Box(layer=M0,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=I1,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.065*tp))
        elems += spira.Box(layer=M2,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=I3,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.065*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))

        elems += spira.Polygon(shape=lowerHalf, layer=M1)
        elems += spira.Polygon(shape=upperHalf, layer=M1)
        elems += spira.Polygon(shape=middleCross, layer=M1)


        elems += spira.Polygon(shape=lowerHalf, layer=M4)
        elems += spira.Polygon(shape=upperHalf, layer=M4)
        elems += spira.Polygon(shape=middleCross, layer=M4)

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