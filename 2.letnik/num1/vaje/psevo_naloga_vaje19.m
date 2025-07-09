A = [1 1 1 1;
     1 2 3 4;
     2 3 4 5];

[U2,S2,V2] = svd(A)
[V1,S1,U1] = psevdoInverz(A);
A_plus = pinv(A)
