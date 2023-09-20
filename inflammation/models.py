"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """_summary_

    Args:
        data (matrix): numpy data array

    Returns:
       np.mean(data, axis=0) : a numpy data array
       Returns the daily mean of a 2D inflammation data array.
    
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Returns the daily max of a 2d inflammation data array."""
    return np.max(data, axis=0)


def daily_min(data):
    """Returns the daily min of a 2d inflammation data array."""
    return np.min(data, axis=0)
