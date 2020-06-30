@ECHO OFF
REM Windows batch script for TimEx extractions for all cells

REM run example sequence for TimEx
REM Author:    Lieze Schindler
REM Last mod:  26 June 2020

REM use -c instead of -x to extract self-contained verilog files (with timing)

@ECHO ON

TimEx .\mitll_and2t\LSmitll_AND2T_v1p5.cir -d .\Definitions\definitions_ptl.txt -x

TimEx .\mitll_buff\LSmitll_buff_v1p5.cir -d .\Definitions\definitions.txt -x

TimEx .\mitll_bufft\LSmitll_bufft_v1p5.cir -d .\Definitions\definitions_ptl.txt -x

TimEx .\mitll_clksplt\LSmitll_CLKSPLT_v1p5.cir -d .\Definitions\definitions.txt -x

TimEx .\mitll_clkspltt\LSmitll_CLKSPLTT_v1p5.cir -d .\Definitions\definitions_ptl.txt -x

TimEx .\mitll_dfft\LSmitll_DFFT_v1p5.cir -d .\Definitions\definitions_ptl.txt -x

TimEx .\mitll_jtlt\LSmitll_JTLT_v1p5.cir -d .\Definitions\definitions_ptl.txt -x

TimEx .\mitll_merget\LSmitll_MERGET_v1p5.cir -d .\Definitions\definitions_ptl.txt -x

TimEx .\mitll_ndrot\LSmitll_NDROT_v1p5.cir -d .\Definitions\definitions_ptl.txt -x

TimEx .\mitll_nott\LSmitll_NOTT_v1p5.cir -d .\Definitions\definitions_ptl.txt -x

TimEx .\mitll_or2t\LSmitll_OR2T_v1p5.cir -d .\Definitions\definitions_ptl.txt -x

TimEx .\mitll_ptltx\LSmitll_ptltx_v1p5.cir -d .\Definitions\definitions_ptltx.txt -x

TimEx .\mitll_ptlrx\LSmitll_ptlrx_v1p5.cir -d .\Definitions\definitions_ptlrx.txt -x

TimEx .\mitll_splitt\LSmitll_SPLITT_v1p5.cir -d .\Definitions\definitions_ptl.txt -x

TimEx .\mitll_xort\LSmitll_XORT_v1p5.cir -d .\Definitions\definitions_ptl.txt -x

pause

