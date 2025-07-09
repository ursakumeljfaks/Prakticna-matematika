mojaTabla = load('no_transistors.mat');
mojaTabla = mojaTabla.data;

semilogy(mojaTabla(:,1), mojaTabla(:,2));
X = mojaTabla(:,1);
Y = mojaTabla(:,2);
%povprecje vseh tranzistorjev
povprecje = sum(mojaTabla(:,2))/length(mojaTabla(:,2));

b = log(mojaTabla(:,2));
prva = norm(b,1);

n = length(mojaTabla(:,2));
A = [ones(n,1) X X.^2];
frobenious = norm(A,"fro");

%predolocen sistem za Ac=b -> LUc=b
[L,U] = luRazcep(A'*A);
%Ly=b ->prema substitucija
y = premaSub(L, A'*b);
%Uc=y ->obratna substitucija
c = obratnaSub(U,y);
%vsota absolutnih vrednosti koeficientov vektorja c
vsota = 0;
for i=1:length(c)
    vsota = vsota + abs(c(i))
end
vsota;

%graf
semilogy(X,A*c,X,b)

%najvecje odstopanje ene od druge (odstejes y koordinate ene in druge ter
% pogledas maksimalno vrednost absolutnih vrednosti le teh)
max(abs(b-A*c))






