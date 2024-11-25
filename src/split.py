import yaml
import pickle

import pandas as pd
from sklearn.model_selection import train_test_split


def split():
    """Function that will split the dataset in train & test and save them in a pickle file
    """
    # Loading the parameters
    with open('params.yaml', 'r') as file:
        params = yaml.safe_load(file)

    # Setting the parameters
    test_size = params['split']['test_size']
    seed = params['split']['seed']

    # Read the data from the csv file
    data = pd.read_csv('data/winequality-red.csv', sep=";")

    # Split the data into training and test sets.
    # The split is controled by the test_size parameter
    train, test = train_test_split(data,
                                   test_size= test_size,
                                   random_state=seed)

    # Save the test set to a file
    with open('temp/test.pkl', "wb") as file:
        pickle.dump(test, file)

    # Save the train set to a file
    with open('temp/train.pkl', "wb") as file:
        pickle.dump(train, file)

split()
