
f1 = @(x,y) x.^2-y.^2-1+2/3*cos(x.*y)+y.^3;
f2 = @(x,y)  x.^2-y.^2-1+2/3*cos(x.*y);
fimplicit(f1)
hold on
fimplicit(f2)

F = @(x) [f1(x(1),x(2)); f2(x(1),x(2))];

JF = @(x) [2*x(1) - 2/3*sin(x(1).*x(2)).*x(2),  2*x(2) - 2/3*sin(x(1).*x(2))*x(1) + 3*x(2).^2;
           2*x(1) - 2/3*sin(x(1).*x(2)).*x(2),  2*x(2) - 2/3*sin(x(1).*x(2))*x(1)];
x0 = [0.5;0.5];
x = newton_metoda(F,JF,x0,10,1e-5);
plot(x(1),x(2),"o");
x = fsolve(F,x0);


y = [2 7 7 16 16 31 57 89 141 181 219 253 275 275 286 341 383 414 442 480 528 562 632 684 730 756 802 841 897].';
x2 = [1:29].';
x3 = [ones(length(x2),1) x2];

% iskanje zacetnega priblizka
y2 = log(y);
a = x3\y2;
rez_a = exp(a(1));
rez_b = a(2);

f3 = @(koef) koef(1)*exp(koef(2)*x);
JF = @(koef) [exp(koef(2)*xP), koef(1) * xP .* exp(koef(2)*xP)];


