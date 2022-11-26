import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import export_graphviz

df = pd.read_csv("dataset_website.csv")
print(df.head())

df = np.array(df)

X = df[:, :-1]
y = df[:, -1]

y = y.astype('int')
X = X.astype('int')


Xtrain, Xtest, ytrain, ytest = train_test_split(X, y,test_size=2, random_state=0)

model = DecisionTreeClassifier()
model.fit(Xtrain, ytrain)
x = model.predict(Xtest)
y = model.predict(Xtrain)

pickle.dump(model, open("ml.pkl","wb"))
model=pickle.load(open('ml.pkl','rb'))

