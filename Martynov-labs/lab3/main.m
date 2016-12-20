clear all;
syms x y z; % зададим переменные интегрирования
fun = @(x, y, z) 2/3 * (x + y + z); % зазадим функцию плотности
p_theory = integral3(fun, 0, 0.7, 0, 0.7, 0, 0.7) % посчитаем численно теоретическую вероятность попасть в куб
dot_counter = 0; % счетчик попаданий
N = 70; % количество экспериментов

for n=1:N
    f = []; % условные плотности
    ksi = []; % точки
    
    % Моделируем
    f = [f int(int(fun,y,0,1),z,0,1)];
    b = solve(int(f(1),x,0,x)-rand,x);
    ksi = [ksi max(double(b))];
  
    f = [f int(subs(fun,x,ksi(1)),z,0,1)/subs(f(1),x,ksi(1))];
    b = solve(int(f(2),y,0,y)-rand,y);
    ksi = [ksi max(double(b))];
    
    f = [f subs(subs(fun,x,ksi(1)),y,ksi(2))/int(subs(subs(fun,x,ksi(1)),y,ksi(2)),z,0,1)];
    b = solve(int(f(3),z,0,z)-rand,z);
    ksi = [ksi max(double(b))];
    
    % Увеличиваем счетчик, если попали
    if (sum(ksi <= 0.7) == 3)
        dot_counter = dot_counter + 1;
    end;
end;
p_experiment = dot_counter/N % экспериментальная вероятность
error = abs(p_experiment - p_theory) % погрешность