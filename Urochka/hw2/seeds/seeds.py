import os
import seaborn as sns
import pandas as pd
from sklearn.linear_model import Lasso, Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
import numpy as np
from matplotlib import pyplot as plt

mean_squared_error = r2_score
for seed in [3, 666, 97, 32]:
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    dataset = os.path.join(cur_dir, 'housingprices.csv')

    df = pd.read_csv(dataset)
    scatter_matrix = sns.pairplot(data=df)
    scatter_matrix.savefig(os.path.join(cur_dir, 'sm{}.png'.format(seed)))

    def filter_condition(x):
        if x == 'Price':
            pass
        else:
            return x

    cols = list(filter(filter_condition, df.columns))
    print(cols)
    target = df['Price']
    X = df[cols]
    X_train, X_test, y_train, y_test = train_test_split(X, target, test_size=0.3, random_state=seed)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    baseline_model = 0

    regularization_l = np.arange(0.1, 150, 0.1)
    regularization_r = np.arange(0.1, 300, 1)
    ridge_rss_train = []
    ridge_rss_test = []
    lasso_rss_train = []
    lasso_rss_test = []
    lasso_params = []
    ridge_params = []


    best_model = 0
    best_score = -999999
    for l in regularization_l:
        reg_lasso = Lasso(alpha=l)
        reg_lasso.fit(X_train, y_train)
        lasso_rss_train.append(mean_squared_error(y_train, reg_lasso.predict(X_train)))
        lasso_rss_test.append(mean_squared_error(y_test, reg_lasso.predict(X_test)))
        lasso_params.append(reg_lasso.coef_)
        if mean_squared_error(y_test, reg_lasso.predict(X_test)) > best_score:
            best_score = mean_squared_error(y_test, reg_lasso.predict(X_test))
            best_model = reg_lasso

    for l in regularization_r:
        reg_ridge = Ridge(alpha=l)
        reg_ridge.fit(X_train, y_train)
        ridge_rss_train.append(mean_squared_error(y_train, reg_ridge.predict(X_train)))
        ridge_rss_test.append(mean_squared_error(y_test, reg_ridge.predict(X_test)))
        ridge_params.append(reg_ridge.coef_)
        if mean_squared_error(y_test, reg_ridge.predict(X_test)) > best_score:
            best_score = mean_squared_error(y_test, reg_ridge.predict(X_test))
            best_model = reg_ridge


    plt.close()
    plt.plot(regularization_r, ridge_rss_train, 'r', label='ridge train')
    plt.plot(regularization_r, ridge_rss_test, 'g', label='ridge test')
    plt.plot(regularization_r, np.repeat(baseline_model, regularization_r.size), 'magenta', label='baseline')
    plt.xlabel('Regularization strength')
    plt.ylabel('R squared')
    plt.legend(loc='best')
    plt.savefig(os.path.join(cur_dir, 'rss_ridge{}.png'.format(seed)))

    plt.close()
    plt.plot(regularization_l, lasso_rss_train, 'r', label='lasso train')
    plt.plot(regularization_l, lasso_rss_test, 'g', label='lasso test')
    plt.plot(regularization_l, np.repeat(baseline_model, regularization_l.size), 'magenta', label='baseline')
    plt.xlabel('Regularization strength')
    plt.ylabel('R squared')
    plt.legend(loc='best')
    plt.savefig(os.path.join(cur_dir, 'rss_lasso{}.png'.format(seed)))

    plt.close()
    lasso_params = np.array(lasso_params).T
    ridge_params = np.array(ridge_params).T
    colors = sns.color_palette(palette='husl', n_colors=reg_ridge.coef_.size)
    for lp, col, color in zip(lasso_params, cols, colors):
        plt.plot(regularization_l, lp, label=col, color=color)

    plt.xlabel('Regularization strength')
    plt.ylabel('Parameter value')
    plt.legend(loc='best')
    plt.savefig(os.path.join(cur_dir, 'Lasso_params{}.png'.format(seed)))

    plt.close()
    for rp, col, color in zip(ridge_params, cols, colors):
        plt.plot(regularization_r, rp, label=col, color=color)

    plt.xlabel('Regularization strength')
    plt.ylabel('Parameter value')
    plt.legend(loc='best')
    plt.savefig(os.path.join(cur_dir, 'Ridge_params{}.png'.format(seed)))
    plt.close()

    with open(os.path.join(cur_dir, 'results{}.txt'.format(seed)), 'w') as fout:
        fout.write('The best model is {} \n'.format(best_model))
        fout.write('The best score is {} \n'.format(best_score))
        fout.write('The best params are {} \n'.format(best_model.coef_))
    print('The best model is {}, the best score is {}, the best params are {}'.format(best_model, best_score, best_model.coef_))
