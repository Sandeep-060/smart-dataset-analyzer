import pandas as pd


def load_dataset(uploaded_file):
    """
    Reads the uploaded CSV file and returns
    a Pandas DataFrame.

    Parameters
    ----------
    uploaded_file :Streamlit UploadedFile object.

    Returns
    -------
    pandas.DataFrame - Loaded dataset.
    """

    try:
        dataframe = pd.read_csv(uploaded_file)
        return dataframe

    except pd.errors.EmptyDataError:
        raise ValueError("The uploaded CSV file is empty.")

    except pd.errors.ParserError:
        raise ValueError("The CSV file is corrupted or has an invalid format.")

    except UnicodeDecodeError:
        raise ValueError("Unable to read the file. Please use UTF-8 encoded CSV.")

    except Exception as e:
        raise ValueError(f"Unexpected error while loading dataset:\n{e}")