function [lower upper] = get_conf_int(RSS, X, theta_hat, n, p)
    % ���������� �������� ������� RSS
    degrees_of_freedom = n-p;
    RSS_df = RSS/degrees_of_freedom;
    % ������� ���������� � �������� ������������� ���������
    alpha = 0.05;
    t_quantile = tinv(1-alpha/2, degrees_of_freedom);
    % ������ ��������� ����������, ��������������� ����������
    D = RSS_df * diag(inv(X' * X));
    lower = theta_hat - sqrt(D) .* t_quantile;
    upper = theta_hat +sqrt(D) .* t_quantile;
end
