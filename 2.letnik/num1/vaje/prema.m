function y = prema(L,b)

n = length(b);
y = zeros(n,1);
for i=1:n
    y(i) = b(i) - L(i,1:i-1)*y(1:i-1);
end

        
