function y = premaSub(L,b)
% function y = premaSub(L,b)
% resimo sistem L*y=b, kjer je L spodnje trikotna matrika, 
% preko preme substitucije

n = length(b);
y = zeros(n,1);

for i=1:n
    y(i) = (b(i) - L(i,1:i-1)*y(1:i-1))/L(i,i);
end
