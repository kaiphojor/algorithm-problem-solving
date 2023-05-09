import http.client
import json
conn = http.client.HTTPSConnection("solved.ac")

headers = { 'Content-Type': "application/json" }

conn.request("GET", "/api/v3/user/show?handle=jquath", headers=headers)

res = conn.getresponse()
data = res.read()
json_string = json.loads(data.decode("utf-8"))
# print(json_string)
print(json_string['solvedCount'])
print(json_string['handle'])