% ����������� ������
m = 10;
n = 1000;
X = rand(n, m);
b = randn(1, m);
eps = rand(n, 1);
I = ones(n, 1);

z = X * b';
logit = z + eps;
true_prob = sigmoid(z);
threshold = 0.5;
% ���� ����������� > 0.5, �� ���������� �������� ����� 1, ����� ����� 0
true_classes = true_prob > threshold;

% ������������ ������� �������������
initial_beta = ones(m, 1);
options = optimset('GradObj', 'on', 'MaxIter', 50);
[beta_hat, cost] = fminunc(@(t) costfunction(t, X, true_prob), initial_beta, options);
% ������� ������������� �����������
p_hat = predict_proba(beta_hat, X);
logit_hat = X * beta_hat;
% ������ ������ ������ �������� 
plot(abs(true_prob - p_hat));
ylim([0 0.0001]);
xlabel('Object #');
ylabel('|p - p_hat|');
title('The difference between predicted probability and modeled probability');
[b', beta_hat]
