function [X eps theta Y] = get_model(n, p)
    % Генерируем матрицу X, гауссовские ошибки и 
    % вектор параметров регрессии
    X = normrnd(0, 1, [n p]);
    eps = normrnd(0, 1, [n 1]);
    theta = normrnd(0, 1, [p 1]);
    % получаем вектор-столбец ответов Y
    Y = X * theta + eps;
end
