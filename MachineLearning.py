#Machine Learning

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





data = pd.read_csv("/Users/lawandyaseen/Desktop/PPOL564FinalProject/Suspension_TeachExp_Finance.csv")
data = data.drop(columns = ["Unnamed: 0"])
np.random.seed(1234)

len(train) #1321 schools used in training data

#using SKLEARN framework

#separating outcome and predictors
#outcome -- all students
Y = data['ALL STUDENTS']
#predictors of interest
X = data[['BLACK', 'ECONOMICALLY DISADVANTAGED', 'MALE', 'BHNA', 'TEACH_EXP', 'TEACH_EMERG', 'TEACH_OUT_OF_FIELD', 'SCHOOL_LEVEL_PER_PUPIL']]
#economically disadvantaged, black, white, per pupil spending, teacher experience, teacher emergency, teacher out of field

#split data into training and test
train_X, test_X, train_Y, test_Y = train_test_split(X,Y,test_size=.2,random_state=1234)

train_X

(
    ggplot(train_X.melt(),aes(x="value")) +
    geom_histogram() +
    facet_wrap("variable",scales="free") +
    theme_minimal() +
    theme(figure_size = (10,3))
)

#scale of spending --- thousands, other categories are between 0-100



#Using SKLEARN from class

fold_generator = KFold(n_splits=5, shuffle=True,random_state=111)
use_metrics = ["neg_mean_squared_error"]

# (2) Next specify the preprocessing steps
preprocess = ColumnTransformer(transformers=[('num', pp.MinMaxScaler(), ['BLACK', 'ECONOMICALLY DISADVANTAGED', 'MALE', 'BHNA', 'TEACH_EXP', 'TEACH_EMERG', 'TEACH_OUT_OF_FIELD', 'SCHOOL_LEVEL_PER_PUPIL'])])


# (3) Next Let's create our model pipe (note for the model we leave none as a placeholder)
pipe = Pipeline(steps=[('pre_process', preprocess),
                       ('model',None)])


# (4) Specify the models and their repsective tuning parameters.
# Note the naming convention here to reference the model key
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

# (5) Put it all together in the grid search
search = GridSearchCV(pipe, search_space,
                      cv = fold_generator,
                      scoring='neg_mean_squared_error',
                      n_jobs=4)
# (6) Fit the model to the training data
search.fit(train_X,train_Y)


search.best_score_ # Mean out-of-sample (CV) error


search.best_params_
#need to tune the parameter






#predict will use best model
pred_Y = search.predict(test_X)


#visualizing the prediction with best model 
(
    ggplot(pd.DataFrame(dict(pred=pred_Y,truth=test_Y)),
          aes(x='pred',y="truth")) +
    geom_point(alpha=.75) +
    geom_abline(linetype="dashed",color="darkred",size=1) +
    theme_bw() +
    theme(figure_size=(10,7))
)
