import numpy as np

def get_stat_value(x_vec, y_vec):
    return (x_vec+y_vec)@np.log((x_vec+y_vec)/np.sum(x_vec+y_vec)) - (x_vec@np.log(x_vec/np.sum(x_vec)) + y_vec@np.log(y_vec/np.sum(y_vec)))

x = np.array([4782869, 1869615, 907564, 93048, 56154])
y = np.array([5188154, 1034165, 210927, 131377, 90280])

p = x/np.sum(x)
q = y/np.sum(y)
K = 5000
alpha_0 = 0.01

cur_state = np.random.get_state()
np.random.seed(100)

stat_val = []

sample_x = np.random.multinomial(np.sum(x), p, size=K)
sample_y = np.random.multinomial(np.sum(y), p, size=K)

for si in range(K):
    stat_val.append(get_stat_value(sample_x[si], sample_y[si]))

stat_val.sort()
t_alpha = stat_val[int(K*(1-alpha_0))]
stat_real = get_stat_value(x, y)
print(t_alpha)
print(stat_real)
