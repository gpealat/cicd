import yaml
import pickle
import mlflow
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet

def train():

    # Loading the parameters
    with open('params.yaml', 'r') as file:
        params = yaml.safe_load(file)

    alpha = params['train']['alpha']
    l1_ratio = params['train']['l1_ratio']
    seed = params['train']['seed']

    with open('temp/train.pkl', "rb") as file:
        train = pickle.load( file)
   
    with open('temp/test.pkl', "rb") as file:
        test = pickle.load( file)

    # The predicted column is "quality" which is a scalar from [3, 9]
    train_x = train.drop(["quality"], axis=1)
    test_x = test.drop(["quality"], axis=1)
    train_y = train[["quality"]]
    test_y = test[["quality"]]

    # Execute ElasticNet
    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=seed)
    model = lr.fit(train_x, train_y)

    with open('output/model.pkl', "wb") as file:
        pickle.dump(model, file)

train()