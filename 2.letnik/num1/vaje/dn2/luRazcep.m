function [L,U,I] = luRazcep(A)

%metoda izracuna LU razcep matrike A (brez pivotiranja) in nam vrne matriki
%L, U

n = length(A);
I = abs(A(1,1));

for j=1:n-1
    for i=j+1:n
        A(i,j) = A(i,j)/A(j,j);
        I = abs(A(j,j));
        for k=j+1:n
            A(i,k) = A(i,k)-A(i,j)*A(j,k);
        end
    end
end

U = triu(A)
L = tril(A,-1) + eye(n)
I