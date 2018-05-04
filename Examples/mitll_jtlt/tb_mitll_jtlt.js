* JSIM deck file generated with TimEx
* === DEVICE-UNDER-TEST ===
******************************************
* Begin .SUBCKT model                    *
* spice-sdb ver 4.28.2007                *
*                                        *
* RSFQ generic cell for MITLL sfq5ee     *
* Project under IARPA-BAA-16-03          *
* Authored 2 Nov 2015, CJ Fourie, SU     *
* Modified 23 Aug 2016, CJ Fourie, SU    *
* Last mod 23 Mar 2018, L Schindler, SU  *
* (Added PTL drivers & Receivers and   *
*   reduced JJ count)          *
******************************************
*     in  out
*$Ports             in_in  out_out
.SUBCKT mitll_jtlt 2 13 
*==============  Begin SPICE netlist of main design ============
B01rx1     1          6          jmitll     area=0.6978965094340693
B01tx1     10         14         jmitll     area=1.7851040521840216
B02rx1     4          5          jmitll     area=0.4431557447885417
B1         17         21         jmitll     area=0.48805176033496367
B2         11         22         jmitll     area=0.48805176033496367
IB01rx1    0          7          pwl(0      0 5p 8.645054846430082e-05)
IB01tx1    0          16         pwl(0      0 5p 5.531224327588262e-05)
IB1        0          23         pwl(0      0 5p 0.00012008182492244687)
L01rx1     2          1          3.3251593177777415e-13    
L01tx1     11         10         2.3256259129695253e-12    
L02rx1     1          3          2.4032152114216404e-12    
L03rx1     3          4          1.6772485370088992e-12  
L03tx1     10         12         2.3630198619224862e-12     
L1         4          17         2.5109096596962294e-12       
L2         17         18         8.665208165957606e-13       
L3         18         11         8.665208165957606e-13       
LB1        19         0          1p        
LB2        20         0          1p        
LP01       18         23         0.2p      
LP01rx1    0          6          0.34p     
LP01tx1    0          14         0.05p     
LP02rx1    0          5          0.06p     
Lp1        21         0          0.2p      
Lp2        22         0          0.2p      
LPR01rx1   3          7          0.2p      
LPR01tx1   10         16         0.2p      
LRB01rx1   0          8          0.5p      
LRB01tx1   0          15         1p        
LRB02rx1   0          9          1p        
RB01rx1    8          1          9.8294       
RB01tx1    15         10         3.84286     
RB02rx1    9          4          15.4797       
RB1        17         19         14.0557        
RB2        11         20         14.0557        
RINStx1    12         13         1.36      
.model jmitll jj(rtype=1, vg=2.8mV, cap=0.07pF, r0=160, rn=16, icrit=0.1mA)
.ends mitll_jtlt
*******************************
* === SOURCE DEFINITION ===
.SUBCKT SOURCECELL  8 22
b1    1  2  jjmitll100 area=2.25
b2    3  4  jjmitll100 area=2.25
b3    5  6  jjmitll100 area=2.5
ib1   0  2  pwl(0 0 5p 275ua)
ib2   0  5  pwl(0 0 5p 175ua)
l1    8  7  1p
l2    7  0  3.9p
l3    7  1  0.6p
l4    2  3  1.1p
l5    3  5  4.5p
l6    5  11 2p
lp2   4  0  0.2p
lp3   6  0  0.2p
lrb1  9  2  1p
lrb2  10 4  1p
lrb3  12 6  1p
rb1   1  9  4.31
rb2   3  10 4.31
rb3   5  12 3.88
b01   23 27 jmitll100 area=2
b02   24 26 jmitll100 area=1.62
ib01  0  30 pwl(0      0 5p 0.00023)
ib02  0  31 pwl(0      0 5p 8.2e-005)
l01   11 23 2.5e-012
l02   23 24 3.3e-012
l03   24 25 3.5e-013
lp01  0  27 5e-014
lp02  0  26 1.2e-013
lpr01 23 30 2e-013
lpr02 24 31 1.3e-012
lrb01 27 28 1e-012
lrb02 26 29 1e-012
rb01  28 23 4.85
rb02  29 24 6.3
rins  25 22 1.36
.model jjmitll100 jj(rtype=1, vg=2.8mv, cap=0.07pf, r0=160, rn=16, icrit=0.1ma)
.ENDS SOURCECELL
* === INPUT LOAD DEFINITION ===
.SUBCKT LOADINCELL  2 5
tload 2 0 5 0 lossless z0=5 td=10p
.ENDS LOADINCELL
* === OUTPUT LOAD DEFINITION ===
.SUBCKT LOADOUTCELL  2 5
tload 2 0 5 0 lossless z0=5 td=50p
.ENDS LOADOUTCELL
* === SINK DEFINITION ===
.SUBCKT SINKCELL  2
b1    1  9  jmitll100     area=1
b2    4  8  jmitll100     area=1
b3    5  7  jmitll100     area=1
ib1   0  10 pwl(0      0 5p 145u)
l1    2  1  0.2p
l2    1  3  4.3p
l3    3  4  4.6p
l4    4  5  6.0p
l5    5  6  1.3p
lp1   0  9  0.34p
lp2   0  8  0.06p
lp3   0  7  0.03p
lpr1  3  10 0.2p
lrb1  9  11 0.5p
lrb2  8  12 1p
lrb3  7  13 1p
rb1   11 1  15.4
rb2   12 4  11.3
rb3   13 5  11.3
rsink 6  0  2
.model jmitll100 jj(rtype=1, vg=2.8mv, cap=0.07pf, r0=160ohm, rn=16ohm, icrit=0.1ma)
.ENDS SINKCELL
* ===== MAIN =====
I_in 0 1 pwl(0 0 5p 0 1.25E-11 0 1.35E-11 0.001 1.45E-11 0)
XSOURCEINin SOURCECELL 1 2
XLOADINin LOADINCELL 2 3
XLOADOUTout LOADOUTCELL 4 5
XSINKOUTout SINKCELL 5
XDUT mitll_jtlt 3 4
.tran 2.5E-13 3E-11 0 2.5E-13
.PRINT NODEV 3 0
.PRINT NODEV 4 0
.PRINT DEVI XDUT_LP01TX1
.PRINT DEVI XDUT_B01TX1
.PRINT DEVI XDUT_L01TX1
.PRINT DEVI XDUT_L3
.PRINT DEVI XDUT_L2
.PRINT DEVI XDUT_B1
.PRINT DEVI XDUT_LP1
.PRINT DEVI XDUT_L1
.PRINT DEVI XDUT_L03RX1
.PRINT DEVI XDUT_L02RX1
.PRINT DEVI XDUT_B01RX1
.PRINT DEVI XDUT_LP01RX1
.PRINT DEVI XDUT_B02RX1
.PRINT DEVI XDUT_LP02RX1
.PRINT DEVI XDUT_B2
.PRINT DEVI XDUT_LP2
.end
