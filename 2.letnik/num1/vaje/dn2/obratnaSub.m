function x = obratnaSub(U,y)
% function y = obratnaSub(U,y)
% resimo sistem U*x=y, kjer je U zgordnje trikotna matrika, 
% preko obratne substitucije

n = length(y);
x = zeros(n,1);

for i=n:-1:1
    x(i) = (y(i) - U(i,i+1:n)*x(i+1:n))/U(i,i);
end