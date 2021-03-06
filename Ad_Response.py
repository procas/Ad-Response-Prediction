import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from matplotlib.colors import ListedColormap
from matplotlib.colors import ListedColormap
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.cross_validation import train_test_split
import seaborn as sns

# Importing the dataset
dataset = pd.read_csv('Dcl_Dgp_Ads.csv')
X = dataset.iloc[:, [2, 3]].values #independent values
y = dataset.iloc[:, 4].values #dependent value


## Preprocessing: Cleaning the dataset

# Imputer with strategy - mean
                   
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0) #recognises missing values
imputer = imputer.fit(X) 
X= imputer.transform(X)

# Splitting the dataset into the Training set and Test set

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Understanding the nature of the dataset 

pd.DataFrame(X_test).info()
pd.DataFrame(X_test).describe()

# Feature Scaling

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#Encoding categorical data

le_X = LabelEncoder()
X_test[:, 0] = le_X.fit_transform(X_test[:, 0]) # encodes vlaues of first column
onehotencoder = OneHotEncoder(categorical_features = [0])
X_test = onehotencoder.fit_transform(X_test).toarray()
le_Y = LabelEncoder()

# Logistic Regression

dcl_clf = LogisticRegression(random_state = 0)
dcl_clf.fit(X_train, y_train)
pred_dcl = dcl_clf.predict(X_test)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, pred_dcl)

# Visualising the Training set results

X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, dcl_clf.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('blue', 'grey')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('blue', 'grey'))(i), label = j)
plt.title('Training set Prediction')
plt.xlabel('Age Group')
plt.ylabel('Salary Range')
plt.legend()
plt.show()

# Visualising the Test set results

X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, dcl_clf.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('blue', 'grey')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('blue', 'grey'))(i), label = j)
plt.title('Test set Prediction')
plt.xlabel('Age Group')
plt.ylabel('Salary Range')
plt.legend()
plt.show()
