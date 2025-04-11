import requests
import json

url = "https://demo.squashtest.org/squash/api/rest/latest/requirements?size=2&page=50"

payload = {}
headers = {
    "Cookie": 'JSESSIONID=60606E958927263DD68B61754ADE96ED'
}

response = requests.request("GET", url, headers=headers, data=payload)
data = response.json()

# Access the 'page' part of the response
page_data = data.get("page", {})
size = page_data.get("size")
total_elements = page_data.get("totalElements")
total_pages = page_data.get("totalPages")
number = page_data.get("number")

print(size)
print(total_elements)
print(total_pages)
print(number)
# print(response)
# print(response.json)
# page_data = response.json
# size = response.get("size")
# print(size)
# print(json.dumps(response.json(), indent=2))
