"""Training step of the model
"""

import pickle
import yaml
from sklearn.linear_model import ElasticNet

def train():
    """Function that trains the model based on training data
    """

    # Loading the parameters
    with open('params.yaml', 'r') as file:
        params = yaml.safe_load(file)

    # Getting the model parameters from params.yaml
    alpha = params['train']['alpha']
    l1_ratio = params['train']['l1_ratio']
    seed = params['train']['seed']

    # Load the training dataset
    with open('temp/train.pkl', "rb") as file:
        train = pickle.load( file)


    # The predicted column is "quality" which is a scalar from [3, 9]
    train_x = train.drop(["quality"], axis=1)
    train_y = train[["quality"]]

    # Execute ElasticNet
    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=seed)
    model = lr.fit(train_x, train_y)

    # Exporting the model using pickle
    with open('output/model.pkl', "wb") as file:
        pickle.dump(model, file)

train()