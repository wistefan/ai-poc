# This script creates entities in the Context Broker of Happy Cattle Co.
import requests
import json

#url="http://orion.docker:1028/ngsi-ld/v1/entities/" 
url= "http://localhost:1029/ngsi-ld/v1/entities"

headers = {
  'Content-Type': 'application/json',
  'Link': '<http://context/ngsi-context.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"'
}

payload = json.dumps({
  "id": "urn:ngsi-ld:Animal:0001",
  "type": "Animal",
  "modifiedAt": "2021-12-23T12:30:00Z",
  "species": {
    "type": "Property",
    "value": "cow"
  },
  "location": {
    "type": "GeoProperty",
    "value": {
      "type": "Point",
      "coordinates": [
        3.165,
        2.6133,
        -1.4292
      ]
    }
  },
  "animalActivity": {
    "type": "Property",
    "value": ""
  }
})

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)