function x = tangMetoda(f, df, x, stKorakov)

for i=1:stKorakov
    x = x - f(x)/df(x);
end