def validate_dataset(dataframe):
    """
    Validates the loaded DataFrame.

    Returns
    -------
    tuple
        (True, "Success") if valid
        (False, "Reason") if invalid
    """

    # Dataset is empty
    if dataframe.empty:
        return False, "The uploaded CSV file contains no data."

    # No columns found
    if len(dataframe.columns) == 0:
        return False, "The dataset has no columns."

    # Duplicate column names
    if dataframe.columns.duplicated().any():
        return False, "Duplicate column names were found."

    # Missing column names
    if dataframe.columns.isnull().any():
        return False, "Some column names are missing."

    return True, "Dataset is valid."