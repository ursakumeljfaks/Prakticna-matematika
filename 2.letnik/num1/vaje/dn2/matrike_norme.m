format long
n = 101;
A1 = magic(n);
for i=1:n
    for j=1:n
        A1(i,j) = 1/A1(i,j);
    end
end
A = A1;


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

C = A/10 + B + eye(n)/100;
b = ones(n,1);

%pogojenostno stevilo matrike C v prvi normi
pogojenostno = norm(C,1) * norm(inv(C),1);

%LU razcep za matriko C brez pivotiranja in izracun druge norme Cx-b
[L,U,I] = luRazcep(C);
pivot = I;

%normalni sistem C'Cx=C'b, potem Choleski
D = C'*C;
V_t = chol(D);
V = V_t';
y2 = premaSub(V,C'*b); 
x2 = obratnaSub(V', y2);
neskoncna = norm(x2,"inf");

