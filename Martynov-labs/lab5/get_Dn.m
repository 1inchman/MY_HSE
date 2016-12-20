function none = get_Dn(n)
    % ������������ ������
    Dn = zeros(1, n);
    D = zeros(1, n);
    % ��������� �������� Dn
    for j=1:n
        Fx = sort(rand(1, n));
        for i=1:n
            D(i) = sqrt(n) * max(i/n - Fx(i), Fx(i) - (i-1)/n);
        end
        Dn(j) = max(D);
    end

    Dn = sort(Dn);
    % �������� ������������
    Dn_quantile = Dn(0.9*n)
    % ����������� �� ��������� � ������������� ���������
    error = abs(Dn_quantile - 1.23)
    % �������� ������������
    Dn_quantile = Dn(0.95*n)
    % �����������
    error = abs(Dn_quantile - 1.36)
end
