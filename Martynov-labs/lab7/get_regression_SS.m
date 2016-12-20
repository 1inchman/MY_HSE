function [TSS ESS RSS R_squared] = get_regression_SS(Y, y_hat)
    % ���������� ������� 
    y_mean = mean(Y);
    % ��������������� ����������
    TSS = sum((Y-y_mean).^2);
    ESS = sum((Y-y_mean).^2);
    RSS = sum((Y-y_hat).^2);
    R_squared = 1 - RSS/TSS;
end
