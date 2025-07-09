%2_naloga_dn
format long

f = @(x, b) b - 1 + x*cos(x) + sin(x+b) - 4*cos(2*x) + 5*sin(2*x);
b = 4/20;
xL = 0;
xU = 2*pi;
x1 = 0;
x2 = pi/2;
x3 = pi;
x4 = 5*pi/3;
x5 = 2*pi;

fplot(@(x) f(x,b), [xL,xU])
grid on



nicla1 = fzero(@(x)f(x,b),x1)
nicla2 = fzero(@(x)f(x,b),x2)
nicla3 = fzero(@(x)f(x,b),x3)
nicla4 = fzero(@(x)f(x,b),x4)
nicla5 = fzero(@(x)f(x,b),x5)

