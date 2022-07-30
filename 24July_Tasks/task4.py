#4. Convert attribute dataset in json format
import pandas as pd
read_file_Atrribute= pd.read_excel("C:\ineuron\Attribute DataSet.xlsx")

json_data = read_file_Atrribute.to_json('attribute_JSONFile.json')
json_data