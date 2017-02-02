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
cur_dir = os.path.dirname(os.path.abspath(__file__))
dataset = os.path.join(cur_dir, 'housingprices.csv')

df = pd.read_csv(dataset)
scatter_matrix = sns.pairplot(data=df)
scatter_matrix.savefig(os.path.join(cur_dir, 'sm.png'))

def filter_condition(x):
    if x == 'Price':
        pass
    else:
        return x

cols = list(filter(filter_condition, df.columns))
print(cols)
target = df['Price']
X = df[cols]
X_train = X.values
y_train = target.values
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

ridge = Ridge(alpha=50.1)
ridge.fit(X_train, y_train)
print(ridge.coef_)
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.3, random_state=42)
print(mean_squared_error(y_test, ridge.predict(X_test)))
