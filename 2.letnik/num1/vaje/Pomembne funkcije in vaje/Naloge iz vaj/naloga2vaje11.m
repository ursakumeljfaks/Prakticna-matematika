T = load('cryptomarket.csv');
A = T(1 : 10, 1 : 10);

%prva naloga
c = sum(T, 2);
ena = norm(c, 1);
dva = norm(c);
infi = norm(c, "inf");

%drug naloga
%prva norma
prva = max(sum(abs(A)));

%druga norma
druga = norm(A);
druga2 = sqrt(sum(eig(A'*A)));

%neskončna norma
neskoncna = max(sum(abs(A')));

%Frobeniousova norma
frob = sqrt(sum(diag(A'*A)));

%ocene
1/sqrt(10)*frob <= druga <= frob