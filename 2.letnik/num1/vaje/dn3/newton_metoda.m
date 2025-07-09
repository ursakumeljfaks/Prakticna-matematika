function [x] = newton_metoda(F,JF,x0,maxSteps,tol)
x = x0;
dx = Inf;
for r=1:maxSteps
    if norm(dx) > tol * norm(x)
        dx = -JF(x)\F(x);
        x = x + dx;
    end
end


