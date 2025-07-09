function v = horner_NP(X, d, t)
    n = length(X) - 1;
    v = d(n+1);
    for i = n:-1:1
        v = v * (t - X(i)) + d(i);
    end
end