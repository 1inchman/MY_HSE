function [J grad] = costfunction(beta, X, y)
    m = length(y);
    J = 1/m * sum(-y.*log(sigmoid(X * beta)) - (1-y).*log(1 - sigmoid(X * beta)));
    grad = 1/m * X' * (sigmoid(X * beta) - y);
    grad = grad(:);
end
