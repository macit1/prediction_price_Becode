import numpy as np
import pickle
import pandas as pd

from encoding import encoder


def prediction(X):
   
    model = pickle.load(open("GradientBoosting_02.pkl", "rb"))
    
    ypred = model.predict(X)
    return ypred
  



def features_to_return(json):
    print(type(json))
    df= pd.DataFrame(json,index=[0])

    print(type(df))

    encoded_df=encoder(df)
    X=encoded_df
    predicitons=prediction(X)
    return predicitons