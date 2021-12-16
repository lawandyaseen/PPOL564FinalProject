#Machine Learning
#used ML pipeline that was used in class


#packages used
import pandas as pd
import numpy as np
import missingno as miss
from plotnine import *
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

from sklearn import preprocessing as pp
from sklearn.compose import ColumnTransformer

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_validate
from sklearn.model_selection import GridSearchCV

from sklearn.linear_model import LinearRegression as LM
from sklearn.neighbors import KNeighborsRegressor as KNN
from sklearn.tree import DecisionTreeRegressor as DTree
from sklearn import tree
from sklearn.ensemble import BaggingRegressor as Bag
from sklearn.ensemble import RandomForestRegressor as RF

import sklearn.metrics as m

from sklearn.pipeline import Pipeline

import sklearn.metrics as m

from sklearn.pipeline import Pipeline

from sklearn.inspection import (
    permutation_importance,
    partial_dependence,
    PartialDependenceDisplay,
    plot_partial_dependence
)
import warnings
warnings.filterwarnings("ignore")




#loading in cleaned data
data = pd.read_csv("/Users/lawandyaseen/Desktop/PPOL564FinalProject/Cleaned Data/project_data.csv")
#dropping index column from export
data = data.drop(columns = ["Unnamed: 0"])
#setting sed
np.random.seed(1234)

len(data)#819 schools used in training data


#using SKLEARN framework

#separating outcome and predictors
#outcome -- all students
Y = data['IN_SCHOOL_SUSPENSION_RATE']
#predictors of interest
X = data[['FEMALE', 'MALE', 'NATIVE', 'ASIAN', 'BLACK', 'HISPANIC', 'MULTIPLE', 'AAPI', 'WHITE', 'TEACH_INEXP', 'SCHOOL_LEVEL_PER_PUPIL']]

#split data into training and test
train_X, test_X, train_Y, test_Y = train_test_split(X,Y,test_size=.2,random_state=1234)

train_X

len(train_X)

#Using SKLEARN from class

#cross validator - using MSE as the measure of effectivness
fold_generator = KFold(n_splits=5, shuffle=True,random_state=111)
use_metrics = ["neg_mean_squared_error"]

#preprocessing data
preprocess = ColumnTransformer(transformers=[('num', pp.MinMaxScaler(), ['FEMALE', 'MALE', 'NATIVE', 'ASIAN', 'BLACK', 'HISPANIC', 'MULTIPLE', 'AAPI', 'WHITE', 'TEACH_INEXP', 'SCHOOL_LEVEL_PER_PUPIL'])])


#creating pipeline
pipe = Pipeline(steps=[('pre_process', preprocess),
                       ('model',None)])


#model ID

search_space = [
    # Linear Model
    {'model' : [LM()]},

    # KNN with K tuning param
    {'model' : [KNN()],
     'model__n_neighbors':[10,15,20,25,30]},

    # Decision Tree with the Max Depth Param
    {'model': [DTree()],
     'model__max_depth':[1,2,3,5]},

    # The Bagging decision tree model
    {'model': [Bag()]},

    # Random forest with the N Estimators tuning param
    {'model' : [RF()],
     'model__max_depth':[1,2,3],
     'model__n_estimators':[500,1000,1250]},
]

# Creating a grid search
search = GridSearchCV(pipe, search_space,
                      cv = fold_generator,
                      scoring='neg_mean_squared_error',
                      n_jobs=4)

# plugging in training data
search.fit(train_X,train_Y)

#reports back the lowest MSE
search.best_score_

#reports the best algorithm and the best parameters
search.best_params_


#pulling scores for comparing
lm_scores = cross_validate(LM(),train_X,train_Y, cv = fold_generator, scoring =use_metrics)
knn_scores = cross_validate(KNN(),train_X,train_Y, cv = fold_generator, scoring =use_metrics)
dt_scores = cross_validate(DTree(),train_X,train_Y, cv = fold_generator, scoring =use_metrics)
bag_scores = cross_validate(Bag(),train_X,train_Y, cv = fold_generator, scoring =use_metrics)
rf_scores = cross_validate(RF(),train_X,train_Y, cv = fold_generator, scoring =use_metrics)

#adding above scores into a dictionary
collect_scores = \
dict(lm = lm_scores['test_neg_mean_squared_error']*-1,
     knn = knn_scores['test_neg_mean_squared_error']*-1,
     dt = dt_scores['test_neg_mean_squared_error']*-1,
     bag = bag_scores['test_neg_mean_squared_error']*-1,
     rf = rf_scores['test_neg_mean_squared_error']*-1)

# converting dictionary into dataframe
collect_scores = pd.DataFrame(collect_scores).melt(var_name="Model",value_name="MSE")
collect_scores.head()

#predict will use best model
pred_Y = search.predict(test_X)


#visualizing the predicted values using the best model
viz4 = (
    ggplot(pd.DataFrame(dict(Predicted=pred_Y,Observed=test_Y)),
          aes(x='Predicted',y='Observed')) +
    geom_point() + labs(title = "Comparison of Accuracy") +
    geom_abline(linetype="dashed",color="green",size=1) + theme_538() +
    theme(figure_size=(10,7))
)

#saving this graphic
viz4.save(filename = "viz4.png", dpi = 100)

rf_mod = search.best_estimator_

#permutation importance with 25 iterations
vi = permutation_importance(rf_mod,test_X,test_Y,n_repeats=25)

# Organizing as a dataframe
vi_dat = pd.DataFrame(dict(variable=train_X.columns,
                           vi = vi['importances_mean'],
                           std = vi['importances_std']))

# Generate intervals
vi_dat['low'] = vi_dat['vi'] - 2*vi_dat['std']
vi_dat['high'] = vi_dat['vi'] + 2*vi_dat['std']

#ascending order
vi_dat = vi_dat.sort_values(by="vi",ascending=False).reset_index(drop=True)


#visualizing rank of importance
viz5 = (
    ggplot(vi_dat,
          aes(x="variable",y="vi")) +
    geom_col(alpha=.5) +
    geom_point() +
    geom_errorbar(aes(ymin="low",ymax="high"),width=.2) +
    theme_bw() +
    scale_x_discrete(limits=vi_dat.variable.tolist()) +
    coord_flip() +
    labs(y="Reduction in AUC ROC",x="", title = "Comparison of Variable Impact on Model Accuracy")
)

#saving this graphic
viz5.save(filename = "viz5.png", dpi = 100)
