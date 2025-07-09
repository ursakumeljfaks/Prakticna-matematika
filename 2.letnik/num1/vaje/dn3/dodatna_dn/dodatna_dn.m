format long

%1.naloga

A = [56.9997    5.4825    5.3692    6.9190    5.9320    5.4825   66.6166   13.4246    6.0367   14.8602    5.3692   13.4246   65.0746    9.1124    10.3721    6.9190    6.0367    9.1124   65.5833    9.4591    5.9320   14.8602   10.3721    9.4591   55.7425];
A = reshape(A,5,5);

%1.1
[X,D] = eig(A);
lastne_vr = diag(D);
r1 = norm(X) + sum(lastne_vr);
%1.2
x = [1;1;1;7;1];
[lambda, z] = potencnaMetoda2(A,x,0.005);
%1.3
[lambda2, z2] = inverznaPotencnaMetoda(A,x,66,5,1e-6);

%2.naloga
B = [56.9997    5.4825    5.2692    6.9190    5.9320    5.4825   65.6166   13.4246    6.0367   14.8602    5.2692   13.4246   65.0746    9.6124    10.3721    6.9190    6.0367    9.6124   65.5833    9.4591    5.9320   14.8602   10.3721    9.4591   57.7425];
B = reshape(B,5,5);

%2.1
M = givens_3diag(B,2,3,0); %3 vrstica 1 element
M(2,1);
%2.2
M = givens_3diag(M, 2, 4, 0); %4 vrstica 1 element
M = givens_3diag(M, 2, 5, 0); %4 vrstica 1 element 
M(2,1);
%2.3
M = givens_3diag(M, 2, 3, 1); %1 vrstica 3 element
M = givens_3diag(M, 2, 4, 1); %1 vrstica 4 element
M = givens_3diag(M, 2, 5, 1); %1 vrstica 5 element
norm(M(1, :));
%2.4
M = givens_3diag(M, 3, 4, 1); %2 vrstica 4 element
M = givens_3diag(M, 3, 5, 1); %2 vrstica 5 element
M = givens_3diag(M, 3, 4, 0); %4 vrstica 2 element
M = givens_3diag(M, 3, 5, 0); %5 vrstica 2 element
M = givens_3diag(M, 4, 5, 0); %5 vrstica 3 element
M = givens_3diag(M, 4, 5, 1); %3 vrstica 5 element
min(diag(M));


%3.naloga
f = @(x) x.^2 + 2.2400 * cos(x + 0.01) - 5 + 1/10 * sin(5.000.*x);
df = @(x) 2.*x - 2.2400 * sin(x + 0.01) + 5.000/10 * cos(5.000.*x);

%3.1
nicla1 = tangMetoda(f,df,3,100);
nicla2 = tangMetoda(f,df,-3,100);
vsota = nicla1+nicla2;
%fplot(f)
%3.2
c = metodaBisekcije(f,0,4,10^(-2));
f(c);
%3.3
d = regulaFalsi(f,-4,0,10^(-3));

