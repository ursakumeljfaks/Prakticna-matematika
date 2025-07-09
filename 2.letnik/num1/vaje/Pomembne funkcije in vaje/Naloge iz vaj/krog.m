%ustvarimo metodo
function [obseg, ploscina] = krog(radij)
% function [obseg, ploscina] = krog(radij)
% funkcija izračuna obseg in ploščino kroga za vhodni parameter radij

obseg = 2*pi*radij;
ploscina = pi*radij^2;

%for zanka 5x izpiše besedo Zanka
for i = 1:5
    disp(['Zanka ', i])
end

%seštejemo prvih 10 števil s for
vsota=0;
for i = 1:10
    vsota = vsota + i;
end
vsota

%seštejemo prvih 10 števil z while
vsota2=0;
ind=1;
while ind <= 10  
    vsota2 = vsota2 + ind;
    ind = ind+1;
end
vsota2

%if stavek
vrednost = 5;
if vrednost > 0
    vrednost = vrednost*2;
elseif vrednost > -2
    vrednost = 0;
else
    vrednost = -vrednost;
end
vrednost