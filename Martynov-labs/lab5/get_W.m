function none = get_W(n)
    % ������������ ������
    W = zeros(1, n);
    % ��������� �������� W
    for j=1:n
        x = sort(rand(1,n));
        for i=1:n
            W(j) = W(j) + (x(i) - (2*i-1)/(2*n))^2;
        end
        W(j) = W(j) + 1/(12*n);
    end
    W = sort(W);
    % �������� ������������ � ����������� �� ��������� � �������������
    W_quantile = W(0.9*n)
    error = abs(W_quantile - 0.35)
    % �������� ������������ � �����������
    W_quantile = W(0.95*n)
    error = abs(W_quantile - 0.46)
end
