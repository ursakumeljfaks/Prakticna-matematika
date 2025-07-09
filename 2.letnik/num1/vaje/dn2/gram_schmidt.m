function [Q,R] = gram_schmidt(A,tip)
%gram_schmidt je Gram-Schmidtova ortogonalizacija matrike A
%[Q,R] = gram_schmidt(A,tip)
%Q je ortogonalna, R zgornja trikotna
%A je matrika mxn, m>=n, rang(A)=n
%tip = 'cgs' za klasicni Gram-Schmidt
%tip = 'mgs' za modificirani Gram-Schmidt

[m,n] = size(A);
Q = zeros(m,n);
R = zeros(n);

for k=1:n
    Q(:,k) = A(:,k);
    for i=1:k-1
        switch tip
            case 'cgs'
                R(i,k) = Q(:,i)'*A(:,k);
            case 'mgs'
                R(i,k) = Q(:,i)'*Q(:,k);
        end
        Q(:,k) = Q(:,k)-R(i,k)*Q(:,i);
    end
    R(k,k) = norm(Q(:,k),2);
    Q(:,k) = Q(:,k)/R(k,k);
end

end