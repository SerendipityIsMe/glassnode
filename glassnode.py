import requests as req
import datetime as dt
import pandas as pd

def date_to_unix(
    year = 2010,
    month = 1,
    day = 15,
    ):
    '''Returns the date (UTC time) in Unix time'''

    time = int((dt.datetime(year, month, day, 0, 0, 0).timestamp()))
    return time


def glassnode(
    endpoint, 
    start,
    until, 
    api_key = 'a2b123be-2c50-4dc9-bdf4-cded52c3d1fc', # Modify before posting publicly!
    asset = 'BTC',
    status = False,
    headers = False,
    wait = 10
    ):
    '''Returns a Dataframe of time, value pairs for a metric from the Glassnode API.
    
    Parameters
    ----------
    endpoint : str
        Endpoint url after https://api.glassnode.com, corresponding to some metric (ex. '/v1/metrics/indicators/puell_multiple' )
    start : list
        Start date as a list in decreasing order (ex. [2015, 11, 27] )
    until : list
        End date as a list in decreasing order (ex. [2018, 5, 13] )
    api_key : str
        Your API key (ex. 'a2b123be-2c50-4dc9-bdf4-cded52c3d1fc' )
    asset : str
        Asset to which the metric refers. (ex. BTC )
    status : bool
        Option to print HTTP status code. '<Response [200]>' means success.
    headers : bool
        Option to print HTTP headers. Contains REST API request and response metadata.
    wait : float
        Seconds until the connection timeouts. ALWAYS specify a period.

    Returns
    -------
    DataFrame
        List of {'t' : unix-time, 'v' : 'metric-value'} pairs
    '''

    s = date_to_unix(year=start[0], month=start[1], day=start[2])
    u = date_to_unix(year=until[0], month=until[1], day=until[2])

    response = req.get(
        f'https://api.glassnode.com{endpoint}', 
        {
        'api_key': api_key, 
        'a': asset, 
        's': s, 
        'u': u
        }, 
        timeout = wait)

    df = pd.DataFrame(response.json())

    if status:
        print(response)
    if headers:
        print(response.headers)
    return df
