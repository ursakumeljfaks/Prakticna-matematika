function [lambda,z] = potencnaMetoda(A, z0, stKorakov, tol)

z = z0/norm(z0);

for i=1:stKorakov
    y = A*z;
    lambda = z'*y;
    z = y/norm(y);
    if norm(y - lambda * z) < tol
        break;
    end
end
