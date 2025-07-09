% prva naloga
f = @(x) sin(x);
x = linspace(0,2*pi,4);
y = f(x);

plot(x,y,"o")
hold on

x_risi = linspace(0,2*pi);
y_risi = f(x_risi);

plot(x_risi,y_risi,"b")

p_koef = polyfit(x,y,3);
plot(x_risi, polyval(p_koef,x_risi),"r")

%druga naloga
g = @(x) 1/5 * x.^2 + cos(x.^2).^2;
x_2 = 0:3;
y_2 = g(x_2);

figure
plot(x_2,y_2,"o")
hold on

x_2risi = linspace(0,3);
y_2risi = g(x_2risi);
plot(x_2risi,y_2risi,"b")

p_2koef = polyfit(x_2,y_2,3);
plot(x_2risi, polyval(p_2koef,x_2risi),"r")

% tretja naloga 
