* JSIM deck file generated with TimEx
* === DEVICE-UNDER-TEST ===
*****************************************
* Begin .SUBCKT model                    *
* spice-sdb ver 4.28.2007                *
*                                        *
* RSFQ generic cell for MITLL sfq5ee     *
* Project under IARPA-BAA-16-03          *
* Authored 5 Nov 2015, CJ Fourie, SU     *
* Modified 1 March 2016, JA Delport, SU  *
* Modified 23 Aug 2016, CJ Fourie, SU    *
* Modified 9 Oct 2016, CJ Fourie, SU     *
*   (added DMP junction B2, optmized)    *
* Last mod 23 Mar 2018, L Schindler, SU  *
* (Added PTL drivers & Receivers and   *
*   reduced JJ count)          *
******************************************
*     in  clk  out
*$Ports             in_in  in_clk  out_out
.SUBCKT mitll_dfft 9 7 10 
*
*==============  Begin SPICE netlist of main design ============
B01rx1     20         22         jmitll     area=0.793833
B01rx2     12         16         jmitll     area=0.906104
B01tx      26         27         jmitll     area=3.02709
B02rx2     14         15         jmitll     area=0.963766
B1         30         31         jmitll     area=1.42778
B2         39         52         jmitll     area=1.49875
B3         45         51         jmitll     area=0.960227
B4         32         33         jmitll     area=1.6952
B5         43         32         jmitll     area=1.17345
B6         36         37         jmitll     area=1.36404
B7         34         35         jmitll     area=1.49997
IB01rx1    0          23         pwl(0      0 5p 0.000115456)
IB01rx2    0          17         pwl(0      0 5p 0.000101889)
IB01tx     0          29         pwl(0      0 5p 0.000181403)
IB1        0          53         pwl(0      0 5p 0.000120402)
IB2        0          54         pwl(0      0 5p 6.34786e-005)
IB3        0          55         pwl(0      0 5p 0.000153633)
IB4        0          56         pwl(0      0 5p 0.00016173)
L01rx1     9          20         1.40665e-012 
L01rx2     7          12         1.23102e-012 
L01tx1     26         25         1.80401e-012 
L02rx1     20         21         3.29467e-012 
L02rx2     12         13         2.44036e-012 
L03rx2     13         14         3.64944e-012 
L1         21         30         1.12845e-012     
L2a        30         48         5.40283e-013    
L2b        48         39         1.60289e-012    
L3a        45         49         9.45374e-013    
L3b        49         32         4.44009e-012    
L4         52         45         1.11414e-012     
L5a        32         50         3.63494e-012    
L5b        50         34         5.93935e-013    
L6         34         26         1.32327e-012     
L7         36         43         1.9079e-012     
L8         14         36         1.79764e-012     
LIB01rx2   13         17         2e-013
LIB01tx    26         29         2e-013
LIB2       49         54         2e-013   
LIB3       50         55         2e-013   
LPB01rx1   0          22         3.4e-013
LPB01rx2   0          16         3.4e-013
LPB01tx    0          27         5e-014
LPB02rx2   0          15         6e-014
LPB1       31         0          2e-013   
LPB3       51         0          2e-013   
LPB4       33         0          2e-013   
LPB6       37         0          2e-013   
LPB7       35         0          2e-013   
LPIB01rx1  21         23         2e-013
LPIB1      48         53         2e-013  
LPIB4      56         36         2e-013  
LRB01rx1   0          24         5e-013
LRB01rx2   0          18         5e-013
LRB01tx    0          28         1e-012
LRB02rx2   0          19         1e-012
LRB1       41         0          1e-012   
LRB2       38         52         1e-012   
LRB3       44         0          1e-012   
LRB4       46         0          1e-012   
LRB5       42         32         1e-012   
LRB6       40         0          1e-012   
LRB7       47         0          1e-012   
RB01rx1    24         20         8.6415
RB01rx2    18         12         7.57077
RB01tx     28         26         2.26617 
RB02rx2    19         14         7.11781
RB1        30         41         4.80461    
RB2        39         38         4.5771    
RB3        45         44         7.14404    
RB4        32         46         4.04666    
RB5        43         42         5.84592    
RB6        40         36         5.02909    
RB7        34         47         4.57337    
RINStx     25         10         1.36      
.model jmitll jj(rtype=1, vg=2.8mV, cap=0.07pF, r0=160, rn=16, icrit=0.1mA)
.ends mitll_dfft
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
I_in 0 1 pwl(0 0 5p 0 1.25E-11 0 1.35E-11 0.001 1.45E-11 0 2.25E-11 0 2.35E-11 0.001 2.45E-11 0)
XSOURCEINin SOURCECELL 1 2
XLOADINin LOADINCELL 2 3
I_clk 0 4 pwl(0 0 5p 0 3.25E-11 0 3.35E-11 0.001 3.45E-11 0 4.25E-11 0 4.35E-11 0.001 4.45E-11 0)
XSOURCEINclk SOURCECELL 4 5
XLOADINclk LOADINCELL 5 6
XLOADOUTout LOADOUTCELL 7 8
XSINKOUTout SINKCELL 8
XDUT mitll_dfft 3 6 7
.tran 2.5E-13 6E-11 0 2.5E-13
.PRINT NODEV 3 0
.PRINT NODEV 6 0
.PRINT NODEV 7 0
.PRINT DEVI XDUT_LPB02RX2
.PRINT DEVI XDUT_B02RX2
.PRINT DEVI XDUT_L8
.PRINT DEVI XDUT_B6
.PRINT DEVI XDUT_LPB6
.PRINT DEVI XDUT_L7
.PRINT DEVI XDUT_B5
.PRINT DEVI XDUT_L3B
.PRINT DEVI XDUT_L3A
.PRINT DEVI XDUT_B3
.PRINT DEVI XDUT_LPB3
.PRINT DEVI XDUT_L4
.PRINT DEVI XDUT_B2
.PRINT DEVI XDUT_L2B
.PRINT DEVI XDUT_L2A
.PRINT DEVI XDUT_L1
.PRINT DEVI XDUT_L02RX1
.PRINT DEVI XDUT_B01RX1
.PRINT DEVI XDUT_LPB01RX1
.PRINT DEVI XDUT_B1
.PRINT DEVI XDUT_LPB1
.PRINT DEVI XDUT_L5A
.PRINT DEVI XDUT_L5B
.PRINT DEVI XDUT_L6
.PRINT DEVI XDUT_B01TX
.PRINT DEVI XDUT_LPB01TX
.PRINT DEVI XDUT_B7
.PRINT DEVI XDUT_LPB7
.PRINT DEVI XDUT_B4
.PRINT DEVI XDUT_LPB4
.PRINT DEVI XDUT_L03RX2
.PRINT DEVI XDUT_L02RX2
.PRINT DEVI XDUT_B01RX2
.PRINT DEVI XDUT_LPB01RX2
.end
