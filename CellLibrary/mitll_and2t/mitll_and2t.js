*****************************************
* Begin .SUBCKT model                    *
* spice-sdb ver 4.28.2007                *
*                                        *
*		        Version: 1.1.31			 *
*										 *
* RSFQ generic cell for MITLL sfq5ee     *
* Project under IARPA-BAA-16-03          *
* Authored 1 March 2016, JA Delport, SU  *
* Modified 9 Oct 2016, CJ Fourie, SU     *
*   (optmized)                           *
* Modified 23 Mar 2018, L Schindler, SU  *
*	(Added PTL drivers & Receivers and   *
*	  reduced JJ count)      			 *
* Modified 30 Apr 2018, L Schindler, SU  *
*	(Optimized cell)					 *
* Modified 9 May 2018, L Schindler, SU   *
*   (Fixed port connections)	         *
* Last mod 26 Oct 2018, L Schindler, SU  *
*   (Updated parameter values)	         *
******************************************
*                 IN_A   IN_B   CLK   OUT
*$Ports             in_A  in_B  in_clk  out_out
.SUBCKT mitll_and2t 29 12 7 19
*==============  Begin SPICE netlist of main design ============
B01        36         40         jmitll     area=1.3190
B01rx1    6          8          jmitll     area=0.9014
B01rx2    11         13         jmitll     area=0.8806
B01rx3    28         30         jmitll     area=0.8806
B01tx1    16         20         jmitll     area=2.2663
B02        63         67         jmitll     area=1.3190
B03        37         48         jmitll     area=1.1340
B04        68         64         jmitll     area=1.1340
B05        49         50         jmitll     area=1.5270
B06        50         69         jmitll     area=1.5270
B07        51         52         jmitll     area=1.2573
B08        43         47         jmitll     area=1.1670
B09        54         55         jmitll     area=2.0355
B10        34         39         jmitll     area=1.7593
B11        61         66         jmitll     area=1.7593
B14        41         46         jmitll     area=1.5018
IB01       0          38         pwl(0      0 5p 0.000113269)
IB01rx1   0          9          pwl(0      0 5p 0.00012754)
IB01rx2   0          14         pwl(0      0 5p 0.000131447)
IB01rx3   0          31         pwl(0      0 5p 0.000131447)
IB01tx1   0          22         pwl(0      0 5p 0.000213665)
IB02       0          65         pwl(0      0 5p 0.000113269)
IB03       0          56         pwl(0      0 5p 6.26758e-005)
IB07       0          45         pwl(0      0 5p 0.000179299)
L01        37         49         2.5797e-012
L01rx1    7          6          1.7746e-012
L01rx2    12         11         1.5370e-012
L01rx3    29         28         1.5370e-012
L01tx1    54         16         4.6440e-012
L02        69         64         2.5797e-012
L02tx1    16         18         2.7428e-012
L03        34         35         1.9325e-012
L04        61         62         1.9325e-012
L05        44         48         1.1464e-012
L06        68         44         1.1464e-012
L07        42         43         1.9932e-012
L08        51         53         3.9e-014  
L09        53         54         2.9248e-012
L13        28         34         2.2304e-012
L14        11         61         2.2304e-012
L15        35         36         6.1049e-012
L16        62         63         6.1049e-012
L17        6          41         1.9428e-012
L19        41         42         2.0373e-013
L20        50         51         3.9901e-013
L21        36         37         1.2909e-013
L22        63         64         1.2909e-013
L23        43         44         1e-014    
LP01       0          40         2.55e-013 
LP01rx1   0          8          3.4e-013  
LP01rx2   0          13         3.4e-013  
LP01rx3   0          30         3.4e-013  
LP01tx1   0          20         5e-014    
LP02       0          67         2.55e-013 
LP07       0          52         2.99e-013 
LP08       0          47         2.11e-013 
LP09       0          55         1.74e-013 
LP10       0          39         2.21e-013 
LP11       0          66         2.21e-013 
LP14       0          46         1.87e-013 
LPR01rx1  6          9          2e-013    
LPR01rx2  11         14         2e-013    
LPR01rx3  28         31         2e-013    
LPR01tx1  16         22         2e-013    
LPR1       35         38         1.3e-014  
LPR2       62         65         1.3e-014  
LPR3       53         56         1.901e-012
LPR4       42         45         8.5e-013  
LRB01      58         0          1e-012    
LRB01rx1  0          10         5e-013    
LRB01rx2  0          15         5e-013    
LRB01rx3  0          32         5e-013    
LRB01tx1  0          21         1e-012    
LRB02      71         0          1e-012    
LRB03      59         48         1e-012    
LRB04      68         72         1e-012    
LRB05      60         50         1e-012    
LRB06      50         75         1e-012    
LRB07      76         0          1e-012    
LRB08      74         0          1e-012    
LRB09      77         0          1e-012    
LRB10      57         0          1e-012    
LRB11      70         0          1e-012    
LRB14      73         0          1e-012    
RB01       58         36         5.20089   
RB01rx1   10         6          7.61037   
RB01rx2   15         11         7.78977   
RB01rx3   32         28         7.78977   
RB01tx1   21         16         3.02698   
RB02       71         63         5.20089   
RB03       59         37         6.04915   
RB04       64         72         6.04915   
RB05       60         49         4.49237   
RB06       69         75         4.49237   
RB07       76         51         5.4563    
RB08       74         43         5.87817   
RB09       77         54         3.37022   
RB10       57         34         3.89913   
RB11       70         61         3.89913   
RB14       73         41         4.56777   
RINStx1   18         19         1.36      
.model jmitll jj(rtype=1, vg=2.6mV, cap=0.07pF, r0=160, rn=16, icrit=0.1mA)
.ends mitll_and2t
