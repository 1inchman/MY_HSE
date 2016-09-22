function rand_num = random_numbers()
  global rand_num;
  P = 10;
  M = 6;
  C = 3;
  rand_num = mod(M * rand_num + C, P);
end
