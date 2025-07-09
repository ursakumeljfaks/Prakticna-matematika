% vrne koeficiente polinoma, ki ima ničli 1 in 2
coeffs = poly(1:2); 
% vrne ničle polinoma s koeficienti 1 -3 2 (to so koeficienti od prej)
% (x-1)(x-2) = x^2-3x+2
roots(coeffs);
n = 20;
koef = poly(1:n);

x = linspace(1,n);
y = polyval(koef, x);
plot(x, y, 'linewidth', 1);
hold on
plot(1:n, zeros(1,n), 'o');

zmoten = koef;
zmoten(2) = zmoten(2) + 2^-23;
r = roots(zmoten);
m = roots(koef);
