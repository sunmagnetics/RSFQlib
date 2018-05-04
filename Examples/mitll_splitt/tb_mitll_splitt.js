* JSIM deck file generated with TimEx
* === DEVICE-UNDER-TEST ===
******************************************
* Begin .SUBCKT model                    *
* spice-sdb ver 4.28.2007                *
*                                        *
* RSFQ generic cell for MITLL sfq5ee     *
* Project under IARPA-BAA-16-03          *
* Authored 3 Nov 2015, CJ Fourie, SU     *
* Modified 8 Nov 2016, CJ Fourie, SU     *
*   (Added TimEx port descriptors)       *
* Last mod 23 Mar 2018, L Schindler, SU  *
* (Added PTL drivers & Receivers and   *
*   reduced JJ count)          *
******************************************
*                      in out1 out2
*$Ports                in_in  out_out1  out_out2
.SUBCKT MITLL_SPLITT 5 13 36 
*==============  Begin SPICE netlist of main design ============
B01urx2    4          6          jjmitll100 area=1.00704
B01utx1    9          14         jjmitll100 area=1.69932
B01utx2    33         37         jjmitll100 area=1.69932
B1         19         20         jjmitll100 area=1.69597
B2         21         22         jjmitll100 area=1.20951
B3         23         24         jjmitll100 area=1.20951
IB01_rx2   0          7          pwl(0      0 5p 0.000134948)
IB01_tx1   0          16         pwl(0      0 5p 7.6267e-005)
IB01_tx2   0          39         pwl(0      0 5p 7.6267e-005)
IB1        0          31         pwl(0      0 5p 0.000359683)
L01urx2    5          4          2.6757e-013
L02utx1    9          12         9.42532e-012
L02utx2    33         35         9.42532e-012
L1         4          19         1.52585e-012     
L2         19         25         2.91538e-012     
L3         25         26         4.81369e-013     
L4         26         21         1.27164e-012     
L5         21         9          3.25722e-012     
L6         26         23         1.27164e-012     
L7         23         33         3.25722e-012     
LP01urx2   0          6          3.4e-013
LP01utx1   0          14         5e-014
LP01utx2   0          37         5e-014
Lp1        20         0          2e-013    
Lp2        22         0          2e-013    
Lp3        24         0          2e-013    
LPuIB1     25         31         2e-013 
LPR01urx2  4          7          2e-013
LPR01utx1  9          16         2e-013
LPR01utx2  33         39         2e-013
LRB01urx2  0          8          5e-013
LRB01utx1  0          15         1e-012
LRB01utx2  0          38         1e-012
LRB1       28         0          1e-012   
LRB2       30         0          1e-012   
LRB3       29         0          1e-012   
RB01_rx2   8          4          6.81198
RB01_tx1   15         9          4.03684
RB01_tx2   38         33         4.03684
RB1        19         28         4.04483    
RB2        21         30         5.67164    
RB3        23         29         5.67164    
RINS_tx1   12         13         1.36      
RINS_tx2   35         36         1.36            
.model jjmitll100 jj(rtype=1, vg=2.8mV, cap=0.07pF, r0=160, rn=16, icrit=0.1mA)
.ends MITLL_SPLITT
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
XLOADOUTout1 LOADOUTCELL 4 5
XSINKOUTout1 SINKCELL 5
XLOADOUTout2 LOADOUTCELL 6 7
XSINKOUTout2 SINKCELL 7
XDUT mitll_splitt 3 4 6
.tran 2.5E-13 3E-11 0 2.5E-13
.PRINT NODEV 3 0
.PRINT NODEV 4 0
.PRINT NODEV 6 0
.PRINT DEVI XDUT_LP01UTX1
.PRINT DEVI XDUT_B01UTX1
.PRINT DEVI XDUT_L5
.PRINT DEVI XDUT_B2
.PRINT DEVI XDUT_LP2
.PRINT DEVI XDUT_L4
.PRINT DEVI XDUT_L6
.PRINT DEVI XDUT_L7
.PRINT DEVI XDUT_B01UTX2
.PRINT DEVI XDUT_LP01UTX2
.PRINT DEVI XDUT_B3
.PRINT DEVI XDUT_LP3
.PRINT DEVI XDUT_L3
.PRINT DEVI XDUT_L2
.PRINT DEVI XDUT_L1
.PRINT DEVI XDUT_B01URX2
.PRINT DEVI XDUT_LP01URX2
.PRINT DEVI XDUT_B1
.PRINT DEVI XDUT_LP1
.end
