
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
        print(df_bitcoin_data.describe())
        int_null_values = df_bitcoin_data.null_count()
        sns.boxplot(df_bitcoin_data['Close'])

        return df_bitcoin_data

    def SplitData(self, df_bitcoin_data, features, target):
        X = df_bitcoin_data[features]
        y = df_bitcoin_data[target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

        return X_train, X_test, y_train, y_test

    def TrainPrediction(self, X_train, X_test, y_train, y_test):
        