function rand_num = random_numbers(M, Z_0, P, N)
  Z = zeros(1, N); % преалоцируем место в памяти под точки
  Z(1) = Z_0; % инициализируем стартовую
  % моделируем псевдослучайную последовательность
  for i=2:N
    Z(i) = mod(M * Z(i-1), P);
  end
  normalize_plot(Z, P, N)
end
