function [Q,R,z] = Givens(A,b)

[m,n] = size(A);
Q = eye(m);
for j=1:n
    for i=j+1:m
        r = sqrt(A(j,j)^2 + A(i,j)^2);
        c = A(j,j)/r;
        s = A(i,j)/r;
        A([j,i],j:n) = [c s; -s c] * A([j,i],j:n);
        b([j,i]) = [c s; -s c] * b([j,i]);
        Q([j,i],:) = [c s; -s c] * Q([j,i],:);
    end
end
Q = Q'
R = A
z = b

