import requests
URL='https://dummyjson.com/users'
response=requests.get(URL)
data=response.json()
print(data)