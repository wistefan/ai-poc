import pickle

from fastapi import Body, FastAPI, Request
from fastapi.logger import logger
from pydantic import ValidationError

import input_data
from models.animal import Animal

app = FastAPI(
	title="AI service PoC",
	description="End to end AI service for animal activity recognition in real-time",
	version="0.1",
	)

#Loading the trained model
with open("./trained-models/trained-model.pkl", "rb") as f:
	loaded_model = pickle.load(f)


# homepage route
@app.get("/")
def read_root():
	return {'message': 'This is the homepage of the API '}


@app.post('/notification')
def get_coordinates(data :dict = Body(...)):
    print("This is the right-time data of the animals in the field")
    print(data)
    coordinates= input_data.animal_notification_parser(data)
    print("These are the current animal coordinates: ")
    print(coordinates)
    return(coordinates)

@app.post('/prediction')
def get_prediction(data:Animal):
    data = get_coordinates()
    print(data)
    input = data.dict()
    posx = input['pos_x']
    posy = input['pos_y']
    posz = input['pos_z']
    temp = input['temp']
    prediction = loaded_model.predict([[posx, posy, posz, temp]]).tolist()[0]
    return  prediction


""" @app.get('/temperature')
async def get_temperature():
	response = actual_temperature
	print(response)
	return response """


@app.post("/animal")
def animal_attributes(data: dict):
	try:
		animal = Animal(**data)
		print("Animal coordinates")
		return "Hi I'm a cow and my coordinates are: " + str(animal.pos_x) + "," + str(animal.pos_x) + "," + str(animal.pos_x)
	except ValidationError as e:
		print(e.json())

