from pydantic import BaseModel

#Creating a class for the attributes input to the ML model and the prediction attribute.
class Animal(BaseModel):
	pos_x : float
	pos_y :float
	pos_z : float
	temp : float = None
	activity : str = None
