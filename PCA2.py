import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None)
x, y = df.iloc[:, 1:].values, df.iloc[:, 0].values
sc = StandardScaler()
x = sc.fit_transform(x)
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
x_pca = pca.fit_transform(x)

import matplotlib.pyplot as plt

plt.scatter(x_pca[y==1, 0], x_pca[y==1, 1], color='red', marker='^', alpha=0.5)
plt.scatter(x_pca[y==2, 0], x_pca[y==2, 1], color='blue', marker='o', alpha=0.5)
plt.scatter(x_pca[y==3, 0], x_pca[y==3, 1], color='lightgreen', marker='s', alpha=0.5)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.show()
