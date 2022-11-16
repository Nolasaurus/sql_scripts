import pandas as pd

def csv_to_db(file, table_name):
    
    data = pd.read_csv(file)
    col_names = data.keys()
    ##TODO connect to db by calling connection script
        ##TODO create connection script
    
    
    ##TODO Authenticate by calling auth script
        ##TODO create authentication script


    ##TODO check if table exists


    ##TODO create table if does not exist

    
    ##TODO if table exists add data that is not already present




    print(data.head())




#csv_file = 'C:/Users/meyer/Downloads/EPA_SmartLocationDatabase_V3_Jan_2021_Final.csv'
#csv_file = 'C:/Users/meyer/Downloads/Electric_Vehicle_Population_Data.csv'

#csv_to_db(csv_file, )