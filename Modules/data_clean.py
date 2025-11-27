
#--------------------------------------------------------------------------
# Import Libraries
#--------------------------------------------------------------------------

import polars as pl
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
#from xgboost import XGBXclassifier
from sklearn import metrics

import warnings
warnings.filterwarnings("ignore")

#--------------------------------------------------------------------------
# Get Variables
#--------------------------------------------------------------------------



#--------------------------------------------------------------------------
# Clean Data
#--------------------------------------------------------------------------

class CleanData:

    def __init__(self, data):
        self.str_data = data

    def ReadData(self):
        df_bitcoin_data = pl.read_csv(self.str_data)
        int_null_values = 

        return df_bitcoin_data
    
    def 
