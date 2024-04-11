# importing the requests library
import requests
 
# api-endpoint
ITEM_ID = "720825548692"
URL = f"https://api.upcdatabase.org/product/{ITEM_ID}"
 
# sending get request and saving the response as response object
r = requests.get(url = URL, headers={"Authorization": "Bearer E13B280796487261E5D32B9DEAF51B30"})
 
# extracting data in json format
data = r.json()
 
print(data)

