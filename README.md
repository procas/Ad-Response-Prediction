# Ad Response Prediction

### The aim of this project is to predict if a person is interested in Advertisements from DCL Chemicals Company

#### Technologies used: Pandas, Matplotlib, Standard Scaler, One hot encoder, Logistic Regression, Imputer

### Data gathering
The dataset was provided with the characteristics of the category of people who were interested in advertisements published by the DCL Chemicals company, e.g., their profession, their area of interest, age group, salary group, etc. among other relevant characteristics.

### Data cleaning
Imputer was used to handle the data cleaning, in case of missing or NaN values in the dataset, or other discrepancies in the data prior to processing. The imputer was made to use 'mean' strategy for missing data replacement.

### Data preparation
The given dataset was split into training and test sets, followed by encoding the categorical values into numerical for the use of analysis.

### Feature selection
The requirements specified that only relevant features for the analysis have been provided, hence no feature extraction of sorts was performed.

### Train-Test split
The dataset was split into approximately 80:20 ratio for training and test sets respectively before commencing the analysis.

### Feature scaling
Feature scaling is done in order to ensure the dimensionality of the training and test sets are appropriate, before fitting the model

### Encoding of categorical data
Categorical data like profession/area of expertise, etc. are difficult to fit into predictive models, hence they have here been converted to corresponding numerical encoded counterparts.

## The predictive model
Logistic regression is chosen as the appropriate predictor model in this problem statement, since each target will have predicted value as 1/0 corresponding to interested or not. Logistic regression is ideal for binary prediction in case of binary classifiers, as well as has superior outlier handling capabilities.

## Visualisation
Created separate visualisation results for both training and test data

### Achieved overall accuracy of 85% in prediction
