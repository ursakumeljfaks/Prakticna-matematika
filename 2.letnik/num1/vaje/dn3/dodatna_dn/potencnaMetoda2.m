function [lambda, z] = potencnaMetoda2(A, z0, tol)

z = z0 / norm(z0);
y = A * z;
lambda = z' * y;
z = y / norm(y);

while norm(y - lambda * z) >= tol
    y = A * z;
    lambda = z' * y;
    z = y / norm(y);
end

end