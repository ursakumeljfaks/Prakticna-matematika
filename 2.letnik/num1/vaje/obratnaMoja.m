function x = obratnaMoja(U,y)

n = length(y);
x = zeros(n, 1);
for i=n:-1:1
    x(i) = (y(i) - x(i+1:n)*U(i, i+1:n))/U(i,i);
end