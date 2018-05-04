*****************************************
* Begin .SUBCKT model                    *
* spice-sdb ver 4.28.2007                *
*                                        *
* RSFQ generic cell for MITLL sfq5ee     *
* Project under IARPA-BAA-16-03          *
* Authored 1 March 2016, JA Delport, SU  *
* Modified 9 Oct 2016, CJ Fourie, SU     *
*   (optmized)                           *
* Modified 23 Mar 2018, L Schindler, SU  *
*	(Added PTL drivers & Receivers and   *
*	  reduced JJ count)      			 *
* Last mod 30 April 2018, L Schindler, SU *
*	(Optimized cell)					 *
******************************************
*                 IN_A   IN_B   CLK   OUT
*$Ports             in_A  in_B  in_clk  out_out
.SUBCKT mitll_and2t 19 7 2 14 
*==============  Begin SPICE netlist of main design ============
B01        25         29         jmitll     area=1.31899
B01rx1     18         20         jmitll     area=1.501389
B01rx2     6          8          jmitll     area=0.88063
B01rx3     1          3          jmitll     area=0.88063
B01tx1     11         15         jmitll     area=2.26625
B02        51         55         jmitll     area=1.31899
B03        26         37         jmitll     area=1.13403
B04        56         52         jmitll     area=1.13403
B05        38         39         jmitll     area=1.52701
B06        39         57         jmitll     area=1.52701
B07        40         41         jmitll     area=1.25725
B08        32         36         jmitll     area=1.56701
B09        12         43         jmitll     area=2.03545
B10        23         28         jmitll     area=1.75934
B11        49         54         jmitll     area=1.75934
B14        30         35         jmitll     area=1.50181
IB01       0          27         pwl(0      0 5p 0.000113269)
IB01rx1    0          21         pwl(0      0 5p 0.00012754)
IB01rx2    0          9          pwl(0      0 5p 0.000131447)
IB01rx3    0          4          pwl(0      0 5p 0.000131447)
IB01tx1    0          17         pwl(0      0 5p 0.000213665)
IB02       0          53         pwl(0      0 5p 0.000113269)
IB03       0          44         pwl(0      0 5p 6.26758e-005)
IB07       0          34         pwl(0      0 5p 0.000179299)
L01        26         38         2.57965e-012   
L01rx1     19         18         1.7746e-012    
L01rx2     7          6          1.53695e-012    
L01rx3     2          1          1.53695e-012     
L01tx1     12         11         4.64399e-012 
L02        57         52         2.57965e-012    
L02tx1     11         13         2.74282e-012 
L03        23         24         1.93254e-012   
L04        49         50         1.93254e-012   
L05        33         37         1.14641e-012   
L06        56         33         1.14641e-012  
L07        31         32         1.99319e-012  
L08        40         42         3.9e-014    
L09        42         12         2.92475e-012    
L13        18         23         2.2304e-012       
L14        6          49         2.2304e-012       
L15        24         25         6.1049e-012    
L16        50         51         6.1049e-012    
L17        1          30         1.94279e-012          
L19        30         31         2.03734e-013    
L20        39         40         3.9901e-013    
L21        25         26         1.29089e-013     
L22        51         52         1.29089e-013     
L23        32         33         0.01p     
LP01       0          29         0.255p    
LP01rx1    0          20         0.34p     
LP01rx2    0          8          0.34p     
LP01rx3    0          3          0.34p     
LP01tx1    0          15         0.05p     
LP02       0          55         0.229p    
LP07       0          41         0.299p    
LP08       0          36         0.211p    
LP09       0          43         0.174p    
LP10       0          28         0.221p    
LP11       0          54         0.203p    
LP14       0          35         0.187p    
LPR01rx1   18         21         0.2p      
LPR01rx2   6          9          0.2p      
LPR01rx3   1          4          0.2p      
LPR01tx1   11         17         0.2p      
LPR1       24         27         0.013p    
LPR2       50         53         0.01p     
LPR3       42         44         1.901p    
LPR4       31         34         0.85p     
LRB01      46         0          1p        
LRB01rx1   0          22         0.5p      
LRB01rx2   0          10         0.5p      
LRB01rx3   0          5          0.5p      
LRB01tx1   0          16         1p        
LRB02      59         0          1p        
LRB03      47         37         1p        
LRB04      56         60         1p        
LRB05      48         39         1p        
LRB06      39         63         1p        
LRB07      64         0          1p        
LRB08      62         0          1p        
LRB09      65         0          1p        
LRB10      45         0          1p        
LRB11      58         0          1p        
LRB14      61         0          1p        
RB01       46         25         5.20089          
RB01rx1    22         18         7.61037  
RB01rx2    10         6          7.78977     
RB01rx3    5          1          7.78977     
RB01tx1    16         11         3.02698   
RB02       59         51         5.20089         
RB03       47         26         6.04915      
RB04       52         60         6.04915        
RB05       48         38         4.49237        
RB06       57         63         4.49237         
RB07       64         40         5.4563        
RB08       62         32         5.87817         
RB09       65         12         3.37022        
RB10       45         23         3.89913      
RB11       58         49         3.89913       
RB14       61         30         4.56777         
RINStx1    13         14         1.36      
.model jmitll jj(rtype=1, vg=2.8mV, cap=0.07pF, r0=160, rn=16, icrit=0.1mA)
.ends mitll_and2t
*******************************
