function p = predict(beta, X)
    p = predict_proba(beta, X);
    p = p > 0.5;
end
