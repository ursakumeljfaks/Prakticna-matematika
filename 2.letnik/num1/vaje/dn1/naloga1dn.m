format long

mojaTabla = load('salaries.mat')
mojaTabla = mojaTabla.salaries;
b = [1,2,3,6,7,10,15];

%koliko izplačil
izplacila = 52*7;

%celotna vrednost nezaokrozenih izplacil za te delavce
%sum(mojaTabela, 1) sešteje vse vrednosti v vsakem stolpcu
%zmnožek s to tabelo 1 in 0 nam da samo vsoto za naš b
%še ena vsota čez te vsote je da sešteje vse vrednosti za te specifične
%b-je in nam da eno skupno vsoto
vsota = sum(sum(mojaTabla, 1).*[1 1 1 0 0 1 1 0 0 1 0 0 0 0 1]);

%prvo je treba zaokrožiti vrednosti v tabeli
tab = floor(mojaTabla);
posamezne = sum(sum(tab, 1).*[1 1 1 0 0 1 1 0 0 1 0 0 0 0 1]);
vsota2 = abs(vsota-posamezne);

%ce je do centa natančno
tab2 = floor(100*mojaTabla);
posamezne1 = sum(sum(tab2, 1).*[1 1 1 0 0 1 1 0 0 1 0 0 0 0 1]);
vsota3 = abs(vsota-posamezne1/100);

%najprej 1:2:51 začne pri 1, za korak 2 se povečuje do 51, potem pa izpiše
%vse ostanke pri deljenju z 0.01
%to tabelo pomnožimo z vektorjem b in na koncu seštejemo najprej vsak
%stolpec v vektorju b in potem še vse vsote vektorja b
tab3 = mod(mojaTabla(1:2:51,:), 0.01);
vsota4 = sum(sum(tab3, 1).*[1 1 1 0 0 1 1 0 0 1 0 0 0 0 1])


