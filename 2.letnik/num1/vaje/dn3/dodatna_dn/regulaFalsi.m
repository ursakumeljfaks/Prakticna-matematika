function c = regulaFalsi(f, a, b, tol)

c = (a * f(b) - b * f(a)) / (f(b) - f(a));

while abs(c - a) >= tol && abs(c - b) >= tol
    if f(c) == 0
        break
    elseif f(a) * f(c) < 0
        b = c;
    else
        a = c;
    end
    c = (a * f(b) - b * f(a)) / (f(b) - f(a));
end
c