n = 100;
t = linspace(0, 1, n);
w = zeros(n, 1);
x = normrnd(0, 1, n);

for i = 1:n-1
  w(i+1) = w(i) + sqrt(t(i+1) - t(i)) * x(i+1);
end

plot(t, w)
