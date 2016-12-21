% ����������� ������
p = 5;
n = 1000;
X = rand(n, p);
beta = [0.9 0.5 0.3 -0.9 0.2];
I = ones(n, 1);

g = X*beta';
true_prob = sigmoid(g);
Y = rand(n,1)<true_prob;

% ������������ ������� �������������
f = @(b) likelihood(b, X, Y);
beta_hat = fminsearch(f, [1; 1; 1; 1; 1]);
% ������� ������������� �����������
g_hat = X * beta_hat;
prob_hat = predict_proba(beta_hat, X);
% ������ ������ ������ ��������
plot(true_prob, 'or');
hold on;
plot(prob_hat, '*b');
[beta', beta_hat]
