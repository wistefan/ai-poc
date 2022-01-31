# This script creates a subscription of Happy Cattle to Smart Shepherd Inc. 
# to get notified about new predictions calculations
import requests
import json


url = "http://localhost:1029/ngsi-ld/v1/subscriptions/"


headers = {
	'Content-Type': 'application/ld+json'
}

payload= json.dumps({
	"description": "Notify me of new animal coordinates",
	"type": "Subscription",
	"entities": [{"type": "Animal"}],
	"notification": {
		"format": "keyValues",
		"endpoint": {
		"uri": "http://apis.docker:5000/subscription",
		"accept": "application/json"
		}
	},
	"@context": "http://context/ngsi-context.jsonld"
})

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)