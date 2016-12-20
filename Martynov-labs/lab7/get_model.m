function [X eps theta Y] = get_model(n, p)
    % ���������� ������� X, ����������� ������ � 
    % ������ ���������� ���������
    X = normrnd(0, 1, [n p]);
    eps = normrnd(0, 1, [n 1]);
    theta = normrnd(0, 1, [p 1]);
    % �������� ������-������� ������� Y
    Y = X * theta + eps;
end
