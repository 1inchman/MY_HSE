function [lower upper] = get_conf_int(RSS, X, theta_hat, n, p)
    % количество степеней свободы RSS
    degrees_of_freedom = n-p;
    RSS_df = RSS/degrees_of_freedom;
    % уровень надежности и квантиль распределения стьюдента
    alpha = 0.05;
    t_quantile = tinv(1-alpha/2, degrees_of_freedom);
    % оценка дисперсии параметров, векторизованные вычисления
    D = RSS_df * diag(inv(X' * X));
    lower = theta_hat - sqrt(D) .* t_quantile;
    upper = theta_hat +sqrt(D) .* t_quantile;
end
