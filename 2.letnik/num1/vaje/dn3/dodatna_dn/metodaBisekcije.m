function c = metodaBisekcije(f,a,b,tol)

while abs(a-b) >= tol
    c = (a + b) / 2;
    if f(a) * f(c) < 0
        b = c;
    elseif f(b) * f(c) < 0 
        a = c;
    else
        break;
    end
end
c