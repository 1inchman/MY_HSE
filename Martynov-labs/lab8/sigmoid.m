function g = sigmoid(z)
    g = exp(z)./(1.0 + exp(z));
end
