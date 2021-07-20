import pandas as pd
import numpy as np
import joblib

reloadmodel=joblib.load('./model/ML_model_joblib.pkl')


def predict(location, sqft, bath, bhk): 
    X=pd.read_csv("IndependentVariable")   
    loc_index = np.where(X.columns==location)[0][0]

    x = np.zeros(len(X.columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
        
  #  print([x])
    return reloadmodel.predict([x])