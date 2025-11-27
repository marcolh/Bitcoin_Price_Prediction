
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