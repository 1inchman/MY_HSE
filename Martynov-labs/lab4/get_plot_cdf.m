function none = get_plot_cdf(n, dim)
    wiener_zeros = zeros(1, n); % преалоцируем пам€ть под нули
    % тыс€чу раз генерируем винеровский процесс размерности n
    % после чего находим наибольший нуль
    for j=1:1000
        [t w] = get_wiener(n, dim);
        for i=length(w):-1:2
            if (w(i)*w(i-1)<=0)
                wiener_zeros(j) = i/n; % сохран€ем нуль
                break; % прекращаем поиск, так как наиб. нуль найден
            end
        end
    end
    % считаем ecdf
    [y, x] = ecdf(wiener_zeros);
    figure;
    plot(x, y);
    grid on;
    hold on;
    % сравниваем с теоретической функцией
    plot(t, 2/pi * asin(sqrt(t)));
    legend('Experiment cdf', 'Theoretical cdf');
    title('Cumulative density functions');
end
