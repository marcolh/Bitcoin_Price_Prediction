
"""
Ta
"""

#--------------------------------------------------------------------------
# Import Libraries
#--------------------------------------------------------------------------

from Modules import data_clean

#--------------------------------------------------------------------------
# Get Variables
#--------------------------------------------------------------------------

str_data = 'bitcoin.csv'

#--------------------------------------------------------------------------
# Execute Code
#--------------------------------------------------------------------------

try:
    dc = data_clean.CleanData(str_data)
    print("the classes are started successfully")
except Exception as e:
    print("the classes are not initiated successfully")
    print(f"Error: {e}")
    exit(1)

try:
    df_bitcoin_data = dc.ReadData()
    print("Success")
except Exception as e:
    print("Fail")
    print(f"Error: {e}")
    exit(1)

try:
    features = ['Date','Open','High','Low','Adj Close','Volume'] 
    target = 'Close'
    X_train, X_test, y_train, y_test = dc.SplitData(df_bitcoin_data, features, target)
    print("train and test split has been completed successfully")
except Exception as e:
    print("the automation failed to complete the train and test split")
    print(f"Error:{e}")
    exit(1)