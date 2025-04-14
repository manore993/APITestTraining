import requests
import json

url = "https://demo.squashtest.org/squash/api/rest/latest/requirements?size=2&page=50"

payload = {}
headers = {
    "Cookie": 'JSESSIONID=9E3A41A9097B18A305EE0120D928B803'
}

url1 = "https://demo.squashtest.org/squash/api/rest/latest/requirements/712"
response = requests.request("GET", url1, headers=headers, data=payload)
data = response.json()
page_data = data.get("id")
print(page_data)