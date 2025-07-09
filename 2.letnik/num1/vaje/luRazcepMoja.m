function [L,U] = luRazcepMoja(A)
%metoda izracuna LU razcep matrike A brez pivotiranja in nam vrne
%matriki L (spodnje trikotna z enicami po diagonali) in U zgornje trikotna
n = length(A);

for j=1:n-1
    for i=j+1:n
        A(i,j) = A(i,j)/A(j,j);
        for k=j+1:n
            A(i,k) = A(i,k) - A(i,j)*A(j,k);
        end
    end
end

L = tril(A, -1) + eye(n)
U = triu(A)


A = [1 2 1 2;
     2 6 4 5;
     3 10 8 10;
     1 6 6 9];

