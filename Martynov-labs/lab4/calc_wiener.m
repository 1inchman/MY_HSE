function [w t] = calc_wiener(n)
    t = linspace(0, 1, n); % зададим время
    w = zeros(1, n); % преалоцируем память под значения процесса
    x = normrnd(0, 1, [1 n]); % нормально распределенные шаги
    % теперь сама генерация
    for i = 1:n-1
        w(i+1) = w(i) + sqrt(1/n) * x(i);
    end
end
