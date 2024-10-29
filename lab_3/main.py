import json
import csv

from typing import Dict, List
from typing import Optional


def get_json(path_name: str) -> Optional[Dict]:
    '''
    The function is for reading .json file and returns dictionary

    Args:
            path_name: path to .json file

    Returns:
            data: dictionary of regular expressions
    '''
    try:
        with open(path_name, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"The file was not found.")
    except Exception as e:
        print(f"An error occured while reading JSON the file: {str(e)}.")


def get_csv(path_name: str) -> Optional[List]:
    '''
    The function is for reading .csv file and returns list 
    of strings without a header string

    Args:
            path_name: path to .csv file

    Returns:
            data: a list of lists that contains lines from the file 
                  (without the header line)

    '''
    data = []
    try:
        with open(path_name, 'r', encoding='utf-16') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                data.append(row)
            data.pop(0)
        return data
    except FileNotFoundError:
        print(f"The file was not found.")
    except Exception as e:
        print(f"An error occured while reading CSV the file: {str(e)}.") 
    