import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
plt.rcParams['font.sans-serif'] = ['DFKai-sb'] 
plt.rcParams['axes.unicode_minus'] = False
%config InlineBackend.figure_format = 'retina'
import warnings
warnings.filterwarnings('ignore')

from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris['data'], columns=iris['feature_names'])
df['target'] = iris['target']

X_cols = ['sepal width (cm)', 'petal length (cm)']
y_col = 'target'

X = df[X_cols]
y = df[y_col]

df.plot(kind='scatter', x='sepal width (cm)', y='petal length (cm)', 
        title='沒有目標值的輔助');