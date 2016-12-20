n = 1000;

mu = 5;
sigma = 1;
x = 0:10/n:(10-1/n);
h = 1/sqrt(n);
% ГїГ¤Г°Г® ГЈГ ГіГ±Г±Г 
K = @(y) 1/sqrt(2*pi) * exp(-y^2/2);
% ГЈГҐГ­ГҐГ°ГЁГ°ГіГҐГ¬ ГўГ»ГЎГ®Г°ГЄГі
X = randn([1 n]) * sigma + mu;
f_experiment = zeros(1, n);
% ГЋГ¶ГҐГ­ГЄГ  ГЏГ Г°Г§ГҐГ­Г -ГђГ®Г§ГҐГ­ГЎГ«Г ГІГІГ 
for i =1:n
    sum = 0;
    for j=1:n
        sum = sum + K((x(i) - X(j))/h);
    end
    i
    f_experiment(i) = sum/(n*h);
end
hold on;
plot(x, f_experiment, 'r');

f_theory = @(x) 1/(sigma * sqrt(2*pi)) * exp(-(x - mu).^2/(2*sigma^2));
plot(x, f_theory(x));
legend('Experiment', 'Theory');
figure;
plot(x, f_experiment, 'r');
hold on;
plot(x, normpdf(x, mu, sigma));
legend('Experiment', 'Matlab built-in');


%РґСЂСѓРіРѕРµ h_n
h = 7/sqrt(n);

for i =1:n
    sum = 0;
    for j=1:n
        sum = sum + K((x(i) - X(j))/h);
    end
    f_experiment(i) = sum/(n*h);
end
figure;
hold on;
plot(x, f_experiment, 'r');

f_theory = @(x) 1/(sigma * sqrt(2*pi)) * exp(-(x - mu).^2/(2*sigma^2));
plot(x, f_theory(x));
legend('Experiment', 'Theory');
figure;
plot(x, f_experiment, 'r');
hold on;
plot(x, normpdf(x, mu, sigma));
legend('Experiment', 'Matlab built-in');
