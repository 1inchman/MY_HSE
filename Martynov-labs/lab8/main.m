% сгенерируем модель
p = 5;
n = 1000;
X = rand(n, p);
beta = [0.9 0.5 0.3 -0.9 0.2];
I = ones(n, 1);

g = X*beta';
true_prob = sigmoid(g);
Y = rand(n,1)<true_prob;

% оптимизируем функцию правдоподобия
f = @(b) likelihood(b, X, Y);
beta_hat = fminsearch(f, [1; 1; 1; 1; 1]);
% считаем предсказанные вероятности
g_hat = X * beta_hat;
prob_hat = predict_proba(beta_hat, X);
% строим график модуля разности
plot(true_prob, 'or');
hold on;
plot(prob_hat, '*b');
[beta', beta_hat]
