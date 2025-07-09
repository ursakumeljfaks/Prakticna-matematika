A = [3, 2, 8, 1
     7, 2, 5, 6
     0, 7, 3, 5]

A'; %transponiranje matrike
A(2,3); %element v 2 vrstici in 3 stolpcu
A(:, [1, 4]); %izpiše 1 in 4 stolpec kot svojo matriko
A([2 3], [3 1]); %izpiše 3 in 1 element v 2 in 3 vrstici kot svojo matriko
A(:, 1:2:end); %izpiše 1 stolpec in gre za korak 2 naprej (1+2=3) in izpiše še 3
A(:); %izpiše vse vrednosti indeksov matrike
[A; A(end, :)]; %naredi novo matriko, kjer doda za zadnjo vrstico zadnjo vrstico matrike A
A + eye(3,4); %matriki A prišteje identično matriko, ki ima enke 3x3 in zadnji stolpec ničle
A - 3; %vsem elementom matrike A bo odštel 3
A(end:-1:1,:); %izpisal bo matriko, ki bo začela pri zadnji vrstici in se bo za korak -1 šla do 1 vrstice
fliplr(A); %nova matrika, katere vrstice so obrnjene, začnejo iz leve proti desni
diag(A); %izpiše vrednosti matrike A po diagonali
diag(diag(A)); %naredi diagonalno matriko iz števil diag(A)
tril(A); %naredi spodnje trikotno matriko matrike A, vsa števila na zgornji diagonali zamenja z 0
triu(A); %naredi zgornje trikotno matriko matrike A
A.^2; %vsako število pri posameznem indeksu bo dal na potenco 2
exp(A); %vsako število da e na vsako število matrike A
size(A); %vrne velikost matrike A
max(A); %vrača največji element matrike A po stolpcih
max(max(A)); %vrne največje število od te vrstice z največjimi elementi vsakega stolpca
A == 2; %vrne 1 (kot True) na mestih, kjer je enako 2, na ostalih pa 0
A ~= 2; %to je znak za neenakost, tam kjer je enako 2 vrne 0, tam kjer ni pa 1
A>2; %tam kjer so elementi večji od 2 da 1, tam kjer niso da 0

%Drugi pdf 1. naloga%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
B=[11, 2, -3, 0
    2, 1, 8, 7
    0, 22, 21, -9
    4, -3, 2, 0
    5, 1, 10, -8]
C=[1, 2, 0, 4
    2, 9, 2, 3
    3, 0, 1, 2
    4, 3, 2, 8]
size(B); %dimenzija matrike B
B'; %transponirana matrika B
B(3,2); %element v 3 vrstici in 2 stolpcu
B(:,2); %drugi stolpec matrike B
B(3,:); %tretja vrstica matrike B
%ni mi jasno kako naj bi izgledala ta podmatrika
max(max(B)); %največji element matrike B
B*(1/2); %matriko, katere elementi so elementi matrike B pomnoženi z 1/2
C.^2; %matriko, katere elementi so kvadrati elementov matrike C
C^2;
B*diag(diag(C)); %produkt matrike B in diagonalne matrike, katere diagonala je enaka diagonali matrike C
triu(C)-diag(diag(C)); %zgornjetrikotno matriko matrike C brez diagonale



