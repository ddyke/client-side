import requests

r = requests.get("http://www.realpython.com")

with open ("test_requests.html", "wb") as code:
    code.write(r.content)