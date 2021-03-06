# -*- coding: utf-8 -*-
"""Task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bW9WbPaYQ1WRDM6xdVsoC1t8aXQE2yZK
"""

# Commented out IPython magic to ensure Python compatibility.
#importing the required libraries
import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
iris=load_iris()
iris.data

iris.feature_names

iris.target

df=pd.DataFrame(iris.data, columns=iris.feature_names)
df.head()

df.shape

df['target']=iris.target
df.head()

sns.pairplot(df)

sns.heatmap(df.corr(), annot= True)

sns.scatterplot(x= 'petal width (cm)', y= 'petal length (cm)', data=df)

df.isnull().sum()

from sklearn.model_selection import train_test_split
X = df.drop('target',axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier()
dtree.fit(X_train,y_train)
predictions = dtree.predict(X_test)

from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(y_test,predictions))

print(confusion_matrix(y_test,predictions))

from sklearn import tree
feat_names=['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)']
classes=['setosa', 'versicolor', 'virginica']

fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=300)
tree.plot_tree(dtree,
               feature_names = feat_names, 
               class_names=classes,
               filled = True);