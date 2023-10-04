# download zip from url and unzip it
import os
import zipfile
import requests

def download_unzip(url, path):
    """Download zip from url and unzip it to path
    Args:
        url (str): url of zip file
        path (str): path to unzip
    """
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(path)