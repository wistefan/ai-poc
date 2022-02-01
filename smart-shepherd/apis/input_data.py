# This function parses the NGSI-LD notifocation payload and returns the coordinates 

def animal_notification_parser(payload: dict):

	list = payload["data"]

	location = list[0]["location"]

	coordinates = location["coordinates"]

	#list of aninal dict keys 
	keys = ["pos_x","pos_y","pos_z"]
	
	#creating a dict from 2 lists of keys and values 
	coord_dict = dict(zip(keys,coordinates))

	#print(coord_dict)
	return coord_dict


#Test the obove function here

#This is the expected structure of a Notification payload based on a Subscription for animal coordinates update

""" payload = {
   "id":"urn:ngsi-ld:Notification:61eff022a0e34da012c4747e",
   "type":"Notification",
   "subscriptionId":"urn:ngsi-ld:Subscription:61eff01fa0e34da012c4747d",
   "notifiedAt":"2022-01-25T12:42:10.410Z",
   "data":[
      {
         "id":"urn:ngsi-ld:Animal:0001",
         "type":"Animal",
         "state":"",
         "species":"cow",
         "location":{
            "type":"Point",
            "coordinates":[
               -1.744,
               2.1433,
               3.162
            ]
         }
      }
   ]
} """


#x = json_parser(payload)
#print(x)
