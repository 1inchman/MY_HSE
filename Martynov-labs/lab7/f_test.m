function [f_experiment f_theory] = f_test(n, p)
    % последние к параметров
    q = 4;
    count=0;
    n_exp = 100;
    for i=1:n_exp
       [X eps theta Y] = get_model(n, p);
       [theta_hat y_hat] = get_estimates(X, Y);

       X_zero = X(1:end, 1:p-q+1);
       theta_zero = theta(1:p-q+1);
       Y_zero = X_zero * theta_zero + eps;
       [theta_hat_zero y_hat_zero] = get_estimates(X_zero, Y_zero);
       [TSS ESS RSS R_squared] = get_regression_SS(Y, y_hat);
       [TSS_zero ESS_zero RSS_zero R_sq_zero] = get_regression_SS(Y_zero, y_hat_zero);
       % F-тест
       f_experiment = ((RSS_zero - RSS)/(q+1))/(RSS/(n-p));
       f_theory = finv(0.95, q+1, n-p);
       if f_experiment<f_theory
           count = count + 1;
       end
   end
   count/n_exp
   end
