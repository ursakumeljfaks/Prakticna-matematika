%2. naloga iz spletne učilnice NalogeOctave

function [matrika] = vaje_2(n)
% function [matrika] = vaje_2(n) 
% funkcija sprejme število n in vrne nxn matriko
A=diag(1:n);

B=triu(4*ones(n),1); %najprej ustvarimo matriko samih 1 velikosti 5x5,
                    %potem z triu ustvarimo zgornjetrikotno, z 1 pa
                    %ustvarimo, da se diagonala premakne za eno naprej in
                    %se krat 4, da dobimo same 4
C=diag(ones(n-1,1),-1);
D=-1*diag(ones(n-2,1),-2); 
matrika = A+B+C+D


