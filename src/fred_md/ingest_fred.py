import pandas as pd

from urllib.error import HTTPError

from .utils.transform import normalize


make_url = lambda version: f"https://s3.amazonaws.com/files.fred.stlouisfed.org/fred-md/monthly/{version}.csv"

def import_raw_fred(version: str = "current") -> pd.DataFrame:
    """
    Takes a version name and imports the data. Defaults to the latest data.

    Parameters
    ----------
    version : str, optional
        version in format YYYY-MM, by default "current"

    Returns
    -------
    pd.DataFrame
        The raw data
    """

    url = make_url(version)

    try:
        data = pd.read_csv(url)
    except HTTPError:
        raise ValueError(f"Got a HTTP error, check your version: {version}!")

    return data


def import_transformed_data(version: str = "current") -> pd.DataFrame:
    """
    Takes a version name and imports the data and applies the transformation. 
    Defaults to the latest data.

    Parameters
    ----------
    version : str, optional
        version in format YYYY-MM, by default "current"

    Returns
    -------
    pd.DataFrame
        The transformed data
    """

    raw_df = import_raw_fred(version)

    return normalize(raw_df)