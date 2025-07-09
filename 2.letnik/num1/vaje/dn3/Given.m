function A = Given(A, i, k, smer)
    n = size(A, 1);
    theta = atan2(A(k, i), A(i, i));

    if smer == 0
        c = cos(theta);
        s = sin(theta);

        for j = i:n
            temp1 = c * A(i, j) + s * A(k, j);
            temp2 = -s * A(i, j) + c * A(k, j);
            A(i, j) = temp1;
            A(k, j) = temp2;
            if j > i
                A(k, j) = 0.0;
            end
        end

        A(k, i-1) = 0.0;

    elseif smer == 1
        c = cos(theta);
        s = sin(theta);

        for j = i:n
            temp1 = c * A(j, i) + s * A(j, k);
            temp2 = -s * A(j, i) + c * A(j, k);
            A(j, i) = temp1;
            A(j, k) = temp2;
            if j > i
                A(j, k) = 0.0;
            end
        end

        A(i-1, k) = 0.0;

    end
end
