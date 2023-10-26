
from typing import Union




from fastapi import FastAPI
import json
from pydantic import BaseModel
from prediction import features_to_return
app = FastAPI()

class Data(BaseModel):
    LivingArea: int
    Bedrooms: int
    PostalCode: int
    SurfaceOfGood: int
    Garden: bool
    Kitchen:str
    SwimmingPool: bool
    Furnished: bool
    Openfire: bool
    Terrace: bool
    NumberOfFacades: int
    StateOfBuilding:str
    Heating: str
    TypeOfSale:int
        

@app.get("/")
def read_root():
    return {"status": "alive"}

@app.post("/predict")
def predict(payload:Data):
   

    print(payload.model_dump())
    pred=features_to_return(payload.model_dump())
   
# For example, you can use a machine learning model to predict house prices.
# prediction_result = your_prediction_function(data)
# return {"prediction": prediction_result}

# Placeholder response as an example.

    return {"Prediction": pred[0]}


@app.get("/predict")
def get_predict_info():
    """
    Endpoint to handle GET requests for explaining what the POST request to /predict expects.
    """
    explanation = (
        "Send a POST request to this endpoint with JSON data representing a house to get a prediction. "
        "The JSON data should include the necessary features for prediction."
    )
    return explanation