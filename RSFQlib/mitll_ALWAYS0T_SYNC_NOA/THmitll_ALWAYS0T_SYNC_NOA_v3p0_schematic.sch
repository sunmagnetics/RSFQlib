v 20091004 2
C 47800 45900 1 0 0 inductor-1.sym
{
T 48000 46400 5 10 0 0 0 0 1
device=INDUCTOR
T 48000 46200 5 10 1 1 0 0 1
refdes=L1
T 48000 46600 5 10 0 0 0 0 1
symversion=0.1
T 48100 46000 5 10 0 1 0 0 1
value=L1
}
C 50300 45900 1 0 0 inductor-1.sym
{
T 50500 46400 5 10 0 0 0 0 1
device=INDUCTOR
T 50600 46200 5 10 1 1 0 0 1
refdes=L2
T 50500 46600 5 10 0 0 0 0 1
symversion=0.1
T 50600 46000 5 10 0 1 0 0 1
value=L2
}
C 48900 45700 1 270 0 resistor-1.sym
{
T 49300 45400 5 10 0 0 270 0 1
device=RESISTOR
T 49200 45200 5 10 1 1 0 0 1
refdes=R1
T 49000 45300 5 10 0 1 0 0 1
value=R1
}
C 49900 45700 1 270 0 resistor-1.sym
{
T 50300 45400 5 10 0 0 270 0 1
device=RESISTOR
T 50200 45200 5 10 1 1 0 0 1
refdes=R2
T 50000 45300 5 10 0 1 0 0 1
value=R2
}
N 48700 46000 49000 46000 4
{
T 49000 45900 5 10 0 1 0 0 1
netname=1
}
N 49000 46000 49000 45700 4
N 50000 45700 50000 46000 4
{
T 49900 45900 5 10 0 1 0 0 1
netname=2
}
N 50000 46000 50300 46000 4
C 48800 44400 1 0 0 ground.sym
C 49800 44400 1 0 0 ground.sym
N 49000 44700 49000 44800 4
N 50000 44700 50000 44800 4
T 51300 46000 9 15 1 0 0 1 1
Q
T 47200 46000 9 15 1 0 0 1 1
CLK
