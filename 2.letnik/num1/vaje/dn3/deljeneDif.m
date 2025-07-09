function d = deljeneDif(X, Y)
    n = length(X) - 1;  
    d = zeros(n+1, 1);  
    F = zeros(n+1, n+1);
    F(:, 1) = Y;
    for j = 2:n+1
        for i = j:n+1
            F(i, j) = (F(i, j-1) - F(i-1, j-1)) / (X(i) - X(i-j+1));
        end
    end
    d = diag(F);
end