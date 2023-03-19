'''
NO1. Tensorflow
    1. Library for high performance numerical Computation
    2. Used most scientific domain
In Tensorflow data is represented as tensor which is multidimensional array.
Tensorflow feature
1. most common used in Deep learning ,Machine learning
2.Better Computational Visualization Graph
3.In neural machine translation reduces error by 50-60%
4. parallel computing to execute complex models

Tensorflow Application
1. Speech and image reorganization
2.Text Based Application
3. Time Series and forcasting
4. Video Detection


N0.2 Numpy
    1. Stand for Numerical analysis
    2. General purpose Array-Preprocessing package

Numpy is the fundamental package for numerical computation for python , it contains a powerful N-dimensional array object

feature of Numpy
1. Provide fast precompiled function for numerical routing
2. Array oriented computing for Better Efficiency
3. Supports Object-Oriented Approach
4. Compact & Faster Computations with vectorization

Numpy Application
1.Extensively in Data Analysis
2. Creating Powerful N-Dimensional arry
3. Forms the base of other libraries like scipy,scikit-learn
4. replacement of matlab when used with scipy , matplotlib


NO3. SCIPY
    1. Stands For Scientific Python
    2. Used for Scientific And Technical Computation
it provides many user friendly and efficient routines scientific computation ,it extends Numpy

feature of Scipy
1. A collection of mathematical algorithms and scientific functions built on the numpy extension of python
2. high level commands and classes for manipulating and visualizing data
3. Multi dimensional image processing with scipy.ndimage
4. Includes Functions for computing integrals numerically solving differential equation optimization etc

Application of SCIPY
1.Multi-Dimension image operations
2. Solving Diffential equation and fourier transform
3.optimization algorithms
4. linear Algebra

No4. PANDAS
    Stands For Python data analysis library
    used for data analysis and cleaning
it provides fast flexible and expressive dara structure designed to work with stuctured data easyly and intutivity

Feature of pandas
1. Elowuent syntax and rich function
2.apply()enables you to run a fuctiion across a serires of data
3. High level abstraction
4. contains high level data structure and mauplating tools

application of pandas
1.general data wrangling
2.etl jobs and dara storage
3. used in a wide variety of academic and commercial domains including statistic
4.time series specific functionality

No5. Matplotlib
    1. plotiting library for python
    2. used for data visualization
it provides an object oriented api for embedding plot in application

feature of matplotlib
1. as usable as matlab with an advantage of being free and open source
2.support dozen of backend and output types
3.pandas can used as itself in matplotlib api
4. Smaller memory consumption and better runtime behaviour

application
1.correlation analysis of variable
2.visualize 95% confidence interval of the models
3.outler detection
4.visualtization distrubing to gain instant insights
'''
import random

#numpy example
import numpy as np
a=np.array([1,2,3]) # create array
print(type(a))
print(a.shape)
b= np.arange(12) # range array
print(b)
bmatrix=b.reshape(3,4) # format as matrix
print(bmatrix)   # or b= np.arange(12).reshape(3,4)

# ******* Example of pandas ********
import pandas as pd
df=pd.DataFrame(np.random.randn(6,4),index=list(range(6)),columns=list('ABCD'))
print(df.describe())

import matplotlib.pyplot as plt
'''
np.random.seed(30)
N=30
x=np.random.rand(N)
y=np.random.rand(N)
color= np.random.rand(N)
area= (30 * np.random.rand(N))**2
plt.scatter(x,y,s=area,c=color,alpha=0.4)
print(plt.show())
'''
# At a time one can run
from matplotlib import style
style.use('ggplot')
x=[2,4,6]
y=[12,14,16]
x2=[3,3,4]
y2=[7,14,5]
plt.bar(x,y,color='r',align='center')
plt.bar(x2,y2,color='b',align='center')
plt.title('Info')
plt.ylabel('Y axix')
plt.xlabel('X axix')
print(plt.show())





