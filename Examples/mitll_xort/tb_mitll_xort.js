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
.SUBCKT mitll_xort 16 59 7 26 
*==============  Begin SPICE netlist of main design ============
B01        43         44         jmitll     area=2.79835
B01urx1    6          11         jmitll     area=0.723632
B01urx2    58         63         jmitll     area=1.21244
B01urx3    15         20         jmitll     area=1.21244
B02urx1    9          10         jmitll     area=0.772041
B02urx2    61         62         jmitll     area=1.15856
B02urx3    18         19         jmitll     area=1.15856
B02utx1    25         27         jmitll     area=1.36946
B03        43         72         jmitll     area=1.91585
B03urx1    34         74         jmitll     area=0.827992
B03urx2    52         78         jmitll     area=0.89775
B03urx3    53         76         jmitll     area=0.89775
B04        41         42         jmitll     area=2.79835
B06        41         70         jmitll     area=1.91585
B07        37         36         jmitll     area=1.48566
B08        38         39         jmitll     area=0.933603
B09        33         40         jmitll     area=1.28591
B10        33         45         jmitll     area=1.6863
IB01       0          51         pwl(0      0 5p 8.9218e-005)
IB01_rx1   0          12         pwl(0      0 5p 0.000131858)
IB01_rx2   0          64         pwl(0      0 5p 0.000229789)
IB01_rx3   0          21         pwl(0      0 5p 0.000229789)
IB02       0          54         pwl(0      0 5p 8.9218e-005)
IB02_tx1   0          29         pwl(0      0 5p 6.64568e-005)
IB04       0          73         pwl(0      0 5p 0.000124046)
IB05       0          50         pwl(0      0 5p 0.000177629)
L01urx1    7          6          1.89277e-012
L01urx2    59         58         1.86037e-012
L01urx3    16         15         1.86037e-012
L02urx1    6          8          2.23806e-012
L02urx2    58         60         2.15285e-012
L02urx3    15         17         2.15285e-012
L03        72         71         2.27926e-012    
L03urx1    8          9          2.02047e-012
L03urx2    60         61         1.97288e-012
L03urx3    17         18         1.97288e-012
L03utx1    25         24         2.22608e-012
L04urx1    9          34         2.01777e-012
L04urx2    61         52         2.3966e-012
L04urx3    18         53         2.3966e-012
L06        70         71         2.27926e-012    
L08        71         36         1.75154e-012    
L09        37         38         1.26199e-012    
L10        38         40         2.22462e-012    
L11        34         33         1.80333e-012    
L12        38         25         1.8658e-012    
L14        52         43         1.6354e-012    
L15        53         41         1.6354e-012    
LP01       0          44         2e-013   
LP01urx1   0          11         2e-013
LP01urx2   0          63         2e-013
LP01urx3   0          20         2e-013
LP02urx1   0          10         2e-013
LP02urx2   0          62         2e-013
LP02urx3   0          19         2e-013
LP02utx1   0          27         2e-013
LP03       0          42         2e-013   
LP03urx1   0          74         2e-013
LP03urx2   0          78         2e-013
LP03urx3   0          76         2e-013
LP05       0          39         2e-013   
LP06       0          45         2e-013   
LPR01      43         51         2e-013  
LPR01urx1  8          12         2e-013
LPR01urx2  60         64         2e-013
LPR01urx3  17         21         2e-013
LPR02      41         54         2e-013  
LPR02utx1  25         29         2e-013
LPR04      73         71         2e-013  
LPR05      33         50         2e-013  
LRB01      0          47         1e-012  
LRB01urx1  0          13         1e-012
LRB01urx2  0          65         1e-012
LRB01urx3  0          22         1e-012
LRB02urx1  0          14         1e-012
LRB02urx2  0          66         1e-012
LRB02urx3  0          23         1e-012
LRB02utx1  0          28         1e-012
LRB03      68         72         1e-012  
LRB03urx1  0          75         1e-012
LRB03urx2  0          79         1e-012
LRB03urx3  0          77         1e-012
LRB04      0          48         1e-012  
LRB06      69         70         1e-012  
LRB07      35         37         1e-012  
LRB08      0          49         1e-012  
LRB09      55         33         1e-012  
LRB10      0          46         1e-012  
RB01       47         43         2.45141   
RB01_rx1   13         6          9.47982
RB01_rx2   65         58         5.65794
RB01_rx3   22         15         5.65794
RB02_rx1   14         9          8.88542
RB02_rx2   66         61         5.92104
RB02_rx3   23         18         5.92104
RB02_tx1   28         25         5.0092
RB03       68         43         3.58061   
RB03_rx1   75         34         8.28498
RB03_rx2   79         52         7.64122
RB03_rx3   77         53         7.64122
RB04       48         41         2.45141   
RB06       69         41         3.58061   
RB07       36         35         4.61741   
RB08       49         38         7.34778   
RB09       40         55         5.33469   
RB10       46         33         4.06803   
RINS_tx1   24         26         1.36      
.model jmitll jj(rtype=1, vg=2.8mV, cap=0.07pF, r0=160, rn=16, icrit=0.1mA)
.ends mitll_xort
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
I_a 0 1 pwl(0 0 5p 0 1.25E-11 0 1.35E-11 0.001 1.45E-11 0 2.25E-11 0 2.35E-11 0.001 2.45E-11 0 5.25E-11 0 5.35E-11 0.001 5.45E-11 0)
XSOURCEINa SOURCECELL 1 2
XLOADINa LOADINCELL 2 3
I_b 0 4 pwl(0 0 5p 0 3.25E-11 0 3.35E-11 0.001 3.45E-11 0 4.25E-11 0 4.35E-11 0.001 4.45E-11 0)
XSOURCEINb SOURCECELL 4 5
XLOADINb LOADINCELL 5 6
I_clk 0 7 pwl(0 0 5p 0 6.25E-11 0 6.35E-11 0.001 6.45E-11 0)
XSOURCEINclk SOURCECELL 7 8
XLOADINclk LOADINCELL 8 9
XLOADOUTout LOADOUTCELL 10 11
XSINKOUTout SINKCELL 11
XDUT mitll_xort 3 6 9 10
.tran 2.5E-13 8E-11 0 2.5E-13
.PRINT NODEV 3 0
.PRINT NODEV 6 0
.PRINT NODEV 9 0
.PRINT NODEV 10 0
.PRINT DEVI XDUT_LP02URX1
.PRINT DEVI XDUT_B02URX1
.PRINT DEVI XDUT_L04URX1
.PRINT DEVI XDUT_L11
.PRINT DEVI XDUT_B09
.PRINT DEVI XDUT_L10
.PRINT DEVI XDUT_L12
.PRINT DEVI XDUT_B02UTX1
.PRINT DEVI XDUT_LP02UTX1
.PRINT DEVI XDUT_L09
.PRINT DEVI XDUT_B07
.PRINT DEVI XDUT_L08
.PRINT DEVI XDUT_L06
.PRINT DEVI XDUT_B06
.PRINT DEVI XDUT_B04
.PRINT DEVI XDUT_LP03
.PRINT DEVI XDUT_L15
.PRINT DEVI XDUT_B03URX3
.PRINT DEVI XDUT_LP03URX3
.PRINT DEVI XDUT_L04URX3
.PRINT DEVI XDUT_L03URX3
.PRINT DEVI XDUT_L02URX3
.PRINT DEVI XDUT_B01URX3
.PRINT DEVI XDUT_LP01URX3
.PRINT DEVI XDUT_B02URX3
.PRINT DEVI XDUT_LP02URX3
.PRINT DEVI XDUT_L03
.PRINT DEVI XDUT_B03
.PRINT DEVI XDUT_B01
.PRINT DEVI XDUT_LP01
.PRINT DEVI XDUT_L14
.PRINT DEVI XDUT_L04URX2
.PRINT DEVI XDUT_L03URX2
.PRINT DEVI XDUT_L02URX2
.PRINT DEVI XDUT_B01URX2
.PRINT DEVI XDUT_LP01URX2
.PRINT DEVI XDUT_B02URX2
.PRINT DEVI XDUT_LP02URX2
.PRINT DEVI XDUT_B03URX2
.PRINT DEVI XDUT_LP03URX2
.PRINT DEVI XDUT_B08
.PRINT DEVI XDUT_LP05
.PRINT DEVI XDUT_B10
.PRINT DEVI XDUT_LP06
.PRINT DEVI XDUT_B03URX1
.PRINT DEVI XDUT_LP03URX1
.PRINT DEVI XDUT_L03URX1
.PRINT DEVI XDUT_L02URX1
.PRINT DEVI XDUT_B01URX1
.PRINT DEVI XDUT_LP01URX1
.end
