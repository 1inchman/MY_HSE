n_experiments = 100000; % число бросков иглы

hits = 0; % счетчик попаданий за границы
% моделирвоание экспериментов
for i = 1:n_experiments
  hits = hits + throw_needle();
end

p_experiment = hits/n_experiments
p_theory = 2/pi
