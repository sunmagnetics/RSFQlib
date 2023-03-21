v 20091004 2
C 32300 43300 1 0 0 jj-2.sym
{
T 32400 43800 5 10 0 0 0 0 1
device=JOSEPHSON_JUNCTION
T 32750 43950 5 10 1 1 0 0 1
refdes=B1
T 32750 43700 5 10 1 1 0 0 1
model-name=jjmit
T 32750 43450 5 10 1 0 0 0 1
area=B1
}
C 31300 44400 1 0 0 inductor-1.sym
{
T 31500 44900 5 10 0 0 0 0 1
device=INDUCTOR
T 31600 44700 5 10 1 1 0 0 1
refdes=L1
T 31500 45100 5 10 0 0 0 0 1
symversion=0.1
T 31900 44500 5 10 0 1 0 0 1
value=L1
}
C 32400 43200 1 270 0 inductor-1.sym
{
T 32900 43000 5 10 0 0 270 0 1
device=INDUCTOR
T 32700 42700 5 10 1 1 0 0 1
refdes=LP1
T 33100 43000 5 10 0 0 270 0 1
symversion=0.1
T 32500 42800 5 10 0 1 0 0 1
value=LP1
}
C 33400 43200 1 270 0 inductor-1.sym
{
T 33900 43000 5 10 0 0 270 0 1
device=INDUCTOR
T 33700 42700 5 10 1 1 0 0 1
refdes=LRB1
T 34100 43000 5 10 0 0 270 0 1
symversion=0.1
T 33600 42800 5 10 0 1 0 0 1
value=LRB1
}
C 32900 45700 1 270 0 inductor-1.sym
{
T 33400 45500 5 10 0 0 270 0 1
device=INDUCTOR
T 33200 45200 5 10 1 1 0 0 1
refdes=LB1
T 33600 45500 5 10 0 0 270 0 1
symversion=0.1
T 33100 45300 5 10 0 1 0 0 1
value=LB1
}
C 33400 44200 1 270 0 resistor-1.sym
{
T 33800 43900 5 10 0 0 270 0 1
device=RESISTOR
T 33700 43700 5 10 1 1 0 0 1
refdes=RB1
T 33600 43800 5 10 0 1 0 0 1
value=RB1
}
C 32800 46700 1 270 0 current-1.sym
{
T 33800 46100 5 10 0 0 270 0 1
device=CURRENT_SOURCE
T 33300 46200 5 10 1 1 0 0 1
refdes=IB1
T 33300 46000 5 10 1 1 0 0 1
value=pwl(0 0 5p IB1)
}
C 32300 41900 1 0 0 ground.sym
C 33300 41900 1 0 0 ground.sym
C 33200 47100 1 180 0 ground.sym
N 32500 43200 32500 43300 4
{
T 32000 43500 5 10 0 1 0 0 1
netname=2
}
N 32500 42300 32500 42200 4
N 33500 43200 33500 43300 4
{
T 33300 43400 5 10 0 1 0 0 1
netname=101
}
N 33500 42300 33500 42200 4
N 33800 44500 32200 44500 4
{
T 33000 44600 5 10 0 1 0 0 1
netname=1
}
N 33000 45800 33000 45700 4
{
T 32700 45900 5 10 0 1 0 0 1
netname=3
}
N 33000 46700 33000 46800 4
N 33500 44200 33500 44500 4
N 32500 44200 32500 44500 4
C 34800 43300 1 0 0 jj-2.sym
{
T 34900 43800 5 10 0 0 0 0 1
device=JOSEPHSON_JUNCTION
T 35250 43950 5 10 1 1 0 0 1
refdes=B2
T 35250 43700 5 10 1 1 0 0 1
model-name=jjmit
T 35250 43450 5 10 1 0 0 0 1
area=B2
}
C 34900 43200 1 270 0 inductor-1.sym
{
T 35400 43000 5 10 0 0 270 0 1
device=INDUCTOR
T 35200 42700 5 10 1 1 0 0 1
refdes=LP2
T 35600 43000 5 10 0 0 270 0 1
symversion=0.1
T 35000 42800 5 10 0 1 0 0 1
value=LP2
}
C 35900 43200 1 270 0 inductor-1.sym
{
T 36400 43000 5 10 0 0 270 0 1
device=INDUCTOR
T 36200 42700 5 10 1 1 0 0 1
refdes=LRB2
T 36600 43000 5 10 0 0 270 0 1
symversion=0.1
T 36100 42800 5 10 0 1 0 0 1
value=LRB2
}
C 35900 44200 1 270 0 resistor-1.sym
{
T 36300 43900 5 10 0 0 270 0 1
device=RESISTOR
T 36200 43700 5 10 1 1 0 0 1
refdes=RB2
T 35900 43800 5 10 0 1 0 0 1
value=RB2
}
C 34800 41900 1 0 0 ground.sym
C 35800 41900 1 0 0 ground.sym
N 35000 43200 35000 43300 4
{
T 34500 43500 5 10 0 1 0 0 1
netname=5
}
N 35000 42300 35000 42200 4
N 36000 43200 36000 43300 4
{
T 35700 43400 5 10 0 1 0 0 1
netname=104
}
N 36000 42300 36000 42200 4
N 36300 44500 34700 44500 4
{
T 35300 44400 5 10 0 1 0 0 1
netname=4
}
N 36000 44200 36000 44500 4
N 35000 44200 35000 44500 4
C 37300 43300 1 0 0 jj-2.sym
{
T 37400 43800 5 10 0 0 0 0 1
device=JOSEPHSON_JUNCTION
T 37750 43950 5 10 1 1 0 0 1
refdes=B3
T 37750 43700 5 10 1 1 0 0 1
model-name=jjmit
T 37750 43450 5 10 1 0 0 0 1
area=B3
}
C 37400 43200 1 270 0 inductor-1.sym
{
T 37900 43000 5 10 0 0 270 0 1
device=INDUCTOR
T 37700 42700 5 10 1 1 0 0 1
refdes=LP3
T 38100 43000 5 10 0 0 270 0 1
symversion=0.1
T 37500 42600 5 10 0 1 0 0 1
value=LP3
}
C 38400 43200 1 270 0 inductor-1.sym
{
T 38900 43000 5 10 0 0 270 0 1
device=INDUCTOR
T 38700 42700 5 10 1 1 0 0 1
refdes=LRB3
T 39100 43000 5 10 0 0 270 0 1
symversion=0.1
T 38400 42800 5 10 0 1 0 0 1
value=LRB3
}
C 38400 44200 1 270 0 resistor-1.sym
{
T 38800 43900 5 10 0 0 270 0 1
device=RESISTOR
T 38700 43700 5 10 1 1 0 0 1
refdes=RB3
T 38600 43700 5 10 0 1 0 0 1
value=RB3
}
C 37300 41900 1 0 0 ground.sym
C 38300 41900 1 0 0 ground.sym
N 37500 43200 37500 43300 4
{
T 36900 43600 5 10 0 1 0 0 1
netname=8
}
N 37500 42300 37500 42200 4
N 38500 43200 38500 43300 4
{
T 38100 43300 5 10 0 1 0 0 1
netname=107
}
N 38500 42300 38500 42200 4
N 38800 44500 37200 44500 4
{
T 37200 40100 5 10 0 1 0 0 1
netname=7
}
N 38500 44200 38500 44500 4
N 37500 44200 37500 44500 4
C 38800 45400 1 0 0 resistor-1.sym
{
T 39100 45800 5 10 0 0 0 0 1
device=RESISTOR
T 39000 45700 5 10 1 1 0 0 1
refdes=RB4
T 39300 45500 5 10 0 1 0 0 1
value=RB4
}
C 39800 45400 1 0 0 inductor-1.sym
{
T 40000 45900 5 10 0 0 0 0 1
device=INDUCTOR
T 40000 45700 5 10 1 1 0 0 1
refdes=LRB4
T 40000 46100 5 10 0 0 0 0 1
symversion=0.1
T 40300 45500 5 10 0 1 0 0 1
value=LRB4
}
N 39800 45500 39700 45500 4
{
T 40000 45200 5 10 0 1 0 0 1
netname=109
}
C 40200 44300 1 90 0 jj-2.sym
{
T 39700 44400 5 10 0 0 90 0 1
device=JOSEPHSON_JUNCTION
T 39550 44050 5 10 1 1 0 0 1
refdes=B4
T 39550 43800 5 10 1 1 0 0 1
model-name=jjmit
T 39550 43550 5 10 1 0 0 0 1
area=B4
}
N 39300 44500 38500 44500 4
N 38800 45500 38800 44500 4
N 40700 44500 40700 45500 4
C 32300 38300 1 0 0 jj-2.sym
{
T 32400 38800 5 10 0 0 0 0 1
device=JOSEPHSON_JUNCTION
T 32750 38950 5 10 1 1 0 0 1
refdes=B5
T 32750 38700 5 10 1 1 0 0 1
model-name=jjmit
T 32750 38450 5 10 1 0 0 0 1
area=B5
}
C 32400 38200 1 270 0 inductor-1.sym
{
T 32900 38000 5 10 0 0 270 0 1
device=INDUCTOR
T 32700 37700 5 10 1 1 0 0 1
refdes=LP5
T 33100 38000 5 10 0 0 270 0 1
symversion=0.1
T 32600 37700 5 10 0 1 0 0 1
value=LP5
}
C 33400 38200 1 270 0 inductor-1.sym
{
T 33900 38000 5 10 0 0 270 0 1
device=INDUCTOR
T 33700 37700 5 10 1 1 0 0 1
refdes=LRB5
T 34100 38000 5 10 0 0 270 0 1
symversion=0.1
T 33500 37800 5 10 0 1 0 0 1
value=LRB5
}
C 35400 45700 1 270 0 inductor-1.sym
{
T 35900 45500 5 10 0 0 270 0 1
device=INDUCTOR
T 35700 45200 5 10 1 1 0 0 1
refdes=LB2
T 36100 45500 5 10 0 0 270 0 1
symversion=0.1
T 35600 45300 5 10 0 1 0 0 1
value=LB2
}
C 33400 39200 1 270 0 resistor-1.sym
{
T 33800 38900 5 10 0 0 270 0 1
device=RESISTOR
T 33700 38700 5 10 1 1 0 0 1
refdes=RB5
T 33500 38800 5 10 0 1 0 0 1
value=RB5
}
C 35300 46700 1 270 0 current-1.sym
{
T 36300 46100 5 10 0 0 270 0 1
device=CURRENT_SOURCE
T 35800 46200 5 10 1 1 0 0 1
refdes=IB2
T 35800 46000 5 10 1 1 0 0 1
value=pwl(0 0 5p IB2)
}
C 32300 36900 1 0 0 ground.sym
C 33300 36900 1 0 0 ground.sym
N 32500 38200 32500 38300 4
{
T 31900 38400 5 10 0 1 0 0 1
netname=12
}
N 32500 37300 32500 37200 4
N 33500 38200 33500 38300 4
{
T 33300 38300 5 10 0 1 0 0 1
netname=111
}
N 33500 37300 33500 37200 4
N 33800 39500 32200 39500 4
{
T 33100 39500 5 10 0 1 0 0 1
netname=11
}
N 33500 39200 33500 39500 4
N 32500 39200 32500 39500 4
C 34800 38300 1 0 0 jj-2.sym
{
T 34900 38800 5 10 0 0 0 0 1
device=JOSEPHSON_JUNCTION
T 35250 38950 5 10 1 1 0 0 1
refdes=B6
T 35250 38700 5 10 1 1 0 0 1
model-name=jjmit
T 35250 38450 5 10 1 0 0 0 1
area=B6
}
C 34900 38200 1 270 0 inductor-1.sym
{
T 35400 38000 5 10 0 0 270 0 1
device=INDUCTOR
T 35200 37700 5 10 1 1 0 0 1
refdes=LP6
T 35600 38000 5 10 0 0 270 0 1
symversion=0.1
T 35100 37800 5 10 0 1 0 0 1
value=LP6
}
C 35900 38200 1 270 0 inductor-1.sym
{
T 36400 38000 5 10 0 0 270 0 1
device=INDUCTOR
T 36200 37700 5 10 1 1 0 0 1
refdes=LRB6
T 36600 38000 5 10 0 0 270 0 1
symversion=0.1
T 36000 37700 5 10 0 1 0 0 1
value=LRB6
}
C 35900 39200 1 270 0 resistor-1.sym
{
T 36300 38900 5 10 0 0 270 0 1
device=RESISTOR
T 36200 38700 5 10 1 1 0 0 1
refdes=RB6
T 36000 38800 5 10 0 1 0 0 1
value=RB6
}
C 34800 36900 1 0 0 ground.sym
C 35800 36900 1 0 0 ground.sym
N 35000 38200 35000 38300 4
{
T 34500 38400 5 10 0 1 0 0 1
netname=15
}
N 35000 37300 35000 37200 4
N 36000 38200 36000 38300 4
{
T 35700 38400 5 10 0 1 0 0 1
netname=114
}
N 36000 37300 36000 37200 4
N 36300 39500 34700 39500 4
{
T 35500 39500 5 10 0 1 0 0 1
netname=14
}
N 36000 39200 36000 39500 4
N 35000 39200 35000 39500 4
C 37300 38300 1 0 0 jj-2.sym
{
T 37400 38800 5 10 0 0 0 0 1
device=JOSEPHSON_JUNCTION
T 37750 38950 5 10 1 1 0 0 1
refdes=B7
T 37750 38700 5 10 1 1 0 0 1
model-name=jjmit
T 37750 38450 5 10 1 0 0 0 1
area=B7
}
C 37400 38200 1 270 0 inductor-1.sym
{
T 37900 38000 5 10 0 0 270 0 1
device=INDUCTOR
T 37700 37700 5 10 1 1 0 0 1
refdes=LP7
T 38100 38000 5 10 0 0 270 0 1
symversion=0.1
T 37400 37700 5 10 0 1 0 0 1
value=LP7
}
C 38400 38200 1 270 0 inductor-1.sym
{
T 38900 38000 5 10 0 0 270 0 1
device=INDUCTOR
T 38700 37700 5 10 1 1 0 0 1
refdes=LRB7
T 39100 38000 5 10 0 0 270 0 1
symversion=0.1
T 38600 37700 5 10 0 1 0 0 1
value=LRB7
}
C 38400 39200 1 270 0 resistor-1.sym
{
T 38800 38900 5 10 0 0 270 0 1
device=RESISTOR
T 38700 38700 5 10 1 1 0 0 1
refdes=RB7
T 38700 38900 5 10 0 1 0 0 1
value=RB7
}
C 37300 36900 1 0 0 ground.sym
C 38300 36900 1 0 0 ground.sym
N 37500 38200 37500 38300 4
{
T 37200 38400 5 10 0 1 0 0 1
netname=18
}
N 37500 37300 37500 37200 4
N 38500 38200 38500 38300 4
{
T 38200 38400 5 10 0 1 0 0 1
netname=117
}
N 38500 37300 38500 37200 4
N 37200 39500 39300 39500 4
{
T 38000 39600 5 10 0 1 0 0 1
netname=17
}
N 38500 39200 38500 39500 4
N 37500 39200 37500 39500 4
C 38800 40400 1 0 0 resistor-1.sym
{
T 39100 40800 5 10 0 0 0 0 1
device=RESISTOR
T 39000 40700 5 10 1 1 0 0 1
refdes=RB8
T 39200 40400 5 10 0 1 0 0 1
value=RB8
}
C 39800 40400 1 0 0 inductor-1.sym
{
T 40000 40900 5 10 0 0 0 0 1
device=INDUCTOR
T 40000 40700 5 10 1 1 0 0 1
refdes=LRB8
T 40000 41100 5 10 0 0 0 0 1
symversion=0.1
T 40100 40700 5 10 0 1 0 0 1
value=LRB8
}
N 39800 40500 39700 40500 4
{
T 39800 40400 5 10 0 1 0 0 1
netname=119
}
C 40200 39300 1 90 0 jj-2.sym
{
T 39700 39400 5 10 0 0 90 0 1
device=JOSEPHSON_JUNCTION
T 39550 39050 5 10 1 1 0 0 1
refdes=B8
T 39550 38800 5 10 1 1 0 0 1
model-name=jjmit
T 39550 38550 5 10 1 0 0 0 1
area=B8
}
N 38800 40500 38800 39500 4
N 40200 39500 41000 39500 4
{
T 40200 39500 5 10 0 1 0 0 1
netname=19
}
N 40700 39500 40700 40500 4
N 42200 39500 42200 44500 4
{
T 42200 42900 5 10 0 1 0 0 1
netname=10
}
C 44000 42900 1 0 0 resistor-1.sym
{
T 44300 43300 5 10 0 0 0 0 1
device=RESISTOR
T 44200 43200 5 10 1 1 0 0 1
refdes=RB9
T 44600 43100 5 10 0 1 0 0 1
value=RB9
}
C 45000 42900 1 0 0 inductor-1.sym
{
T 45200 43400 5 10 0 0 0 0 1
device=INDUCTOR
T 45200 43200 5 10 1 1 0 0 1
refdes=LRB9
T 45200 43600 5 10 0 0 0 0 1
symversion=0.1
T 45500 43100 5 10 0 1 0 0 1
value=LRB9
}
N 45000 43000 44900 43000 4
{
T 45200 42700 5 10 0 1 0 0 1
netname=121
}
C 45400 41800 1 90 0 jj-2.sym
{
T 44900 41900 5 10 0 0 90 0 1
device=JOSEPHSON_JUNCTION
T 44750 41550 5 10 1 1 0 0 1
refdes=B9
T 44750 41300 5 10 1 1 0 0 1
model-name=jjmit
T 44750 41050 5 10 1 0 0 0 1
area=B9
}
N 44500 42000 43700 42000 4
{
T 44200 42000 5 10 0 1 0 0 1
netname=21
}
N 44000 43000 44000 42000 4
N 45900 42000 45900 43000 4
C 46000 40800 1 0 0 jj-2.sym
{
T 46100 41300 5 10 0 0 0 0 1
device=JOSEPHSON_JUNCTION
T 46450 41450 5 10 1 1 0 0 1
refdes=B10
T 46450 41200 5 10 1 1 0 0 1
model-name=jjmit
T 46450 40950 5 10 1 0 0 0 1
area=B10
}
C 46100 40700 1 270 0 inductor-1.sym
{
T 46600 40500 5 10 0 0 270 0 1
device=INDUCTOR
T 46400 40200 5 10 1 1 0 0 1
refdes=LP10
T 46800 40500 5 10 0 0 270 0 1
symversion=0.1
T 46200 40200 5 10 0 1 0 0 1
value=LP10
}
C 47100 40700 1 270 0 inductor-1.sym
{
T 47600 40500 5 10 0 0 270 0 1
device=INDUCTOR
T 47400 40200 5 10 1 1 0 0 1
refdes=LRB10
T 47800 40500 5 10 0 0 270 0 1
symversion=0.1
T 47300 40300 5 10 0 1 0 0 1
value=LRB10
}
C 47100 41700 1 270 0 resistor-1.sym
{
T 47500 41400 5 10 0 0 270 0 1
device=RESISTOR
T 47400 41200 5 10 1 1 0 0 1
refdes=RB10
T 47200 41400 5 10 0 1 0 0 1
value=RB10
}
C 46000 39400 1 0 0 ground.sym
C 47000 39400 1 0 0 ground.sym
N 46200 40700 46200 40800 4
{
T 45800 40900 5 10 0 1 0 0 1
netname=23
}
N 46200 39800 46200 39700 4
N 47200 40700 47200 40800 4
{
T 47000 40800 5 10 0 1 0 0 1
netname=122
}
N 47200 39800 47200 39700 4
N 45400 42000 47500 42000 4
{
T 46400 42000 5 10 0 1 0 0 1
netname=22
}
N 47200 41700 47200 42000 4
N 46200 41700 46200 42000 4
C 48500 40800 1 0 0 jj-2.sym
{
T 48600 41300 5 10 0 0 0 0 1
device=JOSEPHSON_JUNCTION
T 48950 41450 5 10 1 1 0 0 1
refdes=B14
T 48950 41200 5 10 1 1 0 0 1
model-name=jjmit
T 48950 40950 5 10 1 0 0 0 1
area=B14
}
C 48600 40700 1 270 0 inductor-1.sym
{
T 49100 40500 5 10 0 0 270 0 1
device=INDUCTOR
T 48900 40200 5 10 1 1 0 0 1
refdes=LP14
T 49300 40500 5 10 0 0 270 0 1
symversion=0.1
T 48800 40200 5 10 0 1 0 0 1
value=LP14
}
C 49600 40700 1 270 0 inductor-1.sym
{
T 50100 40500 5 10 0 0 270 0 1
device=INDUCTOR
T 49900 40200 5 10 1 1 0 0 1
refdes=LRB14
T 50300 40500 5 10 0 0 270 0 1
symversion=0.1
T 49700 40300 5 10 0 1 0 0 1
value=LRB14
}
C 49600 41700 1 270 0 resistor-1.sym
{
T 50000 41400 5 10 0 0 270 0 1
device=RESISTOR
T 49900 41200 5 10 1 1 0 0 1
refdes=RB14
T 49600 41400 5 10 0 1 0 0 1
value=RB14
}
C 48500 39400 1 0 0 ground.sym
C 49500 39400 1 0 0 ground.sym
N 48700 40700 48700 40800 4
{
T 48300 41000 5 10 0 1 0 0 1
netname=33
}
N 48700 39800 48700 39700 4
N 49700 40700 49700 40800 4
{
T 49500 40900 5 10 0 1 0 0 1
netname=125
}
N 49700 39800 49700 39700 4
N 49700 41700 49700 42000 4
N 48700 41700 48700 42000 4
C 51000 40800 1 0 0 jj-2.sym
{
T 51100 41300 5 10 0 0 0 0 1
device=JOSEPHSON_JUNCTION
T 51450 41450 5 10 1 1 0 0 1
refdes=B15
T 51450 41200 5 10 1 1 0 0 1
model-name=jjmit
T 51450 40950 5 10 1 0 0 0 1
area=B15
}
C 51100 40700 1 270 0 inductor-1.sym
{
T 51600 40500 5 10 0 0 270 0 1
device=INDUCTOR
T 51400 40200 5 10 1 1 0 0 1
refdes=LP15
T 51800 40500 5 10 0 0 270 0 1
symversion=0.1
T 51100 40100 5 10 0 1 0 0 1
value=LP15
}
C 52100 40700 1 270 0 inductor-1.sym
{
T 52600 40500 5 10 0 0 270 0 1
device=INDUCTOR
T 52400 40200 5 10 1 1 0 0 1
refdes=LRB15
T 52800 40500 5 10 0 0 270 0 1
symversion=0.1
T 52300 40300 5 10 0 1 0 0 1
value=LRB15
}
C 52100 41700 1 270 0 resistor-1.sym
{
T 52500 41400 5 10 0 0 270 0 1
device=RESISTOR
T 52400 41200 5 10 1 1 0 0 1
refdes=RB15
T 52300 41400 5 10 0 1 0 0 1
value=RB15
}
C 51000 39400 1 0 0 ground.sym
C 52000 39400 1 0 0 ground.sym
N 51200 40700 51200 40800 4
{
T 51000 40900 5 10 0 1 0 0 1
netname=35
}
N 51200 39800 51200 39700 4
N 52200 40700 52200 40800 4
{
T 52600 40500 5 10 0 1 0 0 1
netname=134
}
N 52200 39800 52200 39700 4
N 52500 42000 50900 42000 4
{
T 51700 42000 5 10 0 1 0 0 1
netname=34
}
N 52200 41700 52200 42000 4
N 51200 41700 51200 42000 4
C 40300 47600 1 0 0 jj-2.sym
{
T 40400 48100 5 10 0 0 0 0 1
device=JOSEPHSON_JUNCTION
T 40750 48250 5 10 1 1 0 0 1
refdes=B11
T 40750 48000 5 10 1 1 0 0 1
model-name=jjmit
T 40750 47750 5 10 1 0 0 0 1
area=B11
}
C 40400 47500 1 270 0 inductor-1.sym
{
T 40900 47300 5 10 0 0 270 0 1
device=INDUCTOR
T 40700 47000 5 10 1 1 0 0 1
refdes=LP11
T 41100 47300 5 10 0 0 270 0 1
symversion=0.1
T 40500 46800 5 10 0 1 0 0 1
value=LP11
}
C 41400 47500 1 270 0 inductor-1.sym
{
T 41900 47300 5 10 0 0 270 0 1
device=INDUCTOR
T 41700 47000 5 10 1 1 0 0 1
refdes=LRB11
T 42100 47300 5 10 0 0 270 0 1
symversion=0.1
T 41600 47000 5 10 0 1 0 0 1
value=LRB11
}
C 41400 48500 1 270 0 resistor-1.sym
{
T 41800 48200 5 10 0 0 270 0 1
device=RESISTOR
T 41700 48000 5 10 1 1 0 0 1
refdes=RB11
T 41400 48300 5 10 0 1 0 0 1
value=RB11
}
C 40300 46200 1 0 0 ground.sym
C 41300 46200 1 0 0 ground.sym
N 40500 47500 40500 47600 4
{
T 39700 48000 5 10 0 1 0 0 1
netname=27
}
N 40500 46600 40500 46500 4
N 41500 47500 41500 47600 4
{
T 41200 47700 5 10 0 1 0 0 1
netname=126
}
N 41500 46600 41500 46500 4
N 41800 48800 40200 48800 4
{
T 41100 48900 5 10 0 1 0 0 1
netname=26
}
N 41500 48500 41500 48800 4
N 40500 48500 40500 48800 4
C 44300 47600 1 0 0 jj-2.sym
{
T 44400 48100 5 10 0 0 0 0 1
device=JOSEPHSON_JUNCTION
T 44750 48250 5 10 1 1 0 0 1
refdes=B12
T 44750 48000 5 10 1 1 0 0 1
model-name=jjmit
T 44750 47750 5 10 1 0 0 0 1
area=B12
}
C 44400 47500 1 270 0 inductor-1.sym
{
T 44900 47300 5 10 0 0 270 0 1
device=INDUCTOR
T 44700 47000 5 10 1 1 0 0 1
refdes=LP12
T 45100 47300 5 10 0 0 270 0 1
symversion=0.1
T 44500 47000 5 10 0 1 0 0 1
value=LP12
}
C 45400 47500 1 270 0 inductor-1.sym
{
T 45900 47300 5 10 0 0 270 0 1
device=INDUCTOR
T 45700 47000 5 10 1 1 0 0 1
refdes=LRB12
T 46100 47300 5 10 0 0 270 0 1
symversion=0.1
T 45600 47100 5 10 0 1 0 0 1
value=LRB12
}
C 45400 48500 1 270 0 resistor-1.sym
{
T 45800 48200 5 10 0 0 270 0 1
device=RESISTOR
T 45700 48000 5 10 1 1 0 0 1
refdes=RB12
T 45500 48200 5 10 0 1 0 0 1
value=RB12
}
C 44300 46200 1 0 0 ground.sym
C 45300 46200 1 0 0 ground.sym
N 44500 47500 44500 47600 4
{
T 44100 47600 5 10 0 1 0 0 1
netname=31
}
N 44500 46600 44500 46500 4
N 45500 47500 45500 47600 4
{
T 45200 47700 5 10 0 1 0 0 1
netname=130
}
N 45500 46600 45500 46500 4
N 45800 48800 44200 48800 4
{
T 44800 48700 5 10 0 1 0 0 1
netname=30
}
N 45500 48500 45500 48800 4
N 44500 48500 44500 48800 4
C 47000 49700 1 0 0 resistor-1.sym
{
T 47300 50100 5 10 0 0 0 0 1
device=RESISTOR
T 47200 50000 5 10 1 1 0 0 1
refdes=RB13
T 47500 49800 5 10 0 1 0 0 1
value=RB13
}
C 48000 49700 1 0 0 inductor-1.sym
{
T 48200 50200 5 10 0 0 0 0 1
device=INDUCTOR
T 48100 50000 5 10 1 1 0 0 1
refdes=LRB13
T 48200 50400 5 10 0 0 0 0 1
symversion=0.1
T 48500 49800 5 10 0 1 0 0 1
value=LRB13
}
N 48000 49800 47900 49800 4
{
T 48100 49500 5 10 0 1 0 0 1
netname=132
}
C 48400 48600 1 90 0 jj-2.sym
{
T 47900 48700 5 10 0 0 90 0 1
device=JOSEPHSON_JUNCTION
T 47750 48350 5 10 1 1 0 0 1
refdes=B13
T 47750 48100 5 10 1 1 0 0 1
model-name=jjmit
T 47750 47850 5 10 1 0 0 0 1
area=B13
}
N 47500 48800 46700 48800 4
{
T 46900 48800 5 10 0 1 0 0 1
netname=32
}
N 47000 49800 47000 48800 4
N 48900 48800 48900 49800 4
N 48400 48800 49200 48800 4
N 49200 48800 49200 42000 4
N 50000 42000 48400 42000 4
{
T 49000 42000 5 10 0 1 0 0 1
netname=25
}
C 53500 41900 1 0 0 resistor-1.sym
{
T 53800 42300 5 10 0 0 0 0 1
device=RESISTOR
T 53800 42200 5 10 1 1 0 0 1
refdes=RD
T 53800 42000 5 10 0 1 0 0 1
value=RD
}
T 30900 44400 9 20 1 0 0 0 1
A
T 30900 39400 9 20 1 0 0 0 1
B
T 38500 48700 9 20 1 0 0 0 1
CLK
T 54500 41900 9 20 1 0 0 0 1
Q
N 41000 44500 40200 44500 4
{
T 43300 43900 5 10 0 1 0 0 1
netname=9
}
N 41900 44500 42200 44500 4
N 42200 39500 41900 39500 4
N 53500 42000 53400 42000 4
{
T 51800 44100 5 10 0 1 0 0 1
netname=37
}
C 52500 41900 1 0 0 inductor-1.sym
{
T 52700 42400 5 10 0 0 0 0 1
device=INDUCTOR
T 52800 42200 5 10 1 1 0 0 1
refdes=L16
T 52700 42600 5 10 0 0 0 0 1
symversion=0.1
T 52900 42100 5 10 0 1 0 0 1
value=L16
}
C 50000 41900 1 0 0 inductor-1.sym
{
T 50200 42400 5 10 0 0 0 0 1
device=INDUCTOR
T 50300 42200 5 10 1 1 0 0 1
refdes=L15
T 50200 42600 5 10 0 0 0 0 1
symversion=0.1
T 50400 42100 5 10 0 1 0 0 1
value=L15
}
C 45800 48700 1 0 0 inductor-1.sym
{
T 46000 49200 5 10 0 0 0 0 1
device=INDUCTOR
T 46100 49000 5 10 1 1 0 0 1
refdes=L14
T 46000 49400 5 10 0 0 0 0 1
symversion=0.1
T 46300 48700 5 10 0 1 0 0 1
value=L14
}
C 43300 48700 1 0 0 inductor-1.sym
{
T 43500 49200 5 10 0 0 0 0 1
device=INDUCTOR
T 43600 49000 5 10 1 1 0 0 1
refdes=L13
T 43500 49400 5 10 0 0 0 0 1
symversion=0.1
T 43800 48900 5 10 0 1 0 0 1
value=L13
}
C 41800 48700 1 0 0 inductor-1.sym
{
T 42000 49200 5 10 0 0 0 0 1
device=INDUCTOR
T 42100 49000 5 10 1 1 0 0 1
refdes=L12
T 42000 49400 5 10 0 0 0 0 1
symversion=0.1
T 42300 49000 5 10 0 1 0 0 1
value=L12
}
C 39300 48700 1 0 0 inductor-1.sym
{
T 39500 49200 5 10 0 0 0 0 1
device=INDUCTOR
T 39600 49000 5 10 1 1 0 0 1
refdes=L11
T 39500 49400 5 10 0 0 0 0 1
symversion=0.1
T 39800 48800 5 10 0 1 0 0 1
value=L11
}
C 47500 41900 1 0 0 inductor-1.sym
{
T 47700 42400 5 10 0 0 0 0 1
device=INDUCTOR
T 47800 42200 5 10 1 1 0 0 1
refdes=L10
T 47700 42600 5 10 0 0 0 0 1
symversion=0.1
T 48000 42000 5 10 0 1 0 0 1
value=L10
}
C 42800 41900 1 0 0 inductor-1.sym
{
T 43000 42400 5 10 0 0 0 0 1
device=INDUCTOR
T 43100 42200 5 10 1 1 0 0 1
refdes=L9
T 43000 42600 5 10 0 0 0 0 1
symversion=0.1
T 43300 42000 5 10 0 1 0 0 1
value=L9
}
C 41000 39400 1 0 0 inductor-1.sym
{
T 41200 39900 5 10 0 0 0 0 1
device=INDUCTOR
T 41300 39700 5 10 1 1 0 0 1
refdes=L8
T 41200 40100 5 10 0 0 0 0 1
symversion=0.1
T 41700 39500 5 10 0 1 0 0 1
value=L8
}
C 36300 39400 1 0 0 inductor-1.sym
{
T 36500 39900 5 10 0 0 0 0 1
device=INDUCTOR
T 36600 39700 5 10 1 1 0 0 1
refdes=L7
T 36500 40100 5 10 0 0 0 0 1
symversion=0.1
T 36800 39500 5 10 0 1 0 0 1
value=L7
}
C 33800 39400 1 0 0 inductor-1.sym
{
T 34000 39900 5 10 0 0 0 0 1
device=INDUCTOR
T 34100 39700 5 10 1 1 0 0 1
refdes=L6
T 34000 40100 5 10 0 0 0 0 1
symversion=0.1
T 34200 39600 5 10 0 1 0 0 1
value=L6
}
C 31300 39400 1 0 0 inductor-1.sym
{
T 31500 39900 5 10 0 0 0 0 1
device=INDUCTOR
T 31600 39700 5 10 1 1 0 0 1
refdes=L5
T 31500 40100 5 10 0 0 0 0 1
symversion=0.1
T 31900 39500 5 10 0 1 0 0 1
value=L5
}
C 41000 44400 1 0 0 inductor-1.sym
{
T 41200 44900 5 10 0 0 0 0 1
device=INDUCTOR
T 41300 44700 5 10 1 1 0 0 1
refdes=L4
T 41200 45100 5 10 0 0 0 0 1
symversion=0.1
T 41500 44400 5 10 0 1 0 0 1
value=L4
}
C 36300 44400 1 0 0 inductor-1.sym
{
T 36500 44900 5 10 0 0 0 0 1
device=INDUCTOR
T 36600 44700 5 10 1 1 0 0 1
refdes=L3
T 36500 45100 5 10 0 0 0 0 1
symversion=0.1
T 36800 44500 5 10 0 1 0 0 1
value=L3
}
C 33800 44400 1 0 0 inductor-1.sym
{
T 34000 44900 5 10 0 0 0 0 1
device=INDUCTOR
T 34100 44700 5 10 1 1 0 0 1
refdes=L2
T 34000 45100 5 10 0 0 0 0 1
symversion=0.1
T 34200 44500 5 10 0 1 0 0 1
value=L2
}
N 33000 44800 33000 44500 4
C 35700 47000 1 180 0 ground.sym
N 35500 45700 35500 45800 4
{
T 52700 41000 5 10 0 1 0 0 1
netname=6
}
N 35500 44800 35500 44500 4
C 32900 40700 1 270 0 inductor-1.sym
{
T 33400 40500 5 10 0 0 270 0 1
device=INDUCTOR
T 33200 40200 5 10 1 1 0 0 1
refdes=LB3
T 33600 40500 5 10 0 0 270 0 1
symversion=0.1
T 33000 40200 5 10 0 1 0 0 1
value=LB3
}
C 32800 41700 1 270 0 current-1.sym
{
T 33800 41100 5 10 0 0 270 0 1
device=CURRENT_SOURCE
T 33300 41200 5 10 1 1 0 0 1
refdes=IB3
T 33300 41000 5 10 1 1 0 0 1
value=pwl(0 0 5p IB3)
}
C 33200 42100 1 180 0 ground.sym
N 33000 40800 33000 40700 4
{
T 32700 40900 5 10 0 1 0 0 1
netname=13
}
N 33000 41700 33000 41800 4
N 33000 39800 33000 39500 4
C 35400 40700 1 270 0 inductor-1.sym
{
T 35900 40500 5 10 0 0 270 0 1
device=INDUCTOR
T 35700 40200 5 10 1 1 0 0 1
refdes=LB4
T 36100 40500 5 10 0 0 270 0 1
symversion=0.1
T 35500 40400 5 10 0 1 0 0 1
value=LB4
}
C 35300 41700 1 270 0 current-1.sym
{
T 36300 41100 5 10 0 0 270 0 1
device=CURRENT_SOURCE
T 35800 41200 5 10 1 1 0 0 1
refdes=IB4
T 35800 41000 5 10 1 1 0 0 1
value=pwl(0 0 5p IB4)
}
C 35700 42100 1 180 0 ground.sym
N 35500 40800 35500 40700 4
{
T 35200 41000 5 10 0 1 0 0 1
netname=16
}
N 35500 41700 35500 41800 4
N 35500 39800 35500 39500 4
C 42400 43200 1 270 0 inductor-1.sym
{
T 42900 43000 5 10 0 0 270 0 1
device=INDUCTOR
T 42700 42700 5 10 1 1 0 0 1
refdes=LB5
T 43100 43000 5 10 0 0 270 0 1
symversion=0.1
T 42500 42800 5 10 0 1 0 0 1
value=LB5
}
C 42300 44200 1 270 0 current-1.sym
{
T 43300 43600 5 10 0 0 270 0 1
device=CURRENT_SOURCE
T 42800 43700 5 10 1 1 0 0 1
refdes=IB5
T 42800 43500 5 10 1 1 0 0 1
value=pwl(0 0 5p IB5)
}
C 42700 44600 1 180 0 ground.sym
N 42500 43300 42500 43200 4
{
T 42100 43400 5 10 0 1 0 0 1
netname=20
}
N 42500 44200 42500 44300 4
N 42500 42300 42500 42000 4
N 42200 42000 42800 42000 4
C 42900 50000 1 270 0 inductor-1.sym
{
T 43400 49800 5 10 0 0 270 0 1
device=INDUCTOR
T 43200 49500 5 10 1 1 0 0 1
refdes=LB7
T 43600 49800 5 10 0 0 270 0 1
symversion=0.1
T 43100 49600 5 10 0 1 0 0 1
value=LB7
}
C 42800 51000 1 270 0 current-1.sym
{
T 43800 50400 5 10 0 0 270 0 1
device=CURRENT_SOURCE
T 43300 50500 5 10 1 1 0 0 1
refdes=IB7
T 43300 50300 5 10 1 1 0 0 1
value=pwl(0 0 5p IB7)
}
C 43200 51400 1 180 0 ground.sym
N 43000 50100 43000 50000 4
{
T 42500 50300 5 10 0 1 0 0 1
netname=29
}
N 43000 51000 43000 51100 4
N 43000 49100 43000 48800 4
N 42700 48800 43300 48800 4
{
T 58400 41500 5 10 0 1 0 0 1
netname=28
}
C 46600 43200 1 270 0 inductor-1.sym
{
T 47100 43000 5 10 0 0 270 0 1
device=INDUCTOR
T 46900 42700 5 10 1 1 0 0 1
refdes=LB6
T 47300 43000 5 10 0 0 270 0 1
symversion=0.1
T 46800 42800 5 10 0 1 0 0 1
value=LB6
}
C 46500 44200 1 270 0 current-1.sym
{
T 47500 43600 5 10 0 0 270 0 1
device=CURRENT_SOURCE
T 47000 43700 5 10 1 1 0 0 1
refdes=IB6
T 47000 43500 5 10 1 1 0 0 1
value=pwl(0 0 5p IB6)
}
C 46900 44600 1 180 0 ground.sym
N 46700 43300 46700 43200 4
{
T 46200 43500 5 10 0 1 0 0 1
netname=24
}
N 46700 44200 46700 44300 4
N 46700 42300 46700 42000 4
C 51600 43200 1 270 0 inductor-1.sym
{
T 52100 43000 5 10 0 0 270 0 1
device=INDUCTOR
T 51900 42700 5 10 1 1 0 0 1
refdes=LB8
T 52300 43000 5 10 0 0 270 0 1
symversion=0.1
T 51800 42800 5 10 0 1 0 0 1
value=LB8
}
C 51500 44200 1 270 0 current-1.sym
{
T 52500 43600 5 10 0 0 270 0 1
device=CURRENT_SOURCE
T 52000 43700 5 10 1 1 0 0 1
refdes=IB8
T 52000 43500 5 10 1 1 0 0 1
value=pwl(0 0 5p IB8)
}
C 51900 44600 1 180 0 ground.sym
N 51700 43300 51700 43200 4
{
T 51200 43500 5 10 0 1 0 0 1
netname=36
}
N 51700 44200 51700 44300 4
N 51700 42300 51700 42000 4