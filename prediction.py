import numpy as np
import pickle
import pandas as pd

from encoding import encoder


def prediction(X):
   
    model = pickle.load(open("GradientBoosting.pkl", "rb"))
    
    ypred = model.predict(X)
    return ypred
  



def predictions_from_app(house_data):
    
    df= pd.DataFrame(house_data,index=[0])
    encoded_df=encoder(df)
    X=encoded_df
    predicitons=prediction(X)
    return predicitons