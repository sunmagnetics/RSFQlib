@ECHO OFF

REM Run test sequence for RSFQ cell library
REM Author:     Lieze Schindler
REM Last mod:   17 August 2018

REM You need in the path: jsim_n, JoSIM, WRspice and sp

@ECHO ON

josim -m .\output.dat .\mitll_and2t\tb_mitll_and2t.js -g

pause