function p = predict_proba(beta, X)
    p = sigmoid(X * beta);
end
