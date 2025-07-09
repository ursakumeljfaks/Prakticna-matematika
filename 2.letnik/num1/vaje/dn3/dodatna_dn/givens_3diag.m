function A = givens_3diag(A,i,k, smer)


    if smer == 0
        a = A(i,i-1);
        b = A(k,i-1);
        r = hypot(a,b);
        c = a / r;
        s = b / r;
        A([i,k],:) = [c s; -s c] * A([i,k],:);

    elseif smer == 1
        a = A(i-1, i);
        b = A(i-1, k);
        r = hypot(a,b);
        c = a / r;
        s = b / r;
        A(:,[i, k]) = A(:,[i,k])*[c s; -s c]';
    end
end