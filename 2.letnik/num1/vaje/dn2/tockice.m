format long
mojaTabla = load('tocke.mat');
mojaTabla = mojaTabla.tocke;

A = [mojaTabla(:,1).^2 mojaTabla(:,2).^2 mojaTabla(:,3).^2];
druga_norma = norm(A);
b = ones(length(mojaTabla(:,1)),1);

[Q,R,bt] = Givens(A,b);
%rabim kvadratno matriko R 3x3
R1 = R(1:length(R(1,:)),:);
%bt1 = Q'b
bt1 = bt(1:3,1);
%bt2 = Q1'b
bt2 = bt(4:length(bt),1);
x = obratnaSub(R1,bt1); %lahko tudi x = R1\bt1
a1 = sqrt(1./x);
a = a1(1);
b = a1(2);
c = a1(3);

plot3(mojaTabla(:,1), mojaTabla(:,2), mojaTabla(:,3));

%izracunana sled matrike R
[Q1,R1] = gram_schmidt(A,"mgs");
sled = 0;
[m,n] = size(R1);
for i=1:m
    for j=1:n
        if i == j
            sled = sled + R1(i,j);
        end
    end
end
sled;

%narisan graf v parametrizairani obliki
s = linspace(-pi/2,pi/2,30);
t = linspace(-pi,pi,30);
[S,T] = meshgrid(s,t);
X = a.*cos(S).*cos(T);
Y = b.*cos(S).*sin(T);
Z = c.*sin(S);
surf(X,Y,Z)

X1 = reshape(X,900,1);
Y1 = reshape(Y,900,1);
Z1 = reshape(Z,900,1);

F = [X1 Y1 Z1];
razdalja1A = [mojaTabla(1,1) mojaTabla(1,2) mojaTabla(1,3)];
razdalja1F = [F(1,1) F(1,2) F(1,3)];
najmanjsa = abs(norm(razdalja1F-razdalja1A));
for i=1:length(F)
    razdalja = abs(norm([F(i,1) F(i,2) F(i,3)]-razdalja1A));
    if razdalja < najmanjsa
        najmanjsa = razdalja;
    end
end
najmanjsa
  

    
