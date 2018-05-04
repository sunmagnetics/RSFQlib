@ECHO OFF

REM run example sequence for TimEx
REM Author:     Coenrad Fourie
REM Last mod:  4 May 2018 by Lieze Schindler

REM You need in the path: jsim_n, iverilog and vvp

@ECHO ON

TimEx .\mitll_nott\mitll_nott.js -d .\Definitions\definitions_ptl.txt -x
::TimEx .\mitll_nott\mitll_nott.js -d .\Definitions\definitions_jtlt.txt -x
::TimEx .\mitll_nott\mitll_nott.js -d .\Definitions\definitions_dfft.txt -x
::TimEx .\mitll_nott\mitll_nott.js -d .\Definitions\definitions_splitt.txt -x
::TimEx .\mitll_nott\mitll_nott.js -d .\Definitions\definitions_merget.txt -x
::TimEx .\mitll_nott\mitll_nott.js -d .\Definitions\definitions_nott.txt -x
::TimEx .\mitll_nott\mitll_nott.js -d .\Definitions\definitions_and2t.txt -x
::TimEx .\mitll_nott\mitll_nott.js -d .\Definitions\definitions_or2t.txt -x
::TimEx .\mitll_nott\mitll_nott.js -d .\Definitions\definitions_xort.txt -x
::TimEx .\mitll_nott\mitll_nott.js -d .\Definitions\definitions_ndroset.txt -x
::TimEx .\mitll_nott\mitll_nott.js -d .\Definitions\definitions_ndroreset.txt -x
pause