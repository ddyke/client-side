import requests

url = "http://httpbin.org/post"
data = {"fname": "Michael", "lname": "Herman"}

r = requests.post(url, data=data)

#print(r)       # returns status_code
print(r.content)