% количество строк и столбов в матрице X
n = 500;
p = 10;
% возвращаем сгенерированную модель
[X eps theta Y] = get_model(n, p);

% будем оценивать параметры сгенерированной модели
[theta_hat y_hat] = get_estimates(X, Y);

% графическое сравнение полученных параметров и истинных
figure;
hold on;
plot(theta, 'r');
plot(theta_hat, 'g');
legend('Theta_real', 'Theta_regression');

% посчитаем суммы квадратов отклонений 
[TSS ESS RSS R_squared] = get_regression_SS(Y, y_hat);

[lower upper] = get_conf_int(RSS, X, theta_hat, n, p);
figure;
hold on;
plot(lower, 'r');
plot(upper, 'r');
plot(theta_hat, 'k');
legend('Lower confidence bound', 'Upper confidence bound', 'Theta');
% F-тест
[f_hat f_table] = f_test(n, p);
f_hat
f_table
