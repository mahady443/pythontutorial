'''
What is scikit-learn ?
ans: Simple and efficient tool for data mining and data analysis
built   on Numpy ,Scipy,and Matplotlib
open source and commercially usable BSD licence

what can we achieve from using scikit learn
Classification
    identify the category an object belong to
    Application : spam Detection
Regression:
    predicting and attribute associated with an object
    Application : Stock prices prediction

Clustering
    Automatic gropuing of similar object into sets
    application : Customer segmentation
Model
    compairing validating  and choosing parameter and model
    application : improve model accuaracy via parameter
Dimension reduction
    reducing the number of random variable to consider
    application : to increase model efficiency
pre-processing
    feature extraction and normalization
    application : transforming input data such as text for use with machine learning algorithms


'''
import inline as inline

import numpy as np
import pandas as pd
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from pandas import DataFrame
from sklearn.ensemble import  RandomForestClassifier
from sklearn.svm import SVC
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import SGDClassifier
from  sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from  sklearn.model_selection import train_test_split


# loading dataset
wine= pd.read_csv('winequality-red.csv')

print(wine.head())
print(wine.info())
# Data pre-processing
buns=(2,6.5,8)
group_name=['bad','good']
wine['quality']=pd.cut(wine['quality'],bins=buns,labels=group_name)
print(wine['quality'].unique())
label_quality=LabelEncoder
wine['quality']=label_quality().fit_transform(wine['quality'])
print(wine.head(10))
wine1=wine['quality'].value_counts()
print(wine1)
sns.countplot(wine['quality'])
# plt.show()
# Now separate dataset as response variable and feature variable
X=wine.drop('quality',axis=1)
y=wine['quality']
# train and test data
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
# apply standard scaling to get optimized result
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)
print(X_train[:5])
# TOP 3 MODELS
# **************** Random Forest Classifier ****************
rfc=RandomForestClassifier(n_estimators=200)
rfc.fit(X_train,y_train)
pred_rfc=rfc.predict(X_test)
print(pred_rfc[:20])
# How model Perform
print(classification_report(y_test,pred_rfc))
print(confusion_matrix(y_test,pred_rfc))

# *********Svm Classifier svm= Support vector Matrix***********
clf=svm.SVC()
clf.fit(X_train,y_train)
pred_clf=clf.predict(X_test)
# How model Perform
print(classification_report(y_test,pred_clf))
print(confusion_matrix(y_test,pred_clf))


# *****************Neural Network*****************

mlpc=MLPClassifier(hidden_layer_sizes=(11,11,11),max_iter=500)
mlpc.fit(X_train,y_train)
pred_mlpc=mlpc.predict(X_test)
# How model Perform
print(classification_report(y_test,pred_mlpc))
print(confusion_matrix(y_test,pred_mlpc))

from sklearn.metrics import accuracy_score
cm=accuracy_score(y_test,pred_rfc)
print(cm)




# we can also create new data and predict






