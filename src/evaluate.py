import pickle
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from log_experiment import log_experiment

def evaluate():
    """Evaluation of the model based on test data
    """
    def eval_metrics(actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2

    # Load the test dataset saved after the splitting step
    with open('temp/test.pkl', "rb") as file:
        test = pickle.load(file)

    # Load the calibrated model from the pickle file
    with open('output/model.pkl', "rb") as file:
        model = pickle.load(file)

    # The predicted column is "quality" which is a scalar from [3, 9]
    test_x = test.drop(["quality"], axis=1)
    test_y = test[["quality"]]

    # Evaluate Metrics
    predicted_qualities = model.predict(test_x)
    rmse, mae, r2 = eval_metrics(test_y, predicted_qualities)

    return rmse, mae, r2

rmse, mae, r2 = evaluate()
log_experiment({"rmse":rmse, 
                "mae": mae,
                "r2":r2})
