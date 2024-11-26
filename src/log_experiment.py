import yaml
import mlflow
from typing import Dict

def log_experiment(results:Dict)->None:
    # Loading the parameters
    with open('params.yaml', 'r') as file:
        params = yaml.safe_load(file)

    # Reading the information regarding the pipeline
    pipeline_name = params['pipeline']['name']
    pipeline_host = params['pipeline']['host']
    pipeline_port = params['pipeline']['port']

    mlflow.set_tracking_uri(uri=f"http://{pipeline_host}:{pipeline_port}")
    mlflow.set_experiment(pipeline_name)

    with mlflow.start_run():

        # Setting the parameters
        test_size = params['split']['test_size']
        seed = params['split']['seed']

        mlflow.log_param("test_size", test_size)
        mlflow.log_param("test_seed", seed)

        alpha = params['train']['alpha']
        l1_ratio = params['train']['l1_ratio']
        seed = params['train']['seed']

        mlflow.log_param("alpha", alpha)
        mlflow.log_param("l1ratio", l1_ratio)
        mlflow.log_param("seed", seed)

        for c in results.keys():
            mlflow.log_metric(c, results[c])


   