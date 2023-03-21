v 20091004 2
C 50800 44300 1 0 0 jj-2.sym
{
T 50900 44800 5 10 0 0 0 0 1
device=JOSEPHSON_JUNCTION
T 51250 44950 5 10 1 1 0 0 1
refdes=B2
T 51250 44700 5 10 1 1 0 0 1
model-name=jjmit
T 51250 44450 5 10 1 0 0 0 1
area=B2
}
C 49800 45400 1 0 0 inductor-1.sym
{
T 50000 45900 5 10 0 0 0 0 1
device=INDUCTOR
T 50300 45800 5 10 1 1 180 0 1
refdes=L3
T 50000 46100 5 10 0 0 0 0 1
symversion=0.1
T 50100 45500 5 10 0 1 0 0 1
value=L3
}
C 52300 45400 1 0 0 inductor-1.sym
{
T 52500 45900 5 10 0 0 0 0 1
device=INDUCTOR
T 52600 45700 5 10 1 1 0 0 1
refdes=L4
T 52500 46100 5 10 0 0 0 0 1
symversion=0.1
T 53000 45500 5 10 0 1 0 0 1
value=L4
}
C 50900 44200 1 270 0 inductor-1.sym
{
T 51400 44000 5 10 0 0 270 0 1
device=INDUCTOR
T 51200 43700 5 10 1 1 0 0 1
refdes=LP2
T 51600 44000 5 10 0 0 270 0 1
symversion=0.1
T 51100 43900 5 10 0 1 0 0 1
value=LP2
}
C 51900 44200 1 270 0 inductor-1.sym
{
T 52400 44000 5 10 0 0 270 0 1
device=INDUCTOR
T 52200 43700 5 10 1 1 0 0 1
refdes=LRB2
T 52600 44000 5 10 0 0 270 0 1
symversion=0.1
T 52000 43800 5 10 0 1 0 0 1
value=LRB2
}
C 51400 46700 1 270 0 inductor-1.sym
{
T 51900 46500 5 10 0 0 270 0 1
device=INDUCTOR
T 51700 46200 5 10 1 1 0 0 1
refdes=LB2
T 52100 46500 5 10 0 0 270 0 1
symversion=0.1
T 51500 46200 5 10 0 1 0 0 1
value=LB2
}
C 51900 45200 1 270 0 resistor-1.sym
{
T 52300 44900 5 10 0 0 270 0 1
device=RESISTOR
T 52200 44700 5 10 1 1 0 0 1
refdes=RB2
T 52000 44800 5 10 0 1 0 0 1
value=RB2
}
C 49400 45200 1 270 0 resistor-1.sym
{
T 49800 44900 5 10 0 0 270 0 1
device=RESISTOR
T 49700 44700 5 10 1 1 0 0 1
refdes=R2
T 49400 44300 5 10 0 1 0 0 1
value=R2
}
C 51300 47700 1 270 0 current-1.sym
{
T 52300 47100 5 10 0 0 270 0 1
device=CURRENT_SOURCE
T 51800 47200 5 10 1 1 0 0 1
refdes=IB2
T 51800 47000 5 10 1 1 0 0 1
value=pwl(0 0 5p IB2)
}
C 50800 42900 1 0 0 ground.sym
C 51800 42900 1 0 0 ground.sym
C 49300 43900 1 0 0 ground.sym
C 51700 48100 1 180 0 ground.sym
N 49500 45500 49500 45200 4
N 50700 45500 52300 45500 4
{
T 50800 45500 5 10 0 1 0 0 1
netname=6
}
N 51000 44200 51000 44300 4
{
T 50500 44500 5 10 0 1 0 0 1
netname=7
}
N 51000 43300 51000 43200 4
N 52000 44200 52000 44300 4
{
T 51800 44400 5 10 0 1 0 0 1
netname=106
}
N 52000 43300 52000 43200 4
N 51500 47700 51500 47800 4
N 51500 46800 51500 46700 4
{
T 51300 46800 5 10 0 1 0 0 1
netname=8
}
N 51500 45800 51500 45500 4
N 51000 45200 51000 45500 4
N 52000 45200 52000 45500 4
N 49500 44200 49500 44300 4
N 49800 45500 49500 45500 4
{
T 49600 45500 5 10 0 1 0 0 1
netname=5
}
C 46200 44300 1 0 0 jj-2.sym
{
T 46300 44800 5 10 0 0 0 0 1
device=JOSEPHSON_JUNCTION
T 46650 44950 5 10 1 1 0 0 1
refdes=B1
T 46650 44700 5 10 1 1 0 0 1
model-name=jjmit
T 46650 44450 5 10 1 0 0 0 1
area=B1
}
C 45200 45400 1 0 0 inductor-1.sym
{
T 45400 45900 5 10 0 0 0 0 1
device=INDUCTOR
T 45700 45800 5 10 1 1 180 0 1
refdes=L1
T 45400 46100 5 10 0 0 0 0 1
symversion=0.1
T 45500 45500 5 10 0 1 0 0 1
value=L1
}
C 47700 45400 1 0 0 inductor-1.sym
{
T 47900 45900 5 10 0 0 0 0 1
device=INDUCTOR
T 48000 45700 5 10 1 1 0 0 1
refdes=L2
T 47900 46100 5 10 0 0 0 0 1
symversion=0.1
T 48400 45500 5 10 0 1 0 0 1
value=L2
}
C 46300 44200 1 270 0 inductor-1.sym
{
T 46800 44000 5 10 0 0 270 0 1
device=INDUCTOR
T 46600 43700 5 10 1 1 0 0 1
refdes=LP1
T 47000 44000 5 10 0 0 270 0 1
symversion=0.1
T 46500 43900 5 10 0 1 0 0 1
value=LP1
}
C 47300 44200 1 270 0 inductor-1.sym
{
T 47800 44000 5 10 0 0 270 0 1
device=INDUCTOR
T 47600 43700 5 10 1 1 0 0 1
refdes=LRB1
T 48000 44000 5 10 0 0 270 0 1
symversion=0.1
T 47400 43800 5 10 0 1 0 0 1
value=LRB1
}
C 46800 46700 1 270 0 inductor-1.sym
{
T 47300 46500 5 10 0 0 270 0 1
device=INDUCTOR
T 47100 46200 5 10 1 1 0 0 1
refdes=LB1
T 47500 46500 5 10 0 0 270 0 1
symversion=0.1
T 46900 46200 5 10 0 1 0 0 1
value=LB1
}
C 47300 45200 1 270 0 resistor-1.sym
{
T 47700 44900 5 10 0 0 270 0 1
device=RESISTOR
T 47600 44700 5 10 1 1 0 0 1
refdes=RB1
T 47400 44800 5 10 0 1 0 0 1
value=RB1
}
C 46700 47700 1 270 0 current-1.sym
{
T 47700 47100 5 10 0 0 270 0 1
device=CURRENT_SOURCE
T 47200 47200 5 10 1 1 0 0 1
refdes=IB1
T 47200 47000 5 10 1 1 0 0 1
value=pwl(0 0 5p IB1)
}
C 46200 42900 1 0 0 ground.sym
C 47200 42900 1 0 0 ground.sym
C 47100 48100 1 180 0 ground.sym
N 46100 45500 47700 45500 4
{
T 46200 45500 5 10 0 1 0 0 1
netname=1
}
N 46400 44200 46400 44300 4
{
T 45900 44500 5 10 0 1 0 0 1
netname=2
}
N 46400 43300 46400 43200 4
N 47400 44200 47400 44300 4
{
T 47200 44400 5 10 0 1 0 0 1
netname=101
}
N 47400 43300 47400 43200 4
N 46900 47700 46900 47800 4
N 46900 46800 46900 46700 4
{
T 46700 46800 5 10 0 1 0 0 1
netname=3
}
N 46900 45800 46900 45500 4
N 46400 45200 46400 45500 4
N 47400 45200 47400 45500 4
C 48800 45200 1 270 0 resistor-1.sym
{
T 49200 44900 5 10 0 0 270 0 1
device=RESISTOR
T 49100 44700 5 10 1 1 0 0 1
refdes=R1
T 48800 44300 5 10 0 1 0 0 1
value=R1
}
C 48700 43900 1 0 0 ground.sym
N 48900 44200 48900 44300 4
N 48600 45500 48900 45500 4
{
T 52500 46400 5 10 0 1 0 0 1
netname=4
}
N 48900 45500 48900 45200 4
T 44900 45400 9 20 1 0 0 0 1
A
T 53300 45400 9 20 1 0 0 0 1
Q
