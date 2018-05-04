* JSIM deck file generated with TimEx
* === DEVICE-UNDER-TEST ===
*****************************************
* Begin .SUBCKT model                    *
* spice-sdb ver 4.28.2007                *
*                                        *
* RSFQ generic cell for MITLL sfq5ee     *
* Project under IARPA-BAA-16-03          *
* Authored 1 March 2016, JA Delport, SU  *
* Modified 11 Oct 2016, CJ Fourie, SU    *
*   (Added B10, optimized)               *
* Last mod 23 Mar 2018, L Schindler, SU  *
* (Added PTL drivers & Receivers and   *
*   reduced JJ count)          *
******************************************
*                 IN_A   IN_B   CLK   OUT
*$Ports             in_A  in_B  in_clk  out_out
.SUBCKT mitll_or2t 62 54 5 16 
*==============  Begin SPICE netlist of main design ============
B01        30         31         jmitll     area=1.43648
B01urx1    4          9          jmitll     area=0.498239
B01urx2    53         55         jmitll     area=0.761009
B01urx3    61         63         jmitll     area=0.761009
B01utx1    13         17         jmitll     area=1.4217
B02        30         34         jmitll     area=1.02669
B02urx1    7          67         jmitll     area=0.709348
B03        32         33         jmitll     area=1.43648
B03urx1    7          8          jmitll     area=0.624715
B04        32         35         jmitll     area=1.02669
B05        36         37         jmitll     area=1.07602
B08        22         23         jmitll     area=1.00901
B09        14         26         jmitll     area=1.78161
B10        48         36         jmitll     area=1.85929
IB01       0          47         pwl(0      0 5p 0.000258575)
IB01_rx1   0          10         pwl(0      0 5p 6.19356e-005)
IB01_rx2   0          56         pwl(0      0 5p 9.93419e-005)
IB01_rx3   0          64         pwl(0      0 5p 9.93419e-005)
IB01_tx1   0          19         pwl(0      0 5p 0.000124071)
IB02       0          29         pwl(0      0 5p 4.45911e-005)
IB04       0          50         pwl(0      0 5p 7.34836e-005)
L01        38         30         1.19917e-012    
L01urx1    5          4          1.31862e-012
L01urx2    54         53         1.0157e-012
L01urx3    62         61         1.0157e-012
L01utx1    14         13         3.33856e-012
L02        34         39         1.12533e-012    
L02urx1    4          6          2.19746e-012
L02urx2    53         40         1.66138e-012
L02urx3    61         38         1.66138e-012
L02utx1    13         15         2.41485e-012
L03        40         32         1.19917e-012    
L03urx1    6          7          2.41399e-012
L04        35         39         1.12533e-012    
L05        39         41         6e-013    
L06        41         48         2.39701e-012    
L07        36         28         4e-013    
L08        28         8          4.37488e-012    
L09        8          22         1.60915e-012    
L13        22         25         1.86893e-012    
L14        25         14         8.12022e-013    
LP01       31         0          2e-013   
LP01urx1   0          9          3.4e-013
LP01urx2   0          55         3.4e-013
LP01urx3   0          63         3.4e-013
LP01utx1   0          17         5e-014
LP02urx1   0          67         3.4e-013
LP03       33         0          2e-013   
LP05       37         0          2e-013   
LP08       0          23         1.17e-013   
LP09       0          26         1.51e-013   
LPuIB01    41         47         2e-013
LPuIB02    28         29         2e-013
LPuIB04    25         50         2e-013
LPR01urx1  6          10         2e-013
LPR01urx2  40         56         2e-013
LPR01urx3  38         64         2e-013
LPR01utx1  13         19         2e-013
LRB01      43         0          1e-012  
LRB01urx1  0          11         5e-013
LRB01urx2  0          57         5e-013
LRB01urx3  0          65         5e-013
LRB01utx1  0          18         1e-012
LRB02      45         34         1e-012  
LRB02urx1  0          68         5e-013
LRB03      42         0          1e-012  
LRB03urx1  8          12         1e-012
LRB04      46         35         1e-012  
LRB05      44         0          1e-012  
LRB08      24         0          1e-012  
LRB09      27         0          1e-012  
LRB10      49         36         1e-012  
RB01       30         43         4.7755   
RB01_rx1   11         4          13.7683
RB01_rx2   57         53         9.01423
RB01_rx3   65         61         9.01423
RB01_tx1   18         13         4.82513
RB02       30         45         6.68158   
RB02_rx1   68         7          9.67072
RB03       32         42         4.7755   
RB03_rx1   12         7          10.9809
RB04       32         46         6.68158   
RB05       36         44         6.37527   
RB08       24         22         6.79868   
RB09       27         14         3.8504   
RB10       48         49         3.68953   
RINS_tx1   15         16         1.36      
.model jmitll jj(rtype=1, vg=2.8mV, cap=0.07pF, r0=160, rn=16, icrit=0.1mA)
.ends mitll_or2t
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
I_a 0 1 pwl(0 0 5p 0 1.25E-11 0 1.35E-11 0.001 1.45E-11 0 2.25E-11 0 2.35E-11 0.001 2.45E-11 0)
XSOURCEINa SOURCECELL 1 2
XLOADINa LOADINCELL 2 3
I_b 0 4 pwl(0 0 5p 0 3.25E-11 0 3.35E-11 0.001 3.45E-11 0 5.25E-11 0 5.35E-11 0.001 5.45E-11 0)
XSOURCEINb SOURCECELL 4 5
XLOADINb LOADINCELL 5 6
I_clk 0 7 pwl(0 0 5p 0 4.25E-11 0 4.35E-11 0.001 4.45E-11 0)
XSOURCEINclk SOURCECELL 7 8
XLOADINclk LOADINCELL 8 9
XLOADOUTout LOADOUTCELL 10 11
XSINKOUTout SINKCELL 11
XDUT mitll_or2t 3 6 9 10
.tran 2.5E-13 7E-11 0 2.5E-13
.PRINT NODEV 3 0
.PRINT NODEV 6 0
.PRINT NODEV 9 0
.PRINT NODEV 10 0
.PRINT DEVI XDUT_LP01UTX1
.PRINT DEVI XDUT_B01UTX1
.PRINT DEVI XDUT_L01UTX1
.PRINT DEVI XDUT_L14
.PRINT DEVI XDUT_L13
.PRINT DEVI XDUT_L09
.PRINT DEVI XDUT_L08
.PRINT DEVI XDUT_L07
.PRINT DEVI XDUT_B05
.PRINT DEVI XDUT_LP05
.PRINT DEVI XDUT_B10
.PRINT DEVI XDUT_L06
.PRINT DEVI XDUT_L05
.PRINT DEVI XDUT_L02
.PRINT DEVI XDUT_B02
.PRINT DEVI XDUT_L01
.PRINT DEVI XDUT_L02URX3
.PRINT DEVI XDUT_B01URX3
.PRINT DEVI XDUT_LP01URX3
.PRINT DEVI XDUT_B01
.PRINT DEVI XDUT_LP01
.PRINT DEVI XDUT_L04
.PRINT DEVI XDUT_B04
.PRINT DEVI XDUT_L03
.PRINT DEVI XDUT_L02URX2
.PRINT DEVI XDUT_B01URX2
.PRINT DEVI XDUT_LP01URX2
.PRINT DEVI XDUT_B03
.PRINT DEVI XDUT_LP03
.PRINT DEVI XDUT_B03URX1
.PRINT DEVI XDUT_L03URX1
.PRINT DEVI XDUT_L02URX1
.PRINT DEVI XDUT_B01URX1
.PRINT DEVI XDUT_LP01URX1
.PRINT DEVI XDUT_B02URX1
.PRINT DEVI XDUT_LP02URX1
.PRINT DEVI XDUT_B08
.PRINT DEVI XDUT_LP08
.PRINT DEVI XDUT_B09
.PRINT DEVI XDUT_LP09
.end
