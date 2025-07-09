A = eye(9);
b = 50;
vektor = [50, 51, 52, 53, 54, 55, 56, 57];

%na 1 mesto nad diagonalo postavi vektor "vektor"
D = diag(vektor,1);
prava = A+D;

%sešteje vrednosti na diagonali
vsota = sum(diag(prava));
%sešteje vrednosti na 1 mestu nad diagonalo, se pravi sešteje vektor
%"vektor"
vsota2 = sum(diag(prava,1));
koncna = vsota + vsota2;

druga = prava*prava;
size(druga);
v = [1; 1; 1; 0; 0; 0; 0; 0; 1];
%norma vektorja n
n = norm(druga*v)
