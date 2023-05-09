import requests

url = "https://solved.ac/api/v3/user/show"

querystring = {"handle":"jquath"}

headers = {"Content-Type": "application/json"}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)