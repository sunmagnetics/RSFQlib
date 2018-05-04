* JSIM deck file generated with TimEx
* === DEVICE-UNDER-TEST ===
******************************************
* Begin .SUBCKT model                    *
* spice-sdb ver 4.28.2007                *
*                                        *
* RSFQ generic cell for MITLL sfq5ee     *
* Project under IARPA-BAA-16-03          *
* Authored 5 March 2016, JA Delport, SU  *
* Modified 28 Nov 2016, CJ Fourie, SU    *
*   (Deleted current sources, altered    *
*    circuit to make functional;         *
*    optimized)                          *
* Modified 23 Mar 2018, L Schindler, SU  *
*	(Added PTL drivers & Receivers and   *
*	  reduced JJ count)      			 *
* Last mod 20 April 2018, L Schindler, SU *
*    (Adapted to work with TimEx to      *
*     produce verilog file)              *
******************************************
*                 IN_IN    CLK     OUT
*$Ports           in_in    in_clk  out_out
.SUBCKT mitll_nott 51 46 57 
*==============  Begin SPICE netlist of main design ============
B01        12         13         jmitll     area=1.34879
B01_rx1    45         47         jmitll     area=1.24756
B01_rx2    50         52         jmitll     area=1.261343
B01_tx1    55         58         jmitll     area=2.85096
B02        8          10         jmitll     area=0.771808
B03        21         8          jmitll     area=1.22267
B05        5          6          jmitll     area=1.222101
B06        15         16         jmitll     area=1.04323
B07        1          3          jmitll     area=2.21391
B09        18         19         jmitll     area=1.40995
B10        24         25         jmitll     area=1.72271
B11        28         29         jmitll     area=1.41931
IB01_rx1   0          48         pwl(0      0 5p 0.000181215)
IB01_rx2   0          53         pwl(0      0 5p 0.000146094)
IB01_tx1   0          60         pwl(0      0 5p 0.000187178)
IB02       0          9          pwl(0      0 5p 9.69782e-005)
IB03       0          31         pwl(0      0 5p 9.52213e-005)
IB04       0          38         pwl(0      0 5p 0.000101564)
IB06       0          44         pwl(0      0 5p 0.000108369)
L01        5          13         2.28471e-012    
L01_rx1    46         45         2.14574e-012
L01_rx2    51         50         1.85705e-012
L01_tx1    18         55         4.51952e-012
L02_rx1    45         2          2.54675e-012
L02_rx2    50         30         4.47184e-012
L02_tx1    55         56         3.47235e-012
L03        5          7          6.59615e-012    
L04        7          8          4.24132e-013    
L06        4          5          3.28596e-012    
L07        12         10         4.99855e-013    
L08        23         21         8.69458e-013    
L09        12         15         2.84165e-013    
L10        15         17         5.3650679E-12
L12        27         23         2.65318e-012    
L13        2          1          2.15661e-012    
L16        30         28         2.61168e-012    
L17        1          4          9.91803e-013    
L18        23         24         2.58424e-013    
L19        24         26         3.16811e-012    
L20        28         27         1.16759e-012    
L21        17         18         7.46111e-013    
LP01_rx1   0          47         3.4e-013
LP01_rx2   0          52         3.4e-013
LP01_tx1   0          58         5e-014
LP05       0          6          5.67e-013   
LP06       0          16         2.7e-013   
LP07       0          3          3.28e-013   
LP09       0          19         1.2e-013   
LP10       0          25         2.39e-013   
LP11       0          29         1.09e-013   
LPR01_rx1  2          48         2e-013
LPR01_rx2  30         53         2e-013
LPR01_tx1  55         60         2e-013
LPR02      7          9          2.3e-014  
LPR03      4          31         2.08e-013  
LPR04      27         38         2.16e-013  
LPR06      17         44         1.3e-013  
LRB01      14         12         1e-012  
LRB01_rx1  0          49         1e-012
LRB01_rx2  0          54         1e-012
LRB01_tx1  0          59         1e-012
LRB02      10         11         1e-012  
LRB03      21         22         1e-012  
LRB05      0          33         1e-012  
LRB06      0          34         1e-012  
LRB07      0          32         1e-012  
LRB09      0          35         1e-012  
LRB10      0          37         1e-012  
LRB11      0          36         1e-012  
RB01       14         13         5.08598   
RB01_rx1   49         45         4.73894
RB01_rx2   54         50         7.9642
RB01_tx1   59         55         2.58771
RB02       11         8          8.88809   
RB03       22         8          5.61061   
RB05       33         5          7.43943   
RB06       34         15         6.57567   
RB07       32         1          3.09855   
RB09       35         18         4.86536   
RB10       37         24         3.98204   
RB11       36         28         4.83327   
RD         26         0          3.54      
RINS_tx1   56         57         1.36      
.model jmitll jj(rtype=1, vg=2.8mV, cap=0.07pF, r0=160, rn=16, icrit=0.1mA)
.ends mitll_nott
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
b01   23 27 jjmitll100 area=2
b02   24 26 jjmitll100 area=1.62
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
.SUBCKT SINKCELL  45
rix1 40 0 2
rox1 51 0  2
b01        12         13         jmitll     area=1.85
b01rx1     44         46         jmitll     area=1
b01rx2     39         41         jmitll     area=1
b01tx1     49         52         jmitll     area=2
b02        8          10         jmitll     area=1.1
b03        20         8          jmitll     area=1.35
b05        5          6          jmitll     area=1.05
b06        15         16         jmitll     area=1.3
b07        1          3          jmitll     area=2
b09        18         19         jmitll     area=1.75
b10        23         24         jmitll     area=2.38
b11        27         28         jmitll     area=2.16
ib01rx1    0          47         pwl(0      0 5p 155u)
ib01rx2    0          42         pwl(0      0 5p 155u)
ib01tx1    0          54         pwl(0      0 5p 180u)
ib02       0          9          pwl(0      0 5p 125u)
ib03       0          30         pwl(0      0 5p 110u)
ib04       0          37         pwl(0      0 5p 110u)
ib06       0          38         pwl(0      0 5p 110u)
l01        5          13         3p
l01rx1     45         44         2p
l01rx2     40         39         2p
l01tx1     18         49         2p
l02rx1     44         29         4.3p
l02rx2     39         2          4.3p
l02tx1     49         50         3.3p
l03        5          7          8.3p
l04        7          8          2p
l06        4          5          3.6p
l07        12         10         2p
l08        22         20         1.186p
l09        12         15         0.239p
l10        15         17         5.53p
l12        26         22         2.95p
l13        2          1          1.53p
l16        29         27         2.577p
l17        1          4          1.01p
l18        22         23         2p
l19        23         25         2.571p
l20        27         26         1p
l21        17         18         1p
lp01rx1    0          46         0.34p
lp01rx2    0          41         0.34p
lp01tx1    0          52         0.05p
lp05       0          6          0.567p
lp06       0          16         0.27p
lp07       0          3          0.328p
lp09       0          19         0.12p
lp10       0          24         0.239p
lp11       0          28         0.109p
lpr01rx1   29         47         0.2p
lpr01rx2   2          42         0.2p
lpr01tx1   49         54         0.2p
lpr02      7          9          0.023p
lpr03      4          30         0.208p
lpr04      26         37         0.216p
lpr06      17         38         0.13p
lrb01      14         12         1p
lrb01rx1   0          48         0.5p
lrb01rx2   0          43         0.5p
lrb01tx1   0          53         1p
lrb02      10         11         1p
lrb03      20         21         1p
lrb05      0          32         1p
lrb06      0          33         1p
lrb07      0          31         1p
lrb09      0          34         1p
lrb10      0          36         1p
lrb11      0          35         1p
rb01       14         13         5.24
rb01rx1    48         44         9.7
rb01rx2    43         39         9.7
rb01tx1    53         49         4.85
rb02       11         8          8.8
rb03       21         8          7.2
rb05       32         5          9.2
rb06       33         15         7.46
rb07       31         1          4.85
rb09       34         18         5.54
rb10       36         23         4.08
rb11       35         27         4.5
rd         25         0          3.54
rinstx1    50         51         1.36
.model jmitll jj(rtype=1, vg=2.8mv, cap=0.07pf, r0=160, rn=16, icrit=0.1ma)
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
XDUT mitll_nott 3 6 7
.tran 2.5E-13 6E-11 0 2.5E-13
.PRINT NODEV 3 0
.PRINT NODEV 6 0
.PRINT NODEV 7 0
.PRINT DEVI XDUT_LP06
.PRINT DEVI XDUT_B06
.PRINT DEVI XDUT_L10
.PRINT DEVI XDUT_L21
.PRINT DEVI XDUT_B09
.PRINT DEVI XDUT_LP09
.PRINT DEVI XDUT_L01TX1
.PRINT DEVI XDUT_B01TX1
.PRINT DEVI XDUT_LP01TX1
.PRINT DEVI XDUT_L09
.PRINT DEVI XDUT_L07
.PRINT DEVI XDUT_B02
.PRINT DEVI XDUT_B03
.PRINT DEVI XDUT_L08
.PRINT DEVI XDUT_L18
.PRINT DEVI XDUT_B10
.PRINT DEVI XDUT_LP10
.PRINT DEVI XDUT_L12
.PRINT DEVI XDUT_L20
.PRINT DEVI XDUT_B11
.PRINT DEVI XDUT_LP11
.PRINT DEVI XDUT_L16
.PRINT DEVI XDUT_L02RX1
.PRINT DEVI XDUT_B01RX1
.PRINT DEVI XDUT_LP01RX1
.PRINT DEVI XDUT_L04
.PRINT DEVI XDUT_L03
.PRINT DEVI XDUT_L01
.PRINT DEVI XDUT_B01
.PRINT DEVI XDUT_L06
.PRINT DEVI XDUT_L17
.PRINT DEVI XDUT_L13
.PRINT DEVI XDUT_L02RX2
.PRINT DEVI XDUT_B01RX2
.PRINT DEVI XDUT_LP01RX2
.PRINT DEVI XDUT_B07
.PRINT DEVI XDUT_LP07
.PRINT DEVI XDUT_B05
.PRINT DEVI XDUT_LP05
.end
