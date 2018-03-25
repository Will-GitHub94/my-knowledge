# Data Preprocessing

'''
	This file is to execute the steps of data preprocessing on a given data set
	The data set is stored in: 'my-knowledge/machine_learning/data_preprocessing/data/Data.csv'
	For the purposes of this file:
		- Independent variables = 'X'
		- Dependent variables = 'Y'
'''

'''
	Importing the libraries
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
''' '''




'''
	Importing the dataset
'''
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values
''' '''




'''
	Handling missing data
'''
from sklearn.preprocessing import Imputer

# Stating that missing values are displayed as 'NaN'
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)

# Populating missing data in columns 1 & 2
imputer = imputer.fit(X[:, 1:3])

# Replace missing data with mean of column
X[:, 1:3] = imputer.transform(X[:, 1:3])
''' '''




'''
	Encoding categorical data
'''
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Instantiation
labelencoder_X = LabelEncoder()

# Encoding first column ('country'):
#   - L29 will encode but data still in 1 column categorised numerically (0, 1, 2)
#   - L30 & L31 will split these categories into seperate columns
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

# Encoding last column (dependent variable - 'purchased'):
#   - Only 2 categories so no need for columns
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
''' '''




'''
	Splitting dataset into Training & Evaluation sets
'''
from sklearn.cross_validation import train_test_split

# Splitting the dependent variables ('X') & the independent ones
X_train, X_eval, Y_train, Y_eval = train_test_split(X, Y, test_size = 0.2, random_state = 0)

'''