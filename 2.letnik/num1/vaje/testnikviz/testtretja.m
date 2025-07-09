v = [1,1];
for i=3:30
    v(i) = v(i-1) + v(i-2);
end
v;

b = 36;
%30ti stolpec vektorja 1x30
f = v(:,30)+b;
vrednost = 1000/f;