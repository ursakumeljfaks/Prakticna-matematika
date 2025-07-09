function [x,k] = newton(F,JF,x0,N,tol)

X = x0;
k = 0;
while k <= N
    k = k + 1;
    dx = -JF(X(:,k))\F(X(:,k));
    X(:,k+1) = X(:,k) + dx;
end
x = X(:,k+1);
end