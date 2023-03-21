import layer_setup as ls
import spira.all as spira
from spira.technologies.mit.process.database import RDD

# M0 Track block fill cell
class tr_M0(spira.Cell):
    __name_prefix__ = 'tr_M0'
    def create_elements(self, elems):
        lowerHalf = spira.Shape(points=[
            (0.0,0.0),(0.0,0.875),(0.04,0.875),(0.04,0.125),(0.125,0.125),
            (0.125,0.04),(0.875,0.04),(0.875,0.125),(1.0,0.125),(1.0,0.0)
            ])
        lowerHalf = [x * ls.tp for x in lowerHalf]
        upperHalf = spira.Shape(points=[
            (0.0,1.0),(1.0,1.0),(1.0,0.125),(0.96,0.125),(0.96,0.875),
            (0.875,0.875),(0.875,0.96),(0.125,0.96),(0.125,0.875),(0.0,0.875)
            ])
        upperHalf = [x * ls.tp for x in upperHalf]
        middleCross = spira.Shape(points=[
            (0.28,0.04),(0.28,0.28),(0.04,0.28),(0.04,0.72),(0.28,0.72),(0.28,0.96),
            (0.72,0.96),(0.72,0.72),(0.96,0.72),(0.96,0.28),(0.72,0.28),(0.72,0.04)
            ])
        middleCross = [x * ls.tp for x in middleCross]
        elems += spira.Polygon(shape=lowerHalf, layer=ls.M0)
        elems += spira.Polygon(shape=upperHalf, layer=ls.M0)
        elems += spira.Polygon(shape=middleCross, layer=ls.M0)

        return elems

# M1 Track block fill cell
class tr_M1(spira.Cell):
    __name_prefix__ = 'tr_M1'
    def create_elements(self, elems):
        lowerHalf = spira.Shape(points=[
            (0.0,0.0),(0.0,0.875),(0.04,0.875),(0.04,0.125),(0.125,0.125),
            (0.125,0.04),(0.875,0.04),(0.875,0.125),(1.0,0.125),(1.0,0.0)
            ])
        lowerHalf = [x * ls.tp for x in lowerHalf]
        upperHalf = spira.Shape(points=[
            (0.0,1.0),(1.0,1.0),(1.0,0.125),(0.96,0.125),(0.96,0.875),
            (0.875,0.875),(0.875,0.96),(0.125,0.96),(0.125,0.875),(0.0,0.875)
            ])
        upperHalf = [x * ls.tp for x in upperHalf]
        middleCross = spira.Shape(points=[
            (0.28,0.04),(0.28,0.28),(0.04,0.28),(0.04,0.72),(0.28,0.72),(0.28,0.96),
            (0.72,0.96),(0.72,0.72),(0.96,0.72),(0.96,0.28),(0.72,0.28),(0.72,0.04)
            ])
        middleCross = [x * ls.tp for x in middleCross]
        elems += spira.Polygon(shape=lowerHalf, layer=ls.M1)
        elems += spira.Polygon(shape=upperHalf, layer=ls.M1)
        elems += spira.Polygon(shape=middleCross, layer=ls.M1)

        return elems

# M7 Track block fill cell
class tr_M7(spira.Cell):
    __name_prefix__ = 'tr_M7'
    def create_elements(self, elems):
        lowerHalf = spira.Shape(points=[
            (0.0,0.0),(0.0,0.875),(0.04,0.875),(0.04,0.125),(0.125,0.125),
            (0.125,0.04),(0.875,0.04),(0.875,0.125),(1.0,0.125),(1.0,0.0)
            ])
        lowerHalf = [x * ls.tp for x in lowerHalf]
        upperHalf = spira.Shape(points=[
            (0.0,1.0),(1.0,1.0),(1.0,0.125),(0.96,0.125),(0.96,0.875),
            (0.875,0.875),(0.875,0.96),(0.125,0.96),(0.125,0.875),(0.0,0.875)
            ])
        upperHalf = [x * ls.tp for x in upperHalf]
        middleCross = spira.Shape(points=[
            (0.28,0.04),(0.28,0.28),(0.04,0.28),(0.04,0.72),(0.28,0.72),(0.28,0.96),
            (0.72,0.96),(0.72,0.72),(0.96,0.72),(0.96,0.28),(0.72,0.28),(0.72,0.04)
            ])
        middleCross = [x * ls.tp for x in middleCross]
        elems += spira.Polygon(shape=lowerHalf, layer=ls.M7)
        elems += spira.Polygon(shape=upperHalf, layer=ls.M7)
        elems += spira.Polygon(shape=middleCross, layer=ls.M7)

        return elems

# Track block with bias pillar cell
class tr_bias_pillar_M0M6(spira.Cell):
    __name_prefix__ = 'tr_bias_pillar_M0M6'
    def create_elements(self, elems):
        # Common shapes
        top = spira.Shape(points=[
            (0.0,0.875),(0.0,1.0),(1.0,1.0),(1.0,0.125),(0.96,0.125),(0.96,0.28),
            (0.77,0.28),(0.77,0.72),(0.96,0.72),(0.96,0.875),(0.875,0.875),(0.875,0.96),
            (0.72,0.96),(0.72,0.77),(0.28,0.77),(0.28,0.96),(0.125,0.96),(0.125,0.875)
            ])
        top = [x * ls.tp for x in top]
        bot = spira.Shape(points=[
            (0.0,0.0),(0.0,0.875),(0.04,0.875),(0.04,0.72),(0.23,0.72),(0.23,0.28),
            (0.04,0.28),(0.04,0.125),(0.125,0.125),(0.125,0.04),(0.28,0.04),(0.28,0.23),
            (0.72,0.23),(0.72,0.04),(0.875,0.04),(0.875,0.125),(1.0,0.125),(1.0,0.0)
            ])
        bot = [x * ls.tp for x in bot]

        elems += spira.Box(layer=ls.M0,width=0.44*ls.tp,height=0.44*ls.tp,center=(0.5*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.M0,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M0,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.9375*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M0,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.9375*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.M0,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.I0,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.39*ls.tp,0.61*ls.tp))
        elems += spira.Box(layer=ls.I0,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.61*ls.tp,0.39*ls.tp))
        elems += spira.Box(layer=ls.I0,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.065*ls.tp,0.935*ls.tp))
        elems += spira.Box(layer=ls.I0,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.935*ls.tp,0.065*ls.tp))
        elems += spira.Polygon(shape=top, layer=ls.M1)
        elems += spira.Polygon(shape=bot, layer=ls.M1)
        elems += spira.Box(layer=ls.M1,width=0.44*ls.tp,height=0.44*ls.tp,center=(0.5*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.I1,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.61*ls.tp,0.61*ls.tp))
        elems += spira.Box(layer=ls.I1,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.39*ls.tp,0.39*ls.tp))
        elems += spira.Box(layer=ls.I1,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.935*ls.tp,0.935*ls.tp))
        elems += spira.Box(layer=ls.I1,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.065*ls.tp,0.065*ls.tp))
        elems += spira.Box(layer=ls.M2,width=0.44*ls.tp,height=0.44*ls.tp,center=(0.5*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.M2,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M2,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.9375*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M2,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.9375*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.M2,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.I2,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.39*ls.tp,0.61*ls.tp))
        elems += spira.Box(layer=ls.I2,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.61*ls.tp,0.39*ls.tp))
        elems += spira.Box(layer=ls.I2,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.065*ls.tp,0.935*ls.tp))
        elems += spira.Box(layer=ls.I2,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.935*ls.tp,0.065*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.44*ls.tp,height=0.44*ls.tp,center=(0.5*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.9375*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.9375*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.I3,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.61*ls.tp,0.61*ls.tp))
        elems += spira.Box(layer=ls.I3,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.39*ls.tp,0.39*ls.tp))
        elems += spira.Box(layer=ls.I3,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.935*ls.tp,0.935*ls.tp))
        elems += spira.Box(layer=ls.I3,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.065*ls.tp,0.065*ls.tp))
        elems += spira.Polygon(shape=top, layer=ls.M4)
        elems += spira.Polygon(shape=bot, layer=ls.M4)
        elems += spira.Box(layer=ls.M4,width=0.44*ls.tp,height=0.44*ls.tp,center=(0.5*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.I4,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.39*ls.tp,0.61*ls.tp))
        elems += spira.Box(layer=ls.I4,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.61*ls.tp,0.39*ls.tp))
        elems += spira.Box(layer=ls.M5,width=0.44*ls.tp,height=0.44*ls.tp,center=(0.5*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.I5,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.61*ls.tp,0.61*ls.tp))
        elems += spira.Box(layer=ls.I5,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.39*ls.tp,0.39*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.44*ls.tp,height=0.44*ls.tp,center=(0.5*ls.tp,0.5*ls.tp))
        elems += spira.SRef(tr_M7())
        
        return elems

# Track block with half of a bias pillar
class tr_bias_pillar_half(spira.Cell):
    __name_prefix__ = "tr_bias_pillar_half"
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M0,width=0.25*ls.tp,height=0.125*ls.tp,center=(0.5*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M0,width=0.22*ls.tp,height=0.44*ls.tp,center=(0.5*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.M0,width=0.25*ls.tp,height=0.125*ls.tp,center=(0.5*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.I0,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.565*ls.tp,0.935*ls.tp))
        elems += spira.Box(layer=ls.I0,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.5*ls.tp,0.39*ls.tp))
        elems += spira.Box(layer=ls.I0,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.435*ls.tp,0.065*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.22*ls.tp,height=1*ls.tp,center=(0.11*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.22*ls.tp,height=1*ls.tp,center=(0.89*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.155*ls.tp,height=0.04*ls.tp,center=(0.2975*ls.tp,0.98*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.155*ls.tp,height=0.04*ls.tp,center=(0.7025*ls.tp,0.98*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.155*ls.tp,height=0.04*ls.tp,center=(0.2975*ls.tp,0.02*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.155*ls.tp,height=0.04*ls.tp,center=(0.7025*ls.tp,0.02*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.25*ls.tp,height=0.125*ls.tp,center=(0.5*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.25*ls.tp,height=0.125*ls.tp,center=(0.5*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.08*ls.tp,height=0.105*ls.tp,center=(0.5*ls.tp,0.8225*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.08*ls.tp,height=0.105*ls.tp,center=(0.5*ls.tp,0.1775*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.12*ls.tp,height=0.44*ls.tp,center=(0.28*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.12*ls.tp,height=0.44*ls.tp,center=(0.72*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.22*ls.tp,height=0.44*ls.tp,center=(0.5*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.I1,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.435*ls.tp,0.935*ls.tp))
        elems += spira.Box(layer=ls.I1,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.5*ls.tp,0.61*ls.tp))
        elems += spira.Box(layer=ls.I1,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.565*ls.tp,0.065*ls.tp))
        elems += spira.Box(layer=ls.M2,width=0.25*ls.tp,height=0.125*ls.tp,center=(0.5*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M2,width=0.22*ls.tp,height=0.44*ls.tp,center=(0.5*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.M2,width=0.25*ls.tp,height=0.125*ls.tp,center=(0.5*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.I2,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.565*ls.tp,0.935*ls.tp))
        elems += spira.Box(layer=ls.I2,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.5*ls.tp,0.39*ls.tp))
        elems += spira.Box(layer=ls.I2,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.435*ls.tp,0.065*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.25*ls.tp,height=0.125*ls.tp,center=(0.5*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.22*ls.tp,height=0.44*ls.tp,center=(0.5*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.25*ls.tp,height=0.125*ls.tp,center=(0.5*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.I3,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.435*ls.tp,0.935*ls.tp))
        elems += spira.Box(layer=ls.I3,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.5*ls.tp,0.61*ls.tp))
        elems += spira.Box(layer=ls.I3,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.565*ls.tp,0.065*ls.tp))
        elems += spira.Box(layer=ls.M4,width=0.22*ls.tp,height=1*ls.tp,center=(0.11*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.M4,width=0.22*ls.tp,height=1*ls.tp,center=(0.89*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.M4,width=0.155*ls.tp,height=0.04*ls.tp,center=(0.2975*ls.tp,0.98*ls.tp))
        elems += spira.Box(layer=ls.M4,width=0.155*ls.tp,height=0.04*ls.tp,center=(0.7025*ls.tp,0.98*ls.tp))
        elems += spira.Box(layer=ls.M4,width=0.155*ls.tp,height=0.04*ls.tp,center=(0.2975*ls.tp,0.02*ls.tp))
        elems += spira.Box(layer=ls.M4,width=0.155*ls.tp,height=0.04*ls.tp,center=(0.7025*ls.tp,0.02*ls.tp))
        elems += spira.Box(layer=ls.M4,width=0.25*ls.tp,height=0.125*ls.tp,center=(0.5*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.M4,width=0.25*ls.tp,height=0.125*ls.tp,center=(0.5*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M4,width=0.08*ls.tp,height=0.105*ls.tp,center=(0.5*ls.tp,0.8225*ls.tp))
        elems += spira.Box(layer=ls.M4,width=0.08*ls.tp,height=0.105*ls.tp,center=(0.5*ls.tp,0.1775*ls.tp))
        elems += spira.Box(layer=ls.M4,width=0.12*ls.tp,height=0.44*ls.tp,center=(0.28*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.M4,width=0.12*ls.tp,height=0.44*ls.tp,center=(0.72*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.M4,width=0.22*ls.tp,height=0.44*ls.tp,center=(0.5*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.I4,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.5*ls.tp,0.39*ls.tp))
        elems += spira.Box(layer=ls.M5,width=0.22*ls.tp,height=0.44*ls.tp,center=(0.5*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.I5,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.5*ls.tp,0.61*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.22*ls.tp,height=0.44*ls.tp,center=(0.5*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.M7,width=0.22*ls.tp,height=1*ls.tp,center=(0.11*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.M7,width=0.22*ls.tp,height=1*ls.tp,center=(0.89*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.M7,width=0.155*ls.tp,height=0.04*ls.tp,center=(0.2975*ls.tp,0.98*ls.tp))
        elems += spira.Box(layer=ls.M7,width=0.155*ls.tp,height=0.04*ls.tp,center=(0.7025*ls.tp,0.98*ls.tp))
        elems += spira.Box(layer=ls.M7,width=0.155*ls.tp,height=0.04*ls.tp,center=(0.2975*ls.tp,0.02*ls.tp))
        elems += spira.Box(layer=ls.M7,width=0.155*ls.tp,height=0.04*ls.tp,center=(0.7025*ls.tp,0.02*ls.tp))
        elems += spira.Box(layer=ls.M7,width=0.25*ls.tp,height=0.125*ls.tp,center=(0.5*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.M7,width=0.25*ls.tp,height=0.125*ls.tp,center=(0.5*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M7,width=0.08*ls.tp,height=0.75*ls.tp,center=(0.5*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.M7,width=0.56*ls.tp,height=0.44*ls.tp,center=(0.5*ls.tp,0.5*ls.tp))
        return elems

# PTL connection cell
class tr_PTLconnection(spira.Cell):
    __name_prefix__ = 'tr_PTLconnection'
    def create_elements(self, elems):
        # Common shape
        top = spira.Shape(points=[
            (0.0,0.875),(0.0,1.0),(1.0,1.0),(1.0,0.125),(0.96,0.125),(0.96,0.28),
            (0.77,0.28),(0.77,0.72),(0.96,0.72),(0.96,0.875),(0.875,0.875),(0.875,0.96),
            (0.72,0.96),(0.72,0.77),(0.28,0.77),(0.28,0.96),(0.125,0.96),(0.125,0.875)
            ])
        top = [x * ls.tp for x in top]
        bot = spira.Shape(points=[
            (0.0,0.0),(0.0,0.875),(0.04,0.875),(0.04,0.72),(0.23,0.72),(0.23,0.28),
            (0.04,0.28),(0.04,0.125),(0.125,0.125),(0.125,0.04),(0.28,0.04),(0.28,0.23),
            (0.72,0.23),(0.72,0.04),(0.875,0.04),(0.875,0.125),(1.0,0.125),(1.0,0.0)
            ])
        bot = [x * ls.tp for x in bot]
        lowerHalf = spira.Shape(points=[
            (0.0,0.0),(0.0,0.875),(0.04,0.875),(0.04,0.125),(0.125,0.125),
            (0.125,0.04),(0.875,0.04),(0.875,0.125),(1.0,0.125),(1.0,0.0)
            ])
        lowerHalf = [x * ls.tp for x in lowerHalf]
        upperHalf = spira.Shape(points=[
            (0.0,1.0),(1.0,1.0),(1.0,0.125),(0.96,0.125),(0.96,0.875),
            (0.875,0.875),(0.875,0.96),(0.125,0.96),(0.125,0.875),(0.0,0.875)
            ])
        upperHalf = [x * ls.tp for x in upperHalf]
        middleCross = spira.Shape(points=[
            (0.28,0.04),(0.28,0.28),(0.04,0.28),(0.04,0.72),(0.28,0.72),(0.28,0.96),
            (0.72,0.96),(0.72,0.72),(0.96,0.72),(0.96,0.28),(0.72,0.28),(0.72,0.04)
            ])
        middleCross = [x * ls.tp for x in middleCross]
        elems += spira.Polygon(shape=lowerHalf, layer=ls.M0)
        elems += spira.Polygon(shape=upperHalf, layer=ls.M0)
        elems += spira.Polygon(shape=middleCross, layer=ls.M0)
        elems += spira.Box(layer=ls.I0,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.065*ls.tp,0.935*ls.tp))
        elems += spira.Box(layer=ls.I0,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.935*ls.tp,0.065*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.44*ls.tp,height=0.44*ls.tp,center=(0.5*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.9375*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.9375*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.I1,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.61*ls.tp,0.61*ls.tp))
        elems += spira.Box(layer=ls.I1,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.39*ls.tp,0.39*ls.tp))
        elems += spira.Box(layer=ls.I1,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.935*ls.tp,0.935*ls.tp))
        elems += spira.Box(layer=ls.I1,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.065*ls.tp,0.065*ls.tp))
        elems += spira.Polygon(shape=top, layer=ls.M2)
        elems += spira.Polygon(shape=bot, layer=ls.M2)
        elems += spira.Box(layer=ls.M2,width=0.44*ls.tp,height=0.44*ls.tp,center=(0.5*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.I2,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.39*ls.tp,0.61*ls.tp))
        elems += spira.Box(layer=ls.I2,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.61*ls.tp,0.39*ls.tp))
        elems += spira.Box(layer=ls.I2,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.065*ls.tp,0.935*ls.tp))
        elems += spira.Box(layer=ls.I2,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.935*ls.tp,0.065*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.44*ls.tp,height=0.44*ls.tp,center=(0.5*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.9375*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.9375*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.I3,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.61*ls.tp,0.61*ls.tp))
        elems += spira.Box(layer=ls.I3,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.39*ls.tp,0.39*ls.tp))
        elems += spira.Box(layer=ls.I3,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.935*ls.tp,0.935*ls.tp))
        elems += spira.Box(layer=ls.I3,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.065*ls.tp,0.065*ls.tp))
        elems += spira.Polygon(shape=top, layer=ls.M4)
        elems += spira.Polygon(shape=bot, layer=ls.M4)
        elems += spira.Box(layer=ls.M4,width=0.44*ls.tp,height=0.44*ls.tp,center=(0.5*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.I4,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.39*ls.tp,0.61*ls.tp))
        elems += spira.Box(layer=ls.I4,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.61*ls.tp,0.39*ls.tp))
        elems += spira.Box(layer=ls.M5,width=0.44*ls.tp,height=0.44*ls.tp,center=(0.5*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.I5,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.61*ls.tp,0.61*ls.tp))
        elems += spira.Box(layer=ls.I5,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.39*ls.tp,0.39*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.44*ls.tp,height=0.44*ls.tp,center=(0.5*ls.tp,0.5*ls.tp))
        elems += spira.SRef(tr_M7())

        return elems
        
    def create_ports(self,ports):
        ports += spira.Port(name="M6:P",midpoint=(0.500*ls.tp,0.500*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports
tr_PTL_conn = tr_PTLconnection

# PTL connection cell
class tr_PTLconnection_M3M6(spira.Cell):
    __name_prefix__ = 'tr_PTLconnection_M3M6'
    def create_elements(self, elems):
        # Common shape
        top = spira.Shape(points=[
            (0.0,0.875),(0.0,1.0),(1.0,1.0),(1.0,0.125),(0.96,0.125),(0.96,0.28),
            (0.77,0.28),(0.77,0.72),(0.96,0.72),(0.96,0.875),(0.875,0.875),(0.875,0.96),
            (0.72,0.96),(0.72,0.77),(0.28,0.77),(0.28,0.96),(0.125,0.96),(0.125,0.875)
            ])
        top = [x * ls.tp for x in top]
        bot = spira.Shape(points=[
            (0.0,0.0),(0.0,0.875),(0.04,0.875),(0.04,0.72),(0.23,0.72),(0.23,0.28),
            (0.04,0.28),(0.04,0.125),(0.125,0.125),(0.125,0.04),(0.28,0.04),(0.28,0.23),
            (0.72,0.23),(0.72,0.04),(0.875,0.04),(0.875,0.125),(1.0,0.125),(1.0,0.0)
            ])
        bot = [x * ls.tp for x in bot]
        lowerHalf = spira.Shape(points=[
            (0.0,0.0),(0.0,0.875),(0.04,0.875),(0.04,0.125),(0.125,0.125),
            (0.125,0.04),(0.875,0.04),(0.875,0.125),(1.0,0.125),(1.0,0.0)
            ])
        lowerHalf = [x * ls.tp for x in lowerHalf]
        upperHalf = spira.Shape(points=[
            (0.0,1.0),(1.0,1.0),(1.0,0.125),(0.96,0.125),(0.96,0.875),
            (0.875,0.875),(0.875,0.96),(0.125,0.96),(0.125,0.875),(0.0,0.875)
            ])
        upperHalf = [x * ls.tp for x in upperHalf]
        middleCross = spira.Shape(points=[
            (0.28,0.04),(0.28,0.28),(0.04,0.28),(0.04,0.72),(0.28,0.72),(0.28,0.96),
            (0.72,0.96),(0.72,0.72),(0.96,0.72),(0.96,0.28),(0.72,0.28),(0.72,0.04)
            ])
        middleCross = [x * ls.tp for x in middleCross]
        elems += spira.Polygon(shape=lowerHalf, layer=ls.M0)
        elems += spira.Polygon(shape=upperHalf, layer=ls.M0)
        elems += spira.Polygon(shape=middleCross, layer=ls.M0)
        elems += spira.Box(layer=ls.I0,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.065*ls.tp,0.935*ls.tp))
        elems += spira.Box(layer=ls.I0,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.935*ls.tp,0.065*ls.tp))
        elems += spira.Polygon(shape=lowerHalf, layer=ls.M1)
        elems += spira.Polygon(shape=upperHalf, layer=ls.M1)
        elems += spira.Polygon(shape=middleCross, layer=ls.M1)
        elems += spira.Box(layer=ls.I1,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.935*ls.tp,0.935*ls.tp))
        elems += spira.Box(layer=ls.I1,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.065*ls.tp,0.065*ls.tp))
        elems += spira.Polygon(shape=lowerHalf, layer=ls.M2)
        elems += spira.Polygon(shape=upperHalf, layer=ls.M2)
        elems += spira.Polygon(shape=middleCross, layer=ls.M2)
        elems += spira.Box(layer=ls.I2,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.065*ls.tp,0.935*ls.tp))
        elems += spira.Box(layer=ls.I2,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.935*ls.tp,0.065*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.44*ls.tp,height=0.44*ls.tp,center=(0.5*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.9375*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.9375*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.I3,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.61*ls.tp,0.61*ls.tp))
        elems += spira.Box(layer=ls.I3,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.39*ls.tp,0.39*ls.tp))
        elems += spira.Box(layer=ls.I3,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.935*ls.tp,0.935*ls.tp))
        elems += spira.Box(layer=ls.I3,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.065*ls.tp,0.065*ls.tp))
        elems += spira.Polygon(shape=top, layer=ls.M4)
        elems += spira.Polygon(shape=bot, layer=ls.M4)
        elems += spira.Box(layer=ls.M4,width=0.44*ls.tp,height=0.44*ls.tp,center=(0.5*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.I4,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.39*ls.tp,0.61*ls.tp))
        elems += spira.Box(layer=ls.I4,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.61*ls.tp,0.39*ls.tp))
        elems += spira.Box(layer=ls.M5,width=0.44*ls.tp,height=0.44*ls.tp,center=(0.5*ls.tp,0.5*ls.tp))
        elems += spira.Box(layer=ls.I5,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.61*ls.tp,0.61*ls.tp))
        elems += spira.Box(layer=ls.I5,width=0.12*ls.tp,height=0.12*ls.tp,center=(0.39*ls.tp,0.39*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.44*ls.tp,height=0.44*ls.tp,center=(0.5*ls.tp,0.5*ls.tp))
        elems += spira.SRef(tr_M7())

        return elems

# Track block cell
class tr_u_M4_alt(spira.Cell):
    __name_prefix__ = 'tr_u_M4_alt'
    def create_elements(self, elems):
        lowerHalf = spira.Shape(points=[
            (0.0,0.0),(0.0,0.875),(0.04,0.875),(0.04,0.125),(0.125,0.125),
            (0.125,0.04),(0.875,0.04),(0.875,0.125),(1.0,0.125),(1.0,0.0)
            ])
        lowerHalf = [x * ls.tp for x in lowerHalf]
        upperHalf = spira.Shape(points=[
            (0.0,1.0),(1.0,1.0),(1.0,0.125),(0.96,0.125),(0.96,0.875),
            (0.875,0.875),(0.875,0.96),(0.125,0.96),(0.125,0.875),(0.0,0.875)
            ])
        upperHalf = [x * ls.tp for x in upperHalf]
        middleCross = spira.Shape(points=[
            (0.28,0.04),(0.28,0.28),(0.04,0.28),(0.04,0.72),(0.28,0.72),(0.28,0.96),
            (0.72,0.96),(0.72,0.72),(0.96,0.72),(0.96,0.28),(0.72,0.28),(0.72,0.04)
            ])
        middleCross = [x * ls.tp for x in middleCross]
        elems += spira.Box(layer=ls.M0,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M0,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.9375*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M0,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.9375*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.M0,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.I0,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.065*ls.tp,0.935*ls.tp))
        elems += spira.Box(layer=ls.I0,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.935*ls.tp,0.065*ls.tp))
        elems += spira.Polygon(shape=lowerHalf, layer=ls.M1)
        elems += spira.Polygon(shape=upperHalf, layer=ls.M1)
        elems += spira.Polygon(shape=middleCross, layer=ls.M1)
        elems += spira.Box(layer=ls.I1,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.935*ls.tp,0.935*ls.tp))
        elems += spira.Box(layer=ls.I1,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.065*ls.tp,0.065*ls.tp))
        elems += spira.Box(layer=ls.M2,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M2,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.9375*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M2,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.9375*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.M2,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.I2,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.065*ls.tp,0.935*ls.tp))
        elems += spira.Box(layer=ls.I2,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.935*ls.tp,0.065*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.9375*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.9375*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.I3,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.935*ls.tp,0.935*ls.tp))
        elems += spira.Box(layer=ls.I3,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.065*ls.tp,0.065*ls.tp))
        elems += spira.Polygon(shape=lowerHalf, layer=ls.M4)
        elems += spira.Polygon(shape=upperHalf, layer=ls.M4)
        elems += spira.Polygon(shape=middleCross, layer=ls.M4)

        return elems

# Track block cell
class tr_u_M4(spira.Cell):
    __name_prefix__ = 'tr_u_M4'
    def create_elements(self, elems):
        lowerHalf = spira.Shape(points=[
            (0.0,0.0),(0.0,0.875),(0.04,0.875),(0.04,0.125),(0.125,0.125),
            (0.125,0.04),(0.875,0.04),(0.875,0.125),(1.0,0.125),(1.0,0.0)
            ])
        lowerHalf = [x * ls.tp for x in lowerHalf]
        upperHalf = spira.Shape(points=[
            (0.0,1.0),(1.0,1.0),(1.0,0.125),(0.96,0.125),(0.96,0.875),
            (0.875,0.875),(0.875,0.96),(0.125,0.96),(0.125,0.875),(0.0,0.875)
            ])
        upperHalf = [x * ls.tp for x in upperHalf]
        middleCross = spira.Shape(points=[
            (0.28,0.04),(0.28,0.28),(0.04,0.28),(0.04,0.72),(0.28,0.72),(0.28,0.96),
            (0.72,0.96),(0.72,0.72),(0.96,0.72),(0.96,0.28),(0.72,0.28),(0.72,0.04)
            ])
        middleCross = [x * ls.tp for x in middleCross]
        elems += spira.Polygon(shape=lowerHalf, layer=ls.M0)
        elems += spira.Polygon(shape=upperHalf, layer=ls.M0)
        elems += spira.Polygon(shape=middleCross, layer=ls.M0)
        elems += spira.Box(layer=ls.I0,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.065*ls.tp,0.935*ls.tp))
        elems += spira.Box(layer=ls.I0,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.935*ls.tp,0.065*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.9375*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.9375*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.I1,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.935*ls.tp,0.935*ls.tp))
        elems += spira.Box(layer=ls.I1,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.065*ls.tp,0.065*ls.tp))
        elems += spira.Polygon(shape=lowerHalf, layer=ls.M2)
        elems += spira.Polygon(shape=upperHalf, layer=ls.M2)
        elems += spira.Box(layer=ls.I2,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.065*ls.tp,0.935*ls.tp))
        elems += spira.Box(layer=ls.I2,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.935*ls.tp,0.065*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.9375*ls.tp,0.9375*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.9375*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.I3,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.935*ls.tp,0.935*ls.tp))
        elems += spira.Box(layer=ls.I3,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.065*ls.tp,0.065*ls.tp))
        elems += spira.Polygon(shape=lowerHalf, layer=ls.M4)
        elems += spira.Polygon(shape=upperHalf, layer=ls.M4)
        elems += spira.Polygon(shape=middleCross, layer=ls.M4)

        return elems

# Quarter 1 of trackblock cell
class tr_u_M4_quarter1(spira.Cell):
    __name_prefix__ = "tr_u_M4_quarter1"
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M0,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.22*ls.tp,height=0.5*ls.tp,center=(0.39*ls.tp,0.25*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.28*ls.tp,height=0.22*ls.tp,center=(0.14*ls.tp,0.39*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.04*ls.tp,height=0.155*ls.tp,center=(0.02*ls.tp,0.2025*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.155*ls.tp,height=0.04*ls.tp,center=(0.2025*ls.tp,0.02*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.I1,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.065*ls.tp,0.065*ls.tp))
        elems += spira.Box(layer=ls.M2,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.I3,width=0.06*ls.tp,height=0.06*ls.tp,center=(0.065*ls.tp,0.065*ls.tp))
        elems += spira.Box(layer=ls.M4,width=0.22*ls.tp,height=0.5*ls.tp,center=(0.39*ls.tp,0.25*ls.tp))
        elems += spira.Box(layer=ls.M4,width=0.28*ls.tp,height=0.22*ls.tp,center=(0.14*ls.tp,0.39*ls.tp))
        elems += spira.Box(layer=ls.M4,width=0.04*ls.tp,height=0.155*ls.tp,center=(0.02*ls.tp,0.2025*ls.tp))
        elems += spira.Box(layer=ls.M4,width=0.155*ls.tp,height=0.04*ls.tp,center=(0.2025*ls.tp,0.02*ls.tp))
        elems += spira.Box(layer=ls.M4,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.M7,width=0.22*ls.tp,height=0.5*ls.tp,center=(0.39*ls.tp,0.25*ls.tp))
        elems += spira.Box(layer=ls.M7,width=0.28*ls.tp,height=0.22*ls.tp,center=(0.14*ls.tp,0.39*ls.tp))
        elems += spira.Box(layer=ls.M7,width=0.04*ls.tp,height=0.155*ls.tp,center=(0.02*ls.tp,0.2025*ls.tp))
        elems += spira.Box(layer=ls.M7,width=0.155*ls.tp,height=0.04*ls.tp,center=(0.2025*ls.tp,0.02*ls.tp))
        elems += spira.Box(layer=ls.M7,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0625*ls.tp,0.0625*ls.tp))
        return elems

# Quarter 2 of trackblock cell
class tr_u_M4_quarter2(spira.Cell):
    __name_prefix__ = "tr_u_M4_quarter2"
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M0,width=0.125*ls.tp,height=0.125*ls.tp,center=(-0.0625*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.I0,width=0.06*ls.tp,height=0.06*ls.tp,center=(-0.065*ls.tp,0.065*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.22*ls.tp,height=0.5*ls.tp,center=(-0.39*ls.tp,0.25*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.28*ls.tp,height=0.22*ls.tp,center=(-0.14*ls.tp,0.39*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.04*ls.tp,height=0.155*ls.tp,center=(-0.02*ls.tp,0.2025*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.155*ls.tp,height=0.04*ls.tp,center=(-0.2025*ls.tp,0.02*ls.tp))
        elems += spira.Box(layer=ls.M1,width=0.125*ls.tp,height=0.125*ls.tp,center=(-0.0625*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.M2,width=0.125*ls.tp,height=0.125*ls.tp,center=(-0.0625*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.I2,width=0.06*ls.tp,height=0.06*ls.tp,center=(-0.065*ls.tp,0.065*ls.tp))
        elems += spira.Box(layer=ls.M3,width=0.125*ls.tp,height=0.125*ls.tp,center=(-0.0625*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.M4,width=0.22*ls.tp,height=0.5*ls.tp,center=(-0.39*ls.tp,0.25*ls.tp))
        elems += spira.Box(layer=ls.M4,width=0.28*ls.tp,height=0.22*ls.tp,center=(-0.14*ls.tp,0.39*ls.tp))
        elems += spira.Box(layer=ls.M4,width=0.04*ls.tp,height=0.155*ls.tp,center=(-0.02*ls.tp,0.2025*ls.tp))
        elems += spira.Box(layer=ls.M4,width=0.155*ls.tp,height=0.04*ls.tp,center=(-0.2025*ls.tp,0.02*ls.tp))
        elems += spira.Box(layer=ls.M4,width=0.125*ls.tp,height=0.125*ls.tp,center=(-0.0625*ls.tp,0.0625*ls.tp))
        elems += spira.Box(layer=ls.M7,width=0.22*ls.tp,height=0.5*ls.tp,center=(-0.39*ls.tp,0.25*ls.tp))
        elems += spira.Box(layer=ls.M7,width=0.28*ls.tp,height=0.22*ls.tp,center=(-0.14*ls.tp,0.39*ls.tp))
        elems += spira.Box(layer=ls.M7,width=0.04*ls.tp,height=0.155*ls.tp,center=(-0.02*ls.tp,0.2025*ls.tp))
        elems += spira.Box(layer=ls.M7,width=0.155*ls.tp,height=0.04*ls.tp,center=(-0.2025*ls.tp,0.02*ls.tp))
        elems += spira.Box(layer=ls.M7,width=0.125*ls.tp,height=0.125*ls.tp,center=(-0.0625*ls.tp,0.0625*ls.tp))
        return elems
        
class tr_u_M4_NPTL(spira.Cell):
    __name_prefix__ = "tr_u_M4_NPTL"
    def create_elements(self, elems):  
         elems += spira.Polygon(layer=ls.M0,shape=[(0.000*ls.tp,0.000*ls.tp),(0.000*ls.tp,1.000*ls.tp),(0.125*ls.tp,1.000*ls.tp),(0.125*ls.tp,0.875*ls.tp),(0.040*ls.tp,0.875*ls.tp),(0.040*ls.tp,0.125*ls.tp),(0.125*ls.tp,0.125*ls.tp),(0.125*ls.tp,0.040*ls.tp),(0.280*ls.tp,0.040*ls.tp),(0.280*ls.tp,0.280*ls.tp),(0.040*ls.tp,0.280*ls.tp),(0.040*ls.tp,0.720*ls.tp),(0.280*ls.tp,0.720*ls.tp),(0.280*ls.tp,0.960*ls.tp),(0.125*ls.tp,0.960*ls.tp),(0.125*ls.tp,1.000*ls.tp),(0.720*ls.tp,1.000*ls.tp),(0.720*ls.tp,0.040*ls.tp),(0.875*ls.tp,0.040*ls.tp),(0.875*ls.tp,0.125*ls.tp),(0.960*ls.tp,0.125*ls.tp),(0.960*ls.tp,0.280*ls.tp),(0.720*ls.tp,0.280*ls.tp),(0.720*ls.tp,0.720*ls.tp),(0.960*ls.tp,0.720*ls.tp),(0.960*ls.tp,0.875*ls.tp),(0.875*ls.tp,0.875*ls.tp),(0.875*ls.tp,0.960*ls.tp),(0.720*ls.tp,0.960*ls.tp),(0.720*ls.tp,1.000*ls.tp),(1.000*ls.tp,1.000*ls.tp),(1.000*ls.tp,0.000*ls.tp)])
         elems += spira.Polygon(layer=ls.M4,shape=[(0.000*ls.tp,0.000*ls.tp),(0.000*ls.tp,1.000*ls.tp),(0.125*ls.tp,1.000*ls.tp),(0.125*ls.tp,0.875*ls.tp),(0.040*ls.tp,0.875*ls.tp),(0.040*ls.tp,0.125*ls.tp),(0.125*ls.tp,0.125*ls.tp),(0.125*ls.tp,0.040*ls.tp),(0.280*ls.tp,0.040*ls.tp),(0.280*ls.tp,0.280*ls.tp),(0.040*ls.tp,0.280*ls.tp),(0.040*ls.tp,0.720*ls.tp),(0.280*ls.tp,0.720*ls.tp),(0.280*ls.tp,0.960*ls.tp),(0.125*ls.tp,0.960*ls.tp),(0.125*ls.tp,1.000*ls.tp),(0.720*ls.tp,1.000*ls.tp),(0.720*ls.tp,0.040*ls.tp),(0.875*ls.tp,0.040*ls.tp),(0.875*ls.tp,0.125*ls.tp),(0.960*ls.tp,0.125*ls.tp),(0.960*ls.tp,0.280*ls.tp),(0.720*ls.tp,0.280*ls.tp),(0.720*ls.tp,0.720*ls.tp),(0.960*ls.tp,0.720*ls.tp),(0.960*ls.tp,0.875*ls.tp),(0.875*ls.tp,0.875*ls.tp),(0.875*ls.tp,0.960*ls.tp),(0.720*ls.tp,0.960*ls.tp),(0.720*ls.tp,1.000*ls.tp),(1.000*ls.tp,1.000*ls.tp),(1.000*ls.tp,0.000*ls.tp)])
         elems += spira.Polygon(layer=ls.M1,shape=[(0.125*ls.tp,0.000*ls.tp),(0.125*ls.tp,0.040*ls.tp),(0.280*ls.tp,0.040*ls.tp),(0.280*ls.tp,0.280*ls.tp),(0.040*ls.tp,0.280*ls.tp),(0.040*ls.tp,0.125*ls.tp),(0.000*ls.tp,0.125*ls.tp),(0.000*ls.tp,0.875*ls.tp),(0.040*ls.tp,0.875*ls.tp),(0.040*ls.tp,0.720*ls.tp),(0.280*ls.tp,0.720*ls.tp),(0.280*ls.tp,0.960*ls.tp),(0.125*ls.tp,0.960*ls.tp),(0.125*ls.tp,1.000*ls.tp),(0.875*ls.tp,1.000*ls.tp),(0.875*ls.tp,0.960*ls.tp),(0.720*ls.tp,0.960*ls.tp),(0.720*ls.tp,0.720*ls.tp),(0.960*ls.tp,0.720*ls.tp),(0.960*ls.tp,0.875*ls.tp),(1.000*ls.tp,0.875*ls.tp),(1.000*ls.tp,0.125*ls.tp),(0.960*ls.tp,0.125*ls.tp),(0.960*ls.tp,0.280*ls.tp),(0.720*ls.tp,0.280*ls.tp),(0.720*ls.tp,0.040*ls.tp),(0.875*ls.tp,0.040*ls.tp),(0.875*ls.tp,0.000*ls.tp)])
         elems += spira.Polygon(layer=ls.M1,shape=[(0.000*ls.tp,0.000*ls.tp),(0.000*ls.tp,0.125*ls.tp),(0.125*ls.tp,0.125*ls.tp),(0.125*ls.tp,0.000*ls.tp)])
         elems += spira.Polygon(layer=ls.M1,shape=[(0.875*ls.tp,0.000*ls.tp),(0.875*ls.tp,0.125*ls.tp),(1.000*ls.tp,0.125*ls.tp),(1.000*ls.tp,0.000*ls.tp)])
         elems += spira.Polygon(layer=ls.M1,shape=[(0.875*ls.tp,0.875*ls.tp),(0.875*ls.tp,1.000*ls.tp),(1.000*ls.tp,1.000*ls.tp),(1.000*ls.tp,0.875*ls.tp)])
         elems += spira.Polygon(layer=ls.M1,shape=[(0.000*ls.tp,0.875*ls.tp),(0.000*ls.tp,1.000*ls.tp),(0.125*ls.tp,1.000*ls.tp),(0.125*ls.tp,0.875*ls.tp)])
         elems += spira.Polygon(layer=ls.M2,shape=[(0.000*ls.tp,0.875*ls.tp),(0.000*ls.tp,1.000*ls.tp),(0.125*ls.tp,1.000*ls.tp),(0.125*ls.tp,0.875*ls.tp)])
         elems += spira.Polygon(layer=ls.M2,shape=[(0.875*ls.tp,0.875*ls.tp),(0.875*ls.tp,1.000*ls.tp),(1.000*ls.tp,1.000*ls.tp),(1.000*ls.tp,0.875*ls.tp)])
         elems += spira.Polygon(layer=ls.M2,shape=[(0.875*ls.tp,0.000*ls.tp),(0.875*ls.tp,0.125*ls.tp),(1.000*ls.tp,0.125*ls.tp),(1.000*ls.tp,0.000*ls.tp)])
         elems += spira.Polygon(layer=ls.M2,shape=[(0.000*ls.tp,0.000*ls.tp),(0.000*ls.tp,0.125*ls.tp),(0.125*ls.tp,0.125*ls.tp),(0.125*ls.tp,0.000*ls.tp)])
         elems += spira.Polygon(layer=ls.I3,shape=[(0.035*ls.tp,0.035*ls.tp),(0.035*ls.tp,0.095*ls.tp),(0.095*ls.tp,0.095*ls.tp),(0.095*ls.tp,0.035*ls.tp)])
         elems += spira.Polygon(layer=ls.I3,shape=[(0.905*ls.tp,0.905*ls.tp),(0.905*ls.tp,0.965*ls.tp),(0.965*ls.tp,0.965*ls.tp),(0.965*ls.tp,0.905*ls.tp)])
         elems += spira.Polygon(layer=ls.M3,shape=[(0.000*ls.tp,0.875*ls.tp),(0.000*ls.tp,1.000*ls.tp),(0.125*ls.tp,1.000*ls.tp),(0.125*ls.tp,0.875*ls.tp)])
         elems += spira.Polygon(layer=ls.M3,shape=[(0.875*ls.tp,0.875*ls.tp),(0.875*ls.tp,1.000*ls.tp),(1.000*ls.tp,1.000*ls.tp),(1.000*ls.tp,0.875*ls.tp)])
         elems += spira.Polygon(layer=ls.M3,shape=[(0.875*ls.tp,0.000*ls.tp),(0.875*ls.tp,0.125*ls.tp),(1.000*ls.tp,0.125*ls.tp),(1.000*ls.tp,0.000*ls.tp)])
         elems += spira.Polygon(layer=ls.M3,shape=[(0.000*ls.tp,0.000*ls.tp),(0.000*ls.tp,0.125*ls.tp),(0.125*ls.tp,0.125*ls.tp),(0.125*ls.tp,0.000*ls.tp)])
         elems += spira.Polygon(layer=ls.I2,shape=[(0.035*ls.tp,0.905*ls.tp),(0.035*ls.tp,0.965*ls.tp),(0.095*ls.tp,0.965*ls.tp),(0.095*ls.tp,0.905*ls.tp)])
         elems += spira.Polygon(layer=ls.I2,shape=[(0.905*ls.tp,0.035*ls.tp),(0.905*ls.tp,0.095*ls.tp),(0.965*ls.tp,0.095*ls.tp),(0.965*ls.tp,0.035*ls.tp)])
         elems += spira.Polygon(layer=ls.M2,shape=[(0.905*ls.tp,0.035*ls.tp),(0.905*ls.tp,0.095*ls.tp),(0.965*ls.tp,0.095*ls.tp),(0.965*ls.tp,0.035*ls.tp)])
         elems += spira.Polygon(layer=ls.M2,shape=[(0.035*ls.tp,0.905*ls.tp),(0.035*ls.tp,0.965*ls.tp),(0.095*ls.tp,0.965*ls.tp),(0.095*ls.tp,0.905*ls.tp)])
         elems += spira.Polygon(layer=ls.I1,shape=[(0.905*ls.tp,0.905*ls.tp),(0.905*ls.tp,0.965*ls.tp),(0.965*ls.tp,0.965*ls.tp),(0.965*ls.tp,0.905*ls.tp)])
         elems += spira.Polygon(layer=ls.I1,shape=[(0.035*ls.tp,0.035*ls.tp),(0.035*ls.tp,0.095*ls.tp),(0.095*ls.tp,0.095*ls.tp),(0.095*ls.tp,0.035*ls.tp)])
         elems += spira.Polygon(layer=ls.M7,shape=[(0.000*ls.tp,0.000*ls.tp),(0.000*ls.tp,1.000*ls.tp),(0.125*ls.tp,1.000*ls.tp),(0.125*ls.tp,0.875*ls.tp),(0.040*ls.tp,0.875*ls.tp),(0.040*ls.tp,0.125*ls.tp),(0.125*ls.tp,0.125*ls.tp),(0.125*ls.tp,0.040*ls.tp),(0.280*ls.tp,0.040*ls.tp),(0.280*ls.tp,0.280*ls.tp),(0.040*ls.tp,0.280*ls.tp),(0.040*ls.tp,0.720*ls.tp),(0.280*ls.tp,0.720*ls.tp),(0.280*ls.tp,0.960*ls.tp),(0.125*ls.tp,0.960*ls.tp),(0.125*ls.tp,1.000*ls.tp),(0.720*ls.tp,1.000*ls.tp),(0.720*ls.tp,0.040*ls.tp),(0.875*ls.tp,0.040*ls.tp),(0.875*ls.tp,0.125*ls.tp),(0.960*ls.tp,0.125*ls.tp),(0.960*ls.tp,0.280*ls.tp),(0.720*ls.tp,0.280*ls.tp),(0.720*ls.tp,0.720*ls.tp),(0.960*ls.tp,0.720*ls.tp),(0.960*ls.tp,0.875*ls.tp),(0.875*ls.tp,0.875*ls.tp),(0.875*ls.tp,0.960*ls.tp),(0.720*ls.tp,0.960*ls.tp),(0.720*ls.tp,1.000*ls.tp),(1.000*ls.tp,1.000*ls.tp),(1.000*ls.tp,0.000*ls.tp)])
         return elems