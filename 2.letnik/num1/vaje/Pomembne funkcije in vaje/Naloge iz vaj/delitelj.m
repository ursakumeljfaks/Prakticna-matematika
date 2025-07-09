function seznam = delitelj(stevilo)
% function seznam = delitelj(stevilo)
%
% metoda poisce vse delitelje stevila in vrne seznam

seznam = [];

for i = 1:(stevilo)/2
    if mod(stevilo, i) == 0
        seznam = [seznam, i];
    end
end
seznam = [seznam, stevilo];