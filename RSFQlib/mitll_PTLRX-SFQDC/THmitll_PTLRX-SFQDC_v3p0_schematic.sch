v 20091004 2
C 55300 39300 1 0 0 jj-2.sym
{
T 55400 39800 5 10 0 0 0 0 1
device=JOSEPHSON_JUNCTION
T 55750 39950 5 10 1 1 0 0 1
refdes=B1
T 55750 39700 5 10 1 1 0 0 1
model-name=jjmit
T 55750 39450 5 10 1 0 0 0 1
area=B1
}
C 55400 39200 1 270 0 inductor-1.sym
{
T 55900 39000 5 10 0 0 270 0 1
device=INDUCTOR
T 55700 38700 5 10 1 1 0 0 1
refdes=LP1
T 56100 39000 5 10 0 0 270 0 1
symversion=0.1
T 55600 38900 5 10 0 1 0 0 1
value=LP1
}
C 56400 39200 1 270 0 inductor-1.sym
{
T 56900 39000 5 10 0 0 270 0 1
device=INDUCTOR
T 56700 38700 5 10 1 1 0 0 1
refdes=LRB1
T 57100 39000 5 10 0 0 270 0 1
symversion=0.1
T 56500 38800 5 10 0 1 0 0 1
value=LRB1
}
C 57900 41700 1 270 0 inductor-1.sym
{
T 58400 41500 5 10 0 0 270 0 1
device=INDUCTOR
T 58200 41200 5 10 1 1 0 0 1
refdes=LB1
T 58600 41500 5 10 0 0 270 0 1
symversion=0.1
T 58000 41200 5 10 0 1 0 0 1
value=LB1
}
C 54300 40400 1 0 0 inductor-1.sym
{
T 54500 40900 5 10 0 0 0 0 1
device=INDUCTOR
T 54600 40700 5 10 1 1 0 0 1
refdes=L1
T 54500 41100 5 10 0 0 0 0 1
symversion=0.1
T 54800 40500 5 10 0 1 0 0 1
value=L1
}
C 56800 40400 1 0 0 inductor-1.sym
{
T 57000 40900 5 10 0 0 0 0 1
device=INDUCTOR
T 57100 40700 5 10 1 1 0 0 1
refdes=L2
T 57000 41100 5 10 0 0 0 0 1
symversion=0.1
T 57200 40500 5 10 0 1 0 0 1
value=L2
}
C 57800 42700 1 270 0 current-1.sym
{
T 58800 42100 5 10 0 0 270 0 1
device=CURRENT_SOURCE
T 58300 42200 5 10 1 1 0 0 1
refdes=IB1
T 58300 42000 5 10 1 1 0 0 1
value=pwl(0 0 5p IB1)
}
C 55300 37900 1 0 0 ground.sym
C 56300 37900 1 0 0 ground.sym
C 58200 43100 1 180 0 ground.sym
C 56400 40200 1 270 0 resistor-1.sym
{
T 56800 39900 5 10 0 0 270 0 1
device=RESISTOR
T 56700 39700 5 10 1 1 0 0 1
refdes=RB1
T 56500 39800 5 10 0 1 0 0 1
value=RB1
}
N 55200 40500 56800 40500 4
{
T 56000 40500 5 10 0 1 0 0 1
netname=1
}
N 56500 40200 56500 40500 4
N 55500 40500 55500 40200 4
N 58000 42700 58000 42800 4
N 58000 41800 58000 41700 4
{
T 57700 41900 5 10 0 1 0 0 1
netname=4
}
N 55500 39200 55500 39300 4
{
T 55100 39400 5 10 0 1 0 0 1
netname=2
}
N 55500 38300 55500 38200 4
N 56500 39200 56500 39300 4
{
T 56200 39500 5 10 0 1 0 0 1
netname=101
}
N 56500 38300 56500 38200 4
C 59300 39300 1 0 0 jj-2.sym
{
T 59400 39800 5 10 0 0 0 0 1
device=JOSEPHSON_JUNCTION
T 59750 39950 5 10 1 1 0 0 1
refdes=B2
T 59750 39700 5 10 1 1 0 0 1
model-name=jjmit
T 59750 39450 5 10 1 0 0 0 1
area=B2
}
C 59400 39200 1 270 0 inductor-1.sym
{
T 59900 39000 5 10 0 0 270 0 1
device=INDUCTOR
T 59700 38700 5 10 1 1 0 0 1
refdes=LP2
T 60100 39000 5 10 0 0 270 0 1
symversion=0.1
T 59600 38800 5 10 0 1 0 0 1
value=LP2
}
C 60400 39200 1 270 0 inductor-1.sym
{
T 60900 39000 5 10 0 0 270 0 1
device=INDUCTOR
T 60700 38700 5 10 1 1 0 0 1
refdes=LRB2
T 61100 39000 5 10 0 0 270 0 1
symversion=0.1
T 60500 38700 5 10 0 1 0 0 1
value=LRB2
}
C 58300 40400 1 0 0 inductor-1.sym
{
T 58500 40900 5 10 0 0 0 0 1
device=INDUCTOR
T 58600 40700 5 10 1 1 0 0 1
refdes=L3
T 58500 41100 5 10 0 0 0 0 1
symversion=0.1
T 58800 40600 5 10 0 1 0 0 1
value=L3
}
C 60800 40400 1 0 0 inductor-1.sym
{
T 61000 40900 5 10 0 0 0 0 1
device=INDUCTOR
T 61100 40700 5 10 1 1 0 0 1
refdes=L4
T 61000 41100 5 10 0 0 0 0 1
symversion=0.1
T 61200 40600 5 10 0 1 0 0 1
value=L4
}
C 59300 37900 1 0 0 ground.sym
C 60300 37900 1 0 0 ground.sym
C 60400 40200 1 270 0 resistor-1.sym
{
T 60800 39900 5 10 0 0 270 0 1
device=RESISTOR
T 60700 39700 5 10 1 1 0 0 1
refdes=RB2
T 60400 39900 5 10 0 1 0 0 1
value=RB2
}
N 59200 40500 60800 40500 4
{
T 59900 40600 5 10 0 1 0 0 1
netname=5
}
N 60500 40200 60500 40500 4
N 59500 40500 59500 40200 4
N 59500 39200 59500 39300 4
{
T 59000 39400 5 10 0 1 0 0 1
netname=6
}
N 59500 38300 59500 38200 4
N 60500 39200 60500 39300 4
{
T 60300 39400 5 10 0 1 0 0 1
netname=105
}
N 60500 38300 60500 38200 4
N 57700 40500 58300 40500 4
{
T 57800 40500 5 10 0 1 0 0 1
netname=3
}
N 58000 40800 58000 40500 4
C 61800 39300 1 0 0 jj-2.sym
{
T 61900 39800 5 10 0 0 0 0 1
device=JOSEPHSON_JUNCTION
T 62250 39950 5 10 1 1 0 0 1
refdes=B3
T 62250 39700 5 10 1 1 0 0 1
model-name=jjmit
T 62250 39450 5 10 1 0 0 0 1
area=B3
}
C 61900 39200 1 270 0 inductor-1.sym
{
T 62400 39000 5 10 0 0 270 0 1
device=INDUCTOR
T 62200 38700 5 10 1 1 0 0 1
refdes=LP3
T 62600 39000 5 10 0 0 270 0 1
symversion=0.1
T 62000 38800 5 10 0 1 0 0 1
value=LP3
}
C 62900 39200 1 270 0 inductor-1.sym
{
T 63400 39000 5 10 0 0 270 0 1
device=INDUCTOR
T 63200 38700 5 10 1 1 0 0 1
refdes=LRB3
T 63600 39000 5 10 0 0 270 0 1
symversion=0.1
T 63000 38700 5 10 0 1 0 0 1
value=LRB3
}
C 63300 40400 1 0 0 inductor-1.sym
{
T 63500 40900 5 10 0 0 0 0 1
device=INDUCTOR
T 63600 40700 5 10 1 1 0 0 1
refdes=L5
T 63500 41100 5 10 0 0 0 0 1
symversion=0.1
T 63700 40600 5 10 0 1 0 0 1
value=L5
}
C 61800 37900 1 0 0 ground.sym
C 62800 37900 1 0 0 ground.sym
C 62900 40200 1 270 0 resistor-1.sym
{
T 63300 39900 5 10 0 0 270 0 1
device=RESISTOR
T 63200 39700 5 10 1 1 0 0 1
refdes=RB3
T 63000 39700 5 10 0 1 0 0 1
value=RB3
}
N 61700 40500 63300 40500 4
{
T 62200 40400 5 10 0 1 0 0 1
netname=7
}
N 63000 40200 63000 40500 4
N 62000 40500 62000 40200 4
N 62000 39200 62000 39300 4
{
T 61600 39400 5 10 0 1 0 0 1
netname=8
}
N 62000 38300 62000 38200 4
N 63000 39200 63000 39300 4
{
T 62800 39400 5 10 0 1 0 0 1
netname=107
}
N 63000 38300 63000 38200 4
C 62400 41700 1 270 0 inductor-1.sym
{
T 62900 41500 5 10 0 0 270 0 1
device=INDUCTOR
T 62700 41200 5 10 1 1 0 0 1
refdes=LB2
T 63100 41500 5 10 0 0 270 0 1
symversion=0.1
T 62500 41400 5 10 0 1 0 0 1
value=LB2
}
C 62300 42700 1 270 0 current-1.sym
{
T 63300 42100 5 10 0 0 270 0 1
device=CURRENT_SOURCE
T 62800 42200 5 10 1 1 0 0 1
refdes=IB2
T 62800 42000 5 10 1 1 0 0 1
value=pwl(0 0 5p IB2)
}
C 62700 43100 1 180 0 ground.sym
N 62500 42700 62500 42800 4
N 62500 41800 62500 41700 4
{
T 62000 41900 5 10 0 1 0 0 1
netname=9
}
N 62500 40800 62500 40500 4
C 64400 40200 1 270 0 inductor-1.sym
{
T 64900 40000 5 10 0 0 270 0 1
device=INDUCTOR
T 64700 39700 5 10 1 1 0 0 1
refdes=L8
T 65100 40000 5 10 0 0 270 0 1
symversion=0.1
T 64500 39700 5 10 0 1 0 0 1
value=L8
}
C 64400 41700 1 270 0 inductor-1.sym
{
T 64900 41500 5 10 0 0 270 0 1
device=INDUCTOR
T 64700 41200 5 10 1 1 0 0 1
refdes=L6
T 65100 41500 5 10 0 0 270 0 1
symversion=0.1
T 64500 41300 5 10 0 1 0 0 1
value=L6
}
C 64800 42900 1 0 0 resistor-1.sym
{
T 65100 43300 5 10 0 0 0 0 1
device=RESISTOR
T 65000 43200 5 10 1 1 0 0 1
refdes=RB4
T 65300 42900 5 10 0 1 0 0 1
value=RB4
}
C 65800 42900 1 0 0 inductor-1.sym
{
T 66000 43400 5 10 0 0 0 0 1
device=INDUCTOR
T 66000 43200 5 10 1 1 0 0 1
refdes=LRB4
T 66000 43600 5 10 0 0 0 0 1
symversion=0.1
T 66200 43100 5 10 0 1 0 0 1
value=LRB4
}
N 65800 43000 65700 43000 4
{
T 66000 42600 5 10 0 1 0 0 1
netname=111
}
C 64800 37900 1 0 0 resistor-1.sym
{
T 65100 38300 5 10 0 0 0 0 1
device=RESISTOR
T 65000 38200 5 10 1 1 0 0 1
refdes=RB6
T 65200 38000 5 10 0 1 0 0 1
value=RB6
}
C 65800 37900 1 0 0 inductor-1.sym
{
T 66000 38400 5 10 0 0 0 0 1
device=INDUCTOR
T 66000 38200 5 10 1 1 0 0 1
refdes=LRB6
T 66000 38600 5 10 0 0 0 0 1
symversion=0.1
T 66400 38000 5 10 0 1 0 0 1
value=LRB6
}
N 65800 38000 65700 38000 4
{
T 65800 38000 5 10 0 1 0 0 1
netname=116
}
C 66200 41800 1 90 0 jj-2.sym
{
T 65700 41900 5 10 0 0 90 0 1
device=JOSEPHSON_JUNCTION
T 65550 41550 5 10 1 1 0 0 1
refdes=B4
T 65550 41300 5 10 1 1 0 0 1
model-name=jjmit
T 65550 41050 5 10 1 0 0 0 1
area=B4
}
C 66200 38800 1 90 0 jj-2.sym
{
T 65700 38900 5 10 0 0 90 0 1
device=JOSEPHSON_JUNCTION
T 65550 39850 5 10 1 1 0 0 1
refdes=B6
T 65550 39600 5 10 1 1 0 0 1
model-name=jjmit
T 65550 39350 5 10 1 0 0 0 1
area=B6
}
N 64500 40800 64500 40200 4
{
T 64500 40800 5 10 0 1 0 0 1
netname=10
}
N 64800 39000 64800 38000 4
N 64500 41700 64500 42000 4
{
T 64600 42000 5 10 0 1 0 0 1
netname=11
}
N 64500 42000 65300 42000 4
N 66200 42000 67600 42000 4
{
T 66400 42000 5 10 0 1 0 0 1
netname=12
}
N 66700 42000 66700 43000 4
N 64500 39000 65300 39000 4
{
T 64500 39000 5 10 0 1 0 0 1
netname=16
}
N 66700 38000 66700 39000 4
N 66200 39000 67600 39000 4
{
T 66200 39000 5 10 0 1 0 0 1
netname=17
}
N 64200 40500 64500 40500 4
C 66900 43200 1 270 0 inductor-1.sym
{
T 67400 43000 5 10 0 0 270 0 1
device=INDUCTOR
T 67200 42700 5 10 1 1 0 0 1
refdes=LB3
T 67600 43000 5 10 0 0 270 0 1
symversion=0.1
T 67000 42700 5 10 0 1 0 0 1
value=LB3
}
C 66800 44200 1 270 0 current-1.sym
{
T 67800 43600 5 10 0 0 270 0 1
device=CURRENT_SOURCE
T 67300 43700 5 10 1 1 0 0 1
refdes=IB3
T 67300 43500 5 10 1 1 0 0 1
value=pwl(0 0 5p IB3)
}
C 67200 44600 1 180 0 ground.sym
N 67000 44200 67000 44300 4
N 67000 43300 67000 43200 4
{
T 66900 43400 5 10 0 1 0 0 1
netname=14
}
N 67000 42300 67000 42000 4
C 67200 41700 1 270 0 inductor-1.sym
{
T 67700 41500 5 10 0 0 270 0 1
device=INDUCTOR
T 67500 41200 5 10 1 1 0 0 1
refdes=L7
T 67900 41500 5 10 0 0 270 0 1
symversion=0.1
T 67400 41300 5 10 0 1 0 0 1
value=L7
}
C 67200 40200 1 270 0 inductor-1.sym
{
T 67700 40000 5 10 0 0 270 0 1
device=INDUCTOR
T 67500 39700 5 10 1 1 0 0 1
refdes=L9
T 67900 40000 5 10 0 0 270 0 1
symversion=0.1
T 67200 39700 5 10 0 1 0 0 1
value=L9
}
C 68500 41800 1 90 0 jj-2.sym
{
T 68000 41900 5 10 0 0 90 0 1
device=JOSEPHSON_JUNCTION
T 67850 41550 5 10 1 1 0 0 1
refdes=B5
T 67850 41300 5 10 1 1 0 0 1
model-name=jjmit
T 67850 41050 5 10 1 0 0 0 1
area=B5
}
C 68600 41900 1 0 0 inductor-1.sym
{
T 68800 42400 5 10 0 0 0 0 1
device=INDUCTOR
T 68800 42200 5 10 1 1 0 0 1
refdes=LP5
T 68800 42600 5 10 0 0 0 0 1
symversion=0.1
T 69000 42100 5 10 0 1 0 0 1
value=LP5
}
C 68600 42900 1 0 0 inductor-1.sym
{
T 68800 43400 5 10 0 0 0 0 1
device=INDUCTOR
T 68800 43200 5 10 1 1 0 0 1
refdes=LRB5
T 68800 43600 5 10 0 0 0 0 1
symversion=0.1
T 69100 43000 5 10 0 1 0 0 1
value=LRB5
}
C 69900 41800 1 90 0 ground.sym
C 69900 42800 1 90 0 ground.sym
C 67600 42900 1 0 0 resistor-1.sym
{
T 67900 43300 5 10 0 0 0 0 1
device=RESISTOR
T 67800 43200 5 10 1 1 0 0 1
refdes=RB5
T 68100 43000 5 10 0 1 0 0 1
value=RB5
}
N 68600 42000 68500 42000 4
{
T 68700 41700 5 10 0 1 0 0 1
netname=13
}
N 69500 42000 69600 42000 4
N 68600 43000 68500 43000 4
{
T 68700 42700 5 10 0 1 0 0 1
netname=112
}
N 69500 43000 69600 43000 4
N 67600 43000 67600 42000 4
N 67300 41700 67300 42000 4
C 68500 38800 1 90 0 jj-2.sym
{
T 68000 38900 5 10 0 0 90 0 1
device=JOSEPHSON_JUNCTION
T 67850 39850 5 10 1 1 0 0 1
refdes=B7
T 67850 39600 5 10 1 1 0 0 1
model-name=jjmit
T 67850 39350 5 10 1 0 0 0 1
area=B7
}
C 68600 38900 1 0 0 inductor-1.sym
{
T 68800 39400 5 10 0 0 0 0 1
device=INDUCTOR
T 68800 39200 5 10 1 1 0 0 1
refdes=LP7
T 68800 39600 5 10 0 0 0 0 1
symversion=0.1
T 69100 39100 5 10 0 1 0 0 1
value=LP7
}
C 69900 38800 1 90 0 ground.sym
N 68600 39000 68500 39000 4
{
T 68700 38700 5 10 0 1 0 0 1
netname=18
}
N 69500 39000 69600 39000 4
C 68600 37900 1 0 0 inductor-1.sym
{
T 68800 38400 5 10 0 0 0 0 1
device=INDUCTOR
T 68800 38200 5 10 1 1 0 0 1
refdes=LRB7
T 68800 38600 5 10 0 0 0 0 1
symversion=0.1
T 69100 38100 5 10 0 1 0 0 1
value=LRB7
}
C 69900 37800 1 90 0 ground.sym
C 67600 37900 1 0 0 resistor-1.sym
{
T 67900 38300 5 10 0 0 0 0 1
device=RESISTOR
T 67800 38200 5 10 1 1 0 0 1
refdes=RB7
T 67900 37900 5 10 0 1 0 0 1
value=RB7
}
N 68600 38000 68500 38000 4
{
T 68700 37700 5 10 0 1 0 0 1
netname=117
}
N 69500 38000 69600 38000 4
N 67600 38000 67600 39000 4
N 67300 39300 67300 39000 4
N 67300 40800 67300 40200 4
{
T 67300 40400 5 10 0 1 0 0 1
netname=15
}
C 66100 40400 1 0 0 inductor-1.sym
{
T 66300 40900 5 10 0 0 0 0 1
device=INDUCTOR
T 66400 40700 5 10 1 1 0 0 1
refdes=LR1
T 66300 41100 5 10 0 0 0 0 1
symversion=0.1
T 66600 40600 5 10 0 1 0 0 1
value=LR1
}
C 65100 40400 1 0 0 resistor-1.sym
{
T 65400 40800 5 10 0 0 0 0 1
device=RESISTOR
T 65400 40700 5 10 1 1 0 0 1
refdes=R1
T 65400 40500 5 10 0 1 0 0 1
value=R1
}
N 64800 42000 64800 43000 4
N 64500 39000 64500 39300 4
C 64700 40700 1 270 0 ground.sym
N 65100 40500 65000 40500 4
N 66000 40500 66100 40500 4
{
T 66000 40500 5 10 0 1 0 0 1
netname=19
}
N 67000 40500 67300 40500 4
C 67600 40400 1 0 0 inductor-1.sym
{
T 67800 40900 5 10 0 0 0 0 1
device=INDUCTOR
T 67900 40700 5 10 1 1 0 0 1
refdes=L10
T 67800 41100 5 10 0 0 0 0 1
symversion=0.1
T 68100 40500 5 10 0 1 0 0 1
value=L10
}
N 67600 40500 67300 40500 4
C 68800 41400 1 0 0 resistor-1.sym
{
T 69100 41800 5 10 0 0 0 0 1
device=RESISTOR
T 69000 41700 5 10 1 1 0 0 1
refdes=RB8
T 69100 41500 5 10 0 1 0 0 1
value=RB8
}
C 69800 41400 1 0 0 inductor-1.sym
{
T 70000 41900 5 10 0 0 0 0 1
device=INDUCTOR
T 70000 41700 5 10 1 1 0 0 1
refdes=LRB8
T 70000 42100 5 10 0 0 0 0 1
symversion=0.1
T 70300 41500 5 10 0 1 0 0 1
value=LRB8
}
N 69800 41500 69700 41500 4
{
T 70000 40900 5 10 0 1 0 0 1
netname=120
}
C 70200 40300 1 90 0 jj-2.sym
{
T 69700 40400 5 10 0 0 90 0 1
device=JOSEPHSON_JUNCTION
T 69550 40050 5 10 1 1 0 0 1
refdes=B8
T 69550 39800 5 10 1 1 0 0 1
model-name=jjmit
T 69550 39550 5 10 1 0 0 0 1
area=B8
}
N 70700 40500 70700 41500 4
N 68800 40500 68800 41500 4
N 69300 40500 68500 40500 4
{
T 68600 40400 5 10 0 1 0 0 1
netname=20
}
C 70900 41700 1 270 0 inductor-1.sym
{
T 71400 41500 5 10 0 0 270 0 1
device=INDUCTOR
T 71200 41200 5 10 1 1 0 0 1
refdes=LB4
T 71600 41500 5 10 0 0 270 0 1
symversion=0.1
T 71000 41400 5 10 0 1 0 0 1
value=LB4
}
C 70800 42700 1 270 0 current-1.sym
{
T 71800 42100 5 10 0 0 270 0 1
device=CURRENT_SOURCE
T 71300 42200 5 10 1 1 0 0 1
refdes=IB4
T 71300 42000 5 10 1 1 0 0 1
value=pwl(0 0 5p IB4)
}
C 71200 43100 1 180 0 ground.sym
N 71000 42700 71000 42800 4
N 71000 41800 71000 41700 4
{
T 70700 41900 5 10 0 1 0 0 1
netname=22
}
N 71000 40800 71000 40500 4
C 71300 40400 1 0 0 inductor-1.sym
{
T 71500 40900 5 10 0 0 0 0 1
device=INDUCTOR
T 71600 40700 5 10 1 1 0 0 1
refdes=L11
T 71500 41100 5 10 0 0 0 0 1
symversion=0.1
T 71600 40600 5 10 0 1 0 0 1
value=L11
}
N 71300 40500 70200 40500 4
{
T 70300 40500 5 10 0 1 0 0 1
netname=21
}
C 72300 39300 1 0 0 jj-2.sym
{
T 72400 39800 5 10 0 0 0 0 1
device=JOSEPHSON_JUNCTION
T 72750 39950 5 10 1 1 0 0 1
refdes=B9
T 72750 39700 5 10 1 1 0 0 1
model-name=jjmit
T 72750 39450 5 10 1 0 0 0 1
area=B9
}
C 72400 39200 1 270 0 inductor-1.sym
{
T 72900 39000 5 10 0 0 270 0 1
device=INDUCTOR
T 72700 38700 5 10 1 1 0 0 1
refdes=LP9
T 73100 39000 5 10 0 0 270 0 1
symversion=0.1
T 72500 38800 5 10 0 1 0 0 1
value=LP9
}
C 73400 39200 1 270 0 inductor-1.sym
{
T 73900 39000 5 10 0 0 270 0 1
device=INDUCTOR
T 73700 38700 5 10 1 1 0 0 1
refdes=LRB9
T 74100 39000 5 10 0 0 270 0 1
symversion=0.1
T 73500 38800 5 10 0 1 0 0 1
value=LRB9
}
C 74900 41700 1 270 0 inductor-1.sym
{
T 75400 41500 5 10 0 0 270 0 1
device=INDUCTOR
T 75200 41200 5 10 1 1 0 0 1
refdes=LB5
T 75600 41500 5 10 0 0 270 0 1
symversion=0.1
T 75100 41300 5 10 0 1 0 0 1
value=LB5
}
C 73800 40400 1 0 0 inductor-1.sym
{
T 74000 40900 5 10 0 0 0 0 1
device=INDUCTOR
T 74100 40700 5 10 1 1 0 0 1
refdes=L12
T 74000 41100 5 10 0 0 0 0 1
symversion=0.1
T 74100 40500 5 10 0 1 0 0 1
value=L12
}
C 74800 42700 1 270 0 current-1.sym
{
T 75800 42100 5 10 0 0 270 0 1
device=CURRENT_SOURCE
T 75300 42200 5 10 1 1 0 0 1
refdes=IB5
T 75300 42000 5 10 1 1 0 0 1
value=pwl(0 0 5p IB5)
}
C 72300 37900 1 0 0 ground.sym
C 73300 37900 1 0 0 ground.sym
C 75200 43100 1 180 0 ground.sym
N 72200 40500 73800 40500 4
{
T 73000 40500 5 10 0 1 0 0 1
netname=23
}
N 73500 40200 73500 40500 4
N 72500 40500 72500 40200 4
N 75000 42700 75000 42800 4
N 75000 41800 75000 41700 4
{
T 74600 41900 5 10 0 1 0 0 1
netname=26
}
N 72500 39200 72500 39300 4
{
T 72000 39400 5 10 0 1 0 0 1
netname=24
}
N 72500 38300 72500 38200 4
N 73500 39200 73500 39300 4
{
T 72900 39400 5 10 0 1 0 0 1
netname=123
}
N 73500 38300 73500 38200 4
C 76300 39300 1 0 0 jj-2.sym
{
T 76400 39800 5 10 0 0 0 0 1
device=JOSEPHSON_JUNCTION
T 76750 39950 5 10 1 1 0 0 1
refdes=B10
T 76750 39700 5 10 1 1 0 0 1
model-name=jjmit
T 76750 39450 5 10 1 0 0 0 1
area=B10
}
C 76400 39200 1 270 0 inductor-1.sym
{
T 76900 39000 5 10 0 0 270 0 1
device=INDUCTOR
T 76700 38700 5 10 1 1 0 0 1
refdes=LP10
T 77100 39000 5 10 0 0 270 0 1
symversion=0.1
T 76500 38800 5 10 0 1 0 0 1
value=LP10
}
C 77400 39200 1 270 0 inductor-1.sym
{
T 77900 39000 5 10 0 0 270 0 1
device=INDUCTOR
T 77700 38700 5 10 1 1 0 0 1
refdes=LRB10
T 78100 39000 5 10 0 0 270 0 1
symversion=0.1
T 77600 38800 5 10 0 1 0 0 1
value=LRB10
}
C 75300 40400 1 0 0 inductor-1.sym
{
T 75500 40900 5 10 0 0 0 0 1
device=INDUCTOR
T 75600 40700 5 10 1 1 0 0 1
refdes=L13
T 75500 41100 5 10 0 0 0 0 1
symversion=0.1
T 75600 40500 5 10 0 1 0 0 1
value=L13
}
C 77800 40400 1 0 0 inductor-1.sym
{
T 78000 40900 5 10 0 0 0 0 1
device=INDUCTOR
T 78100 40700 5 10 1 1 0 0 1
refdes=L14
T 78000 41100 5 10 0 0 0 0 1
symversion=0.1
T 78200 40500 5 10 0 1 0 0 1
value=L14
}
C 76300 37900 1 0 0 ground.sym
C 77300 37900 1 0 0 ground.sym
C 77400 40200 1 270 0 resistor-1.sym
{
T 77800 39900 5 10 0 0 270 0 1
device=RESISTOR
T 77700 39700 5 10 1 1 0 0 1
refdes=RB10
T 77500 40000 5 10 0 1 0 0 1
value=RB10
}
N 76200 40500 77800 40500 4
{
T 76900 40500 5 10 0 1 0 0 1
netname=27
}
N 77500 40200 77500 40500 4
N 76500 40500 76500 40200 4
N 76500 39200 76500 39300 4
{
T 76100 39600 5 10 0 1 0 0 1
netname=28
}
N 76500 38300 76500 38200 4
N 77500 39200 77500 39300 4
{
T 77100 39400 5 10 0 1 0 0 1
netname=127
}
N 77500 38300 77500 38200 4
N 74700 40500 75300 40500 4
{
T 75200 40600 5 10 0 1 0 0 1
netname=25
}
N 75000 40800 75000 40500 4
C 73400 40200 1 270 0 resistor-1.sym
{
T 73800 39900 5 10 0 0 270 0 1
device=RESISTOR
T 73700 39700 5 10 1 1 0 0 1
refdes=RB9
T 74200 40000 5 10 0 1 0 0 1
value=RB9
}
T 78800 40400 9 20 1 0 0 0 1
Q
T 54000 40400 9 20 1 0 0 0 1
A
