function [A_plus] = psevdoInverz(A)
   [U,S,V] = svd(A);
   S1 = eye(size(S));
   n = size(S)
   for i=1:n
      if S(i,i) ~= 0
        S1(i,i) = 1./diag(S);
   end
   A_plus = V'*S1*U'


