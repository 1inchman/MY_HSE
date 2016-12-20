function none = get_Dn(n)
    % преалоцируем память
    Dn = zeros(1, n);
    D = zeros(1, n);
    % посчитаем значения Dn
    for j=1:n
        Fx = sort(rand(1, n));
        for i=1:n
            D(i) = sqrt(n) * max(i/n - Fx(i), Fx(i) - (i-1)/n);
        end
        Dn(j) = max(D);
    end

    Dn = sort(Dn);
    % квантиль эксперимента
    Dn_quantile = Dn(0.9*n)
    % погрешность по сравнению с теоретической квантилью
    error = abs(Dn_quantile - 1.23)
    % квантиль эксперимента
    Dn_quantile = Dn(0.95*n)
    % погрешность
    error = abs(Dn_quantile - 1.36)
end
