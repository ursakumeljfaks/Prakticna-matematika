function [lambda, z] = inverznaPotencnaMetoda(A, z0, tarca, stKorakov, tol)

z = z0 / norm(z0);
lambda = 0;

for i = 1:stKorakov

    inverzA = inv(A - lambda * eye(size(A)));
    y = inverzA * z;
    z = y / norm(y);
    lambda = z' * A * z;
    if abs(lambda - tarca) < tol
        break;
    end
end
