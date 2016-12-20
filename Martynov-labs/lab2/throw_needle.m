function didhit = throw_needle()
  needle_length = 1; % длина иглы
  xcoord = needle_length * rand(); % моделирование броска иглы, центр иглы находится в этой точке после падения
  angle = 2*pi * rand(); % моделирование угла иглы после падения
  % Проецируем иглу на другую ось. Если центр+проекция/2 больше 1 или центр+проекция/2 меньше 0, значит ушли за границы
  projection = abs(needle_length/2 * sin(angle));
  if ((xcoord + projection) > needle_length) || ((xcoord - projection) < 0)
    didhit = 1;
  else
    didhit = 0;
  end
end
