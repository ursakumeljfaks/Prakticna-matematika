n = 101;
A = magic(n) * (-1);

B = [];
for i=1:n
    for j=1:n
        if mod(i+j,2) == 0
            B(i,j) = 1;
        else
            B(i,j) = 0;
        end
    end
end
B;

C = A/10 + B;
b = ones(1,n);

%pogojenostno stevilo matrike C v prvi normi
norm(C,1) * norm(inv(C),1)

%LU razcep za matriko C brez pivotiranja in izracun druge norme Cx-b
[L,U] = luRazcep(C);
%LUx=b -> prema substitucija
y = premaSub(L,b);
%Ux=y -> obratna substitucija
x = obratnaSub(U,y);
norm(C*x-b)

 
