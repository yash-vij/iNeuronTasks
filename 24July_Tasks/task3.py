#3. read these dataset in pandas as a dataframe

import pandas as pd
read_file_Atrribute= pd.read_excel("C:\ineuron\Attribute DataSet.xlsx")

store_in_csv_Atrribute= read_file_Atrribute.to_csv("Atrribute_Dataset.csv", index = None, header = True)

read_file_Dress= pd.read_excel("C:\ineuron\Dress Sales.xlsx")
store_in_csv_Dress= read_file_Dress.to_csv("Dress_Sales.csv", index = None, header = True)
