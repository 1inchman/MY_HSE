import os
import seaborn as sns
import pandas as pd
from sklearn.linear_model import Lasso, Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import numpy as np
from matplotlib import pyplot as plt

cur_dir = os.path.dirname(os.path.abspath(__file__))
dataset = os.path.join(cur_dir, 'housingprices.csv')

df = pd.read_csv(dataset)
scatter_matrix = sns.pairplot(data=df)
scatter_matrix.savefig('sm.png')

def filter_condition(x):
    if x == 'Price':
        pass
    else:
        return x

cols = list(filter(filter_condition, df.columns))
print(cols)
target = df['Price']
X = df[cols]
X_train, X_test, y_train, y_test = train_test_split(X, target, test_size=0.3, random_state=42)
scaler = StandardScaler()

baseline_model = np.mean(y_train)

regularization_l = np.arange(0.1, 50, 0.5)
regularization_r = np.arange(0.1, 230, 1)
ridge_rss_train = []
ridge_rss_test = []
lasso_rss_train = []
lasso_rss_test = []
lasso_params = []
ridge_params = []

def get_RSS(y_true, y_pred):
	return np.sum((y_true - y_pred)**2)

for l in regularization_l:
    reg_lasso = Lasso(alpha=l, normalize=True)
    reg_lasso.fit(X_train, y_train)
    lasso_rss_train.append(mean_squared_error(y_train, reg_lasso.predict(X_train)))
    lasso_rss_test.append(mean_squared_error(y_test, reg_lasso.predict(X_test)))
    lasso_params.append(reg_lasso.coef_)

for l in regularization_r:
    reg_ridge = Ridge(alpha=l, normalize=True)
    reg_ridge.fit(X_train, y_train)
    ridge_rss_train.append(mean_squared_error(y_train, reg_ridge.predict(X_train)))
    ridge_rss_test.append(mean_squared_error(y_test, reg_ridge.predict(X_test)))
    ridge_params.append(reg_ridge.coef_)

v_rss_t_base = np.repeat(baseline_model, y_train.size)
v_rss_te_base = np.repeat(baseline_model, y_test.size)
baseline_RSS_train = mean_squared_error(y_train, v_rss_t_base)
baseline_RSS_test = mean_squared_error(y_test, v_rss_te_base)

plt.close()
plt.plot(regularization_r, ridge_rss_train, 'r', label='ridge train')
plt.plot(regularization_r, ridge_rss_test, 'g', label='ridge test')
plt.plot(regularization_r, np.repeat(baseline_RSS_train, regularization_r.size), 'magenta', label='baseline train')
plt.plot(regularization_r, np.repeat(baseline_RSS_test, regularization_r.size), 'cyan', label='baseline test')
plt.xlabel('Regularization strength')
plt.ylabel('Mean squared error')
plt.legend(loc='best')
plt.savefig('rss_ridge.png')

plt.close()
plt.plot(regularization_l, lasso_rss_train, 'r', label='lasso train')
plt.plot(regularization_l, lasso_rss_test, 'g', label='lasso test')
plt.plot(regularization_l, np.repeat(baseline_RSS_train, regularization_l.size), 'magenta', label='baseline train')
plt.plot(regularization_l, np.repeat(baseline_RSS_test, regularization_l.size), 'cyan', label='baseline test')
plt.xlabel('Regularization strength')
plt.ylabel('Mean squared error')
plt.legend(loc='best')
plt.savefig('rss_lasso.png')

plt.close()
lasso_params = np.array(lasso_params).T
ridge_params = np.array(ridge_params).T
for lp, col in zip(lasso_params, cols):
    plt.plot(regularization_l, lp, label=col)

plt.xlabel('Regularization strength')
plt.ylabel('Parameter value')
plt.legend(loc='best')
plt.savefig('Lasso_params.png')

plt.close()
for rp, col in zip(ridge_params, cols):
    plt.plot(regularization_r, rp, label=col)

plt.xlabel('Regularization strength')
plt.ylabel('Parameter value')
plt.legend(loc='best')
plt.savefig('Ridge_params.png')
