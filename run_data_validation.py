import great_expectations as gx
import pandas as pd

def run_validation():
    print("Initializing Great Expectations...")
    context = gx.get_context()

    # Connect to local CSV data
    data_source = context.data_sources.add_pandas("customer_pandas_source")
    data_asset = data_source.add_csv_asset(
        name="customer_csv_asset", 
        filepath_or_buffer="customer_data.csv"
    )
    batch_definition = data_asset.add_batch_definition_whole_dataframe("customer_batch")

    # Create Expectation Suite
    suite = gx.ExpectationSuite(name="customer_data_expectations")

    # Add the 8 expectations
    suite.add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="customer_id"))
    suite.add_expectation(gx.expectations.ExpectColumnValuesToBeUnique(column="customer_id"))
    suite.add_expectation(gx.expectations.ExpectColumnValuesToBeBetween(column="age", min_value=0, max_value=120))
    suite.add_expectation(gx.expectations.ExpectColumnValuesToMatchRegex(column="email", regex=r"^[^@]+@[^@]+\.[^@]+$"))
    suite.add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="salary", mostly=0.95))
    suite.add_expectation(gx.expectations.ExpectColumnValuesToBeInSet(column="country", value_set=["USA", "Canada", "UK", "Australia"]))
    suite.add_expectation(gx.expectations.ExpectColumnValuesToBeOfType(column="signup_date", type_="object"))
    suite.add_expectation(gx.expectations.ExpectTableRowCountToBeBetween(min_value=500, max_value=1000))

    # Add suite to context
    suite = context.suites.add(suite)

    # Create a Validation Definition
    validation_definition = gx.ValidationDefinition(
        name="customer_validation",
        data=batch_definition,
        suite=suite,
    )
    validation_definition = context.validation_definitions.add(validation_definition)

    # Create and Run Checkpoint
    checkpoint = gx.Checkpoint(
        name="customer_checkpoint",
        validation_definitions=[validation_definition],
    )
    checkpoint = context.checkpoints.add(checkpoint)
    
    print("Running validation against customer_data(in).csv...")
    checkpoint_result = checkpoint.run()

    # Generate and open HTML Data Docs
    print("Building Data Docs...")
    context.build_data_docs()
    context.open_data_docs()

if __name__ == "__main__":
    run_validation()