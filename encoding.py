import numpy as np
import pandas as pd

def encode_Heating(df,category):
    for index, row in df.iterrows():
    
        if row.Heating=='carbon':
            df.at[index, category]=138805
        elif row.Heating=='electric':
            df.at[index, category]=250000
        elif row.Heating=='fueloil':
            df.at[index, category]=325000
        elif row.Heating=='gas':
            df.at[index, category]=280000
        elif row.Heating=='pellet':
            df.at[index, category]=210000
        elif row.Heating=='solar':
            df.at[index, category]=408000
        elif df.at[index, category]=='wood':
            df.at[index, category]=199000
        else:
            df.at[index, category]=321721
        
    return df

def encode_Kitchen(df,category):
    for index, row in df.iterrows():
    
        if row.Kitchen=='hyper equipped':
            df.at[index, category]=399000
        elif row.Kitchen=='installed':
            df.at[index, category]=289000
        elif row.Kitchen=='not installed':
            df.at[index, category]=225000
        elif row.Kitchen=='semi equipped':
            df.at[index, category]=235000
        elif row.Kitchen=='usa hyper equipped':
            df.at[index, category]=421000
        elif row.Kitchen=='usa installed':
            df.at[index, category]=305613
        elif row.Kitchen=='usa semi equipped':
            df.at[index, category]=256000
        elif row.Kitchen=='usa uninstalled':
            df.at[index, category]=314500
        else:
            df.at[index, category]=401436
    return df

def encode_StateOfBuilding(df,category):
       
    for index, row in df.iterrows():
    
        if row.StateOfBuilding=='as new':
            df.at[index, category]=289000
        elif row.StateOfBuilding=='good':
            df.at[index, category]=269000
        elif row.StateOfBuilding=='just renovated':
            df.at[index, category]=234450
        elif row.StateOfBuilding=='to be done up':
            df.at[index, category]=249000
        elif row.StateOfBuilding=='to renovate':
            df.at[index, category]=249000
        elif row.StateOfBuilding=='to restore':
            df.at[index, category]=220000
        else:
            df.at[index, category]=361939
    return df

def fix_nan_SurfaceOfGood(df):
    for index, row in df.iterrows():
            if np.isnan(df.at[index,'SurfaceOfGood']):
                df.at[index, 'SurfaceOfGood']=df.at[index, 'LivingArea']
def encoder(df):
    
    columns_to_model=['Furnished','Terrace','Garden','LivingArea','TypeOfSale','Bedrooms','PostalCode','Openfire','SwimmingPool','NumberOfFacades','SurfaceOfGood','Kitchen','Heating','StateOfBuilding']
    df=df[columns_to_model]
    fix_nan_SurfaceOfGood(df)

    encoded_df=encode_Heating(df,'Heating')
    encoded_df=encode_Kitchen(df,'Kitchen')
    encoded_df=encode_StateOfBuilding(df,'StateOfBuilding')
    
    encoded_df['NumberOfFacades'].fillna(1,inplace=True)
    encoded_df['Bedrooms'].fillna(1,inplace=True)
    encoded_df.fillna(-1,inplace=True)
    
    return encoded_df
