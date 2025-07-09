A = [1 274 850;
     1 180 1120;
     1 375 740;
     1 205 970;
     1 86 1032];
y = [162;120;223;131;67];
B = A'*A;

%z LU razcepom
[L,U] = luRazcep(B);
b = premaSub(L,A'*y);
rezultat = obratnaSub(U,b);
resitev = [1 60 1050]*rezultat;

%z razcepom Choleskega
% V predstavlja v resnici V transponirano
V_t = chol(B)
V = V_t'
b2 = premaSub(V,A'*y) 
rezultat2 = obratnaSub(V', b2)
resitev2 = [1 60 1050]*rezultat2