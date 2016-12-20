function [theta_hat y_hat] = get_estimates(X, y)
    theta_hat = inv(X' * X) * X' * y;
    y_hat = X * theta_hat;
end
