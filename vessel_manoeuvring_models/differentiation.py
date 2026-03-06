import numpy as np

"""Module for differentiation of dataframes"""
def derivative(df, key):
    # d = np.diff(df[key]) / np.diff(df.index)
    # d = np.concatenate((d, [d[-1]]))
    d = np.gradient(df[key], df.index)
    return d
