function J = likelihood(beta, X, y)
    J =  sum(-y.*log(sigmoid(X * beta)) - (1-y).*log(1 - sigmoid(X * beta)));
end
