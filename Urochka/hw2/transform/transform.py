import os
import pandas as pd
import seaborn as sns
from sklearn.linear_model import Lasso, Ridge
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt
import numpy as np

cur_dir = os.path.dirname(os.path.abspath(__file__))
dataset = os.path.join(cur_dir, 'housingprices.csv')

df = pd.read_csv(dataset)
df['Price'] = np.log(df['Price']+1)
df['Miles to Resort'] = np.log(df['Miles to Resort']+1)
df['Square Feet'] = np.log(df['Square Feet']+1)
df['Miles to Base'] = np.log(df['Miles to Base']+1)
df['Acres'] = np.log(df['Acres']+1)
df['Years Old'] = np.log(df['Years Old']+1)
df['DoM'] = np.log(df['DoM']+1)

sm = sns.pairplot(data=df)
sm.savefig(os.path.join(cur_dir, 'sm.png'))

X_train, X_test, y_train, y_test = train_test_split(df[[x for x in df.columns if x != 'Price']], df['Price'],
                                                    test_size=0.3, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

regularization_l = np.arange(0.01, 0.4, 0.001)
regularization_r = np.arange(0.1, 300, 1)
ridge_r2_train = []
ridge_r2_test = []
lasso_r2_train = []
lasso_r2_test = []
ridge_params = []
lasso_params = []
baseline_model = 0

best_model = 0
best_score = -9999999
for l in regularization_l:
    lasso=Lasso(alpha=l)
    lasso.fit(X_train, y_train)
    lasso_r2_train.append(r2_score(y_train, lasso.predict(X_train)))
    lasso_r2_test.append(r2_score(y_test, lasso.predict(X_test)))
    lasso_params.append(lasso.coef_)
    if r2_score(y_test, lasso.predict(X_test)) > best_score:
        best_score = r2_score(y_test, lasso.predict(X_test))
        best_model = lasso

for r in regularization_r:
    ridge=Ridge(alpha=r)
    ridge.fit(X_train, y_train)
    ridge_r2_train.append(r2_score(y_train, ridge.predict(X_train)))
    ridge_r2_test.append(r2_score(y_test, ridge.predict(X_test)))
    ridge_params.append(ridge.coef_)
    if r2_score(y_test, ridge.predict(X_test)) > best_score:
        best_score = r2_score(y_test, ridge.predict(X_test))
        best_model = ridge

plt.close()
plt.plot(regularization_r, ridge_r2_train, 'r', label='ridge train')
plt.plot(regularization_r, ridge_r2_test, 'g', label='ridge test')
plt.plot(regularization_r, np.repeat(baseline_model, regularization_r.size), 'magenta', label='baseline')
plt.xlabel('Regularization strength')
plt.ylabel('R squared')
plt.legend(loc='best')
plt.savefig(os.path.join(cur_dir, 'r2_ridge.png'))

plt.close()
plt.plot(regularization_l, lasso_r2_train, 'r', label='lasso train')
plt.plot(regularization_l, lasso_r2_test, 'g', label='lasso test')
plt.plot(regularization_l, np.repeat(baseline_model, regularization_l.size), 'magenta', label='baseline')
plt.xlabel('Regularization strength')
plt.ylabel('R squared')
plt.legend(loc='best')
plt.savefig(os.path.join(cur_dir, 'r2_lasso.png'))

plt.close()
lasso_params = np.array(lasso_params).T
ridge_params = np.array(ridge_params).T
colors = sns.color_palette(palette='husl', n_colors=ridge.coef_.size)

cols = [x for x in df.columns if x!='Price']
for rp, col, color in zip(ridge_params, cols, colors):
    plt.plot(regularization_r, rp, label=col, color=color)
plt.xlabel('Regularization strength')
plt.ylabel('Parameter value')
plt.legend(loc='best')
plt.savefig(os.path.join(cur_dir, 'ridge_params.png'))

plt.close()
for lp, col, color in zip(lasso_params, cols, colors):
    plt.plot(regularization_l, lp, label=col, color=color)
plt.xlabel('Regularization strength')
plt.ylabel('Parameter value')
plt.legend(loc='best')
plt.savefig(os.path.join(cur_dir, 'lasso_params.png'))

with open(os.path.join(cur_dir, 'results.txt'), 'w') as fout:
    fout.write('The best model is {} \n'.format(best_model))
    fout.write('The best score is {} \n'.format(best_score))
    fout.write('The best params are {} \n'.format(best_model.coef_))
print('The best model is {}, the best score is {}, the best params are {}'.format(best_model, best_score, best_model.coef_))
