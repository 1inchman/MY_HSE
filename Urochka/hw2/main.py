import os
import seaborn as sns
import pandas as pd
from sklearn.linear_model import Lasso, Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
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
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

regularization = np.arange(0.1, 100, 0.5)
ridge_rss_train = []
ridge_rss_test = []
lasso_rss_train = []
lasso_rss_test = []
lasso_params = []
ridge_params = []
for l in regularization:
    reg_lasso = Lasso(alpha=l)
    reg_ridge = Ridge(alpha=l)
    reg_lasso.fit(X_train, y_train)
    reg_ridge.fit(X_train, y_train)
    ridge_rss_train.append(np.sum((y_train-reg_ridge.predict(X_train))**2))
    ridge_rss_test.append(np.sum((y_test-reg_ridge.predict(X_test))**2))
    lasso_rss_train.append(np.sum((y_train-reg_lasso.predict(X_train))**2))
    lasso_rss_test.append(np.sum((y_test-reg_lasso.predict(X_test))**2))
    lasso_params.append(reg_lasso.coef_)
    ridge_params.append(reg_ridge.coef_)

plt.close()
plt.plot(regularization, ridge_rss_train, 'r', label='ridge train')
plt.plot(regularization, ridge_rss_test, 'g', label='ridge test')
plt.plot(regularization, lasso_rss_train, 'b', label='lasso train')
plt.plot(regularization, lasso_rss_test, 'magenta', label='lasso test')
plt.xlabel('Regularization strength')
plt.ylabel('Residual sum of squares')
plt.legend(loc='best')
plt.savefig('rss.png')

plt.close()
lasso_params = np.array(lasso_params).T
ridge_params = np.array(ridge_params).T
for lp, col in zip(lasso_params, cols):
    plt.plot(regularization, lp, label=col)

plt.xlabel('Regularization strength')
plt.ylabel('Parameter value')
plt.legend(loc='best')
plt.savefig('Lasso_params.png')

plt.close()
for rp, col in zip(ridge_params, cols):
    plt.plot(regularization, rp, label=col)

plt.xlabel('Regularization strength')
plt.ylabel('Parameter value')
plt.legend(loc='best')
plt.savefig('Ridge_params.png')
