#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sklearn import svm
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml


# In[4]:


mnist = fetch_openml('Mnist_784')
x = mnist['data']
y = mnist['target']
x.shape


# In[7]:


shuffle_index = np.random.permutation(70000)
x, y = x[shuffle_index], y[shuffle_index]
x_train, x_test = x[0:60000], x[60000:70000]
y_train, y_test = y[0:60000], y[60000:70000]
x_train = x_train.astype(np.int8)
y_train = y_train.astype(np.int8)
x_test = x_test.astype(np.int8)
y_test = y_test.astype(np.int8)
model = svm.SVC(kernel='rbf')
model.fit(x_train, y_train)
predictions = model.predict(x_test)

print("Accuracy is", metrics.accuracy_score(y_test, predictions))


# In[8]:


for i in range(0,20):

              digit=x_test[i]

              digit_image=digit.reshape(28,28)

              print('Actual Value :', y_test[i])

              plt.imshow(digit_image)

              plt.show()

              print('Value of Predicted Model:', predictions[i])


# In[ ]:




