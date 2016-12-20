function [w t] = calc_wiener(n)
    t = linspace(0, 1, n); % ������� �����
    w = zeros(1, n); % ������������ ������ ��� �������� ��������
    x = normrnd(0, 1, [1 n]); % ��������� �������������� ����
    % ������ ���� ���������
    for i = 1:n-1
        w(i+1) = w(i) + sqrt(1/n) * x(i);
    end
end
