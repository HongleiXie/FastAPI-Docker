import pickle
import numpy as np
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, conlist


app = FastAPI(title="Predicting Wine Class with batching")

# Represents a batch of wines
class Wine(BaseModel):
    # list of constrained list
    # has to be float type and be of size of 13
    # not explicitly naming each feature so the order of the data matters!
    batches: List[conlist(item_type=float, min_items=13, max_items=13)]


@app.on_event("startup") # ensure that the function is run at the startup of the server
def load_clf():
    # Load classifier from pickle file
    with open("../app/wine.pkl", "rb") as file:
        global clf # make the model global so other functions can access it
        clf = pickle.load(file)


@app.get("/")
def home():
    return "Congratulations! Your API is working as expected. This new version allows for batching. Now head over to http://localhost:81/docs"


@app.post("/predict")
def predict(wine: Wine):
    batches = wine.batches
    np_batches = np.array(batches) # the sci-kit learn accepts numpy array with shape (1,13) as model input
    pred = clf.predict(np_batches).tolist() # convert to a list to make them REST-compatible
    return {"Prediction": pred}