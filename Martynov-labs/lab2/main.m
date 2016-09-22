n_experiments = 10000;

hits = 0;
for i = 1:n_experiments
  hits = hits + throw_needle();
end

printf("The probability estimated is %f\n", hits/n_experiments)
printf("The true probability is %f\n", 2/pi)
