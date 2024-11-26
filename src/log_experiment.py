import yaml
import mlflow
from typing import Dict

def log_experiment(results:Dict)->None:
    """Function to log the experiment in MLFlow

    Args:
        results (Dict): Metrics we want to log
    """
    # Loading the parameters
    with open('params.yaml', 'r') as file:
        params = yaml.safe_load(file)

    # Reading the information regarding the pipeline
    pipeline_name = params['pipeline']['name']
    pipeline_host = params['pipeline']['host']
    pipeline_port = params['pipeline']['port']

    # Set the tracking URL
    mlflow.set_tracking_uri(uri=f"http://{pipeline_host}:{pipeline_port}")

    # Set the experiment name
    mlflow.set_experiment(pipeline_name)

    with mlflow.start_run():

        # Setting the parameters from the split step
        test_size = params['split']['test_size']
        seed = params['split']['seed']

        mlflow.log_param("test_size", test_size)
        mlflow.log_param("test_seed", seed)

        # Setting the parameters for our model
        alpha = params['train']['alpha']
        l1_ratio = params['train']['l1_ratio']
        seed = params['train']['seed']

        mlflow.log_param("alpha", alpha)
        mlflow.log_param("l1ratio", l1_ratio)
        mlflow.log_param("seed", seed)

        # Loop to log the metrics passed in arguments
        for c in results.keys():
            mlflow.log_metric(c, results[c])


   