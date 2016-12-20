function none = get_plot_cdf(n, dim)
    wiener_zeros = zeros(1, n); % ������������ ������ ��� ����
    % ������ ��� ���������� ����������� ������� ����������� n
    % ����� ���� ������� ���������� ����
    for j=1:1000
        [t w] = get_wiener(n, dim);
        for i=length(w):-1:2
            if (w(i)*w(i-1)<=0)
                wiener_zeros(j) = i/n; % ��������� ����
                break; % ���������� �����, ��� ��� ����. ���� ������
            end
        end
    end
    % ������� ecdf
    [y, x] = ecdf(wiener_zeros);
    figure;
    plot(x, y);
    grid on;
    hold on;
    % ���������� � ������������� ��������
    plot(t, 2/pi * asin(sqrt(t)));
    legend('Experiment cdf', 'Theoretical cdf');
    title('Cumulative density functions');
end
