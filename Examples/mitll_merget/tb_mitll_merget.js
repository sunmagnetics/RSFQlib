* JSIM deck file generated with TimEx
* === DEVICE-UNDER-TEST ===
*****************************************
* Begin .SUBCKT model                   *
* spice-sdb ver 4.28.2007               *
*                                       *
* RSFQ generic cell for MITLL sfq5ee    *
* Project under IARPA-BAA-16-03         *
* Authored 3 Nov 2015, CJ Fourie, SU    *
* Last mod 23 Mar 2018, L Schindler, SU  *
* (Added PTL drivers & Receivers and   *
*   reduced JJ count)          *
******************************************
*                   IN_A  in_B  OUT
*$Ports             in_A  in_B  out_out
.SUBCKT mitll_merget 24 29 34 
*==============  Begin SPICE netlist of main design ============
B01urx1    23         25         jmitll     area=0.406096932932737
B01urx2    28         30         jmitll     area=0.406096932932737
B01utx1    12         35         jmitll     area=1.6170270947092646
B1         1          2          jmitll     area=1.3297290261410297
B2         1          5          jmitll     area=0.9441504843661195
B3         3          4          jmitll     area=1.3297290261410297
B4         3          6          jmitll     area=0.9441504843661195
B5         7          8          jmitll     area=0.4699573551784042
IB01_rx1   0          26         pwl(0      0 5p 5.78131352e-05)
IB01_rx2   0          31         pwl(0      0 5p 5.78131352e-05)
IB01_tx1   0          37         pwl(0      0 5p 9.86576163e-05)
IB1        0          10         pwl(0      0 5p 2.13019346e-04)
L01urx1    24         23         1.02289510e-13
L01urx2    29         28         1.02289510e-13
L02urx1    23         9          3.65207718e-13
L02urx2    28         11         3.65207718e-13
L02utx1    12         33         7.96831232e-13
L1         9          1          1.98449952e-12  
L2         5          10         4.25096018e-13 
L3         11         3          1.98449952e-12
L4         6          10         4.25096018e-13    
L6         10         7          3.24979008e-12  
L7         7          12         3.11367602e-12
LP01urx1   0          25         3.4e-013
LP01urx2   0          30         3.4e-013
LP01utx1   0          35         5e-014
Lp1        2          0          2e-013    
Lp3        4          0          2e-013    
Lp5        8          0          2e-013    
LPR01urx1  9          26         2e-013
LPR01urx2  11         31         2e-013
LPR01utx1  12         37         2e-013
LRB01urx1  0          27         5e-013
LRB01urx2  0          32         5e-013
LRB01utx1  0          36         1e-012
LRB1       14         0          1e-012   
LRB2       16         5          1e-012   
LRB3       13         0          1e-012   
LRB4       17         6          1e-012   
LRB5       15         0          1e-012   
RB01_rx1   27         23         16.8923
RB01_rx2   32         28         16.8923
RB01_tx1   36         12         4.24229
RB1        1          14         5.15887    
RB2        1          16         7.26569     
RB3        3          13         5.15887    
RB4        3          17         7.26569      
RB5        7          15         14.5969      
RINS_tx1   33         34         1.36       
.model jmitll jj(rtype=1, vg=2.8mV, cap=0.07pF, r0=160, rn=16, icrit=0.1mA)
.ends mitll_merget
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
I_a 0 1 pwl(0 0 5p 0 1.25E-11 0 1.35E-11 0.001 1.45E-11 0)
XSOURCEINa SOURCECELL 1 2
XLOADINa LOADINCELL 2 3
I_b 0 4 pwl(0 0 5p 0 2.25E-11 0 2.35E-11 0.001 2.45E-11 0)
XSOURCEINb SOURCECELL 4 5
XLOADINb LOADINCELL 5 6
XLOADOUTout LOADOUTCELL 7 8
XSINKOUTout SINKCELL 8
XDUT mitll_merget 3 6 7
.tran 2.5E-13 4E-11 0 2.5E-13
.PRINT NODEV 3 0
.PRINT NODEV 6 0
.PRINT NODEV 7 0
.PRINT DEVI XDUT_LP1
.PRINT DEVI XDUT_B1
.PRINT DEVI XDUT_B2
.PRINT DEVI XDUT_L2
.PRINT DEVI XDUT_L4
.PRINT DEVI XDUT_B4
.PRINT DEVI XDUT_L3
.PRINT DEVI XDUT_L02URX2
.PRINT DEVI XDUT_B01URX2
.PRINT DEVI XDUT_LP01URX2
.PRINT DEVI XDUT_B3
.PRINT DEVI XDUT_LP3
.PRINT DEVI XDUT_L6
.PRINT DEVI XDUT_L7
.PRINT DEVI XDUT_B01UTX1
.PRINT DEVI XDUT_LP01UTX1
.PRINT DEVI XDUT_B5
.PRINT DEVI XDUT_LP5
.PRINT DEVI XDUT_L1
.PRINT DEVI XDUT_L02URX1
.PRINT DEVI XDUT_B01URX1
.PRINT DEVI XDUT_LP01URX1
.end
