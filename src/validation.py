import great_expectations as gx
import pandas as pd
import yaml

def validate_data():
    """Function to validate the data
        using the great expectation suite defined as yaml file
    """
    try:

        # Read the data file
        data = pd.read_csv('data/winequality-red.csv',sep=";")

        # Retrieve your Data Context
        context = gx.get_context()

        # Define the Data Source name
        data_source_name = "my_data_source"

        # Add the Data Source to the Data Context
        data_source = context.data_sources.add_pandas(name=data_source_name)

        # Define the Data Asset name
        data_asset_name = "my_dataframe_data_asset"

        # Add a Data Asset to the Data Source
        data_asset = data_source.add_dataframe_asset(name=data_asset_name)

        # Define the Batch Definition name
        batch_definition_name = "my_batch_definition"

        # Add a Batch Definition to the Data Asset
        batch_definition = data_asset.add_batch_definition_whole_dataframe(
            batch_definition_name
        )

        batch_parameters = {"dataframe": data}

        yaml_path = "expectations/winequality-data-validation.yaml"

        # Open the yaml file for great expectations
        with open(yaml_path, 'r') as yaml_file:
            suite_dict = yaml.safe_load(yaml_file)

        # Create a Great Expectation suite
        suite = gx.ExpectationSuite(**suite_dict)

        # Add the suite to the context
        context.suites.add(suite)

        # Get the dataframe as a Batch
        batch = batch_definition.get_batch(batch_parameters=batch_parameters)

        # Test the Expectation
        validation_results = batch.validate(suite)

        # We add an exception if there is a validation error
        if validation_results['success'] is False:
            raise AssertionError('The validation step didn\'t complete propertly')

    except Exception as e:
        raise e


validate_data()
