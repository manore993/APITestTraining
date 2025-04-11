import requests

def test_first_try():

    url = "https://demo.squashtest.org/squash/api/rest/latest/docs/api-documentation.html#_get_all_projects"

    payload = {}
    headers = {
    'Authorization': 'Basic U3F1YXNoOlBAc3N3MHJkITEyMw==',
    'Cookie': 'JSESSIONID=FDA97245C795B1F8CCC4AF7623FA24BB'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200
    assert response.headers.get("Content-Type") == "text/html"
    assert "Squash TM REST API" in response.text

def test_get_all_requirements():
    
    url = "https://demo.squashtest.org/squash/api/rest/latest/requirements?size=2&page=50"

    payload = {}
    headers = {
        "Cookie": 'JSESSIONID=60606E958927263DD68B61754ADE96ED'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    
    data = response.json()
    page_data = data.get("page", {})
    size = page_data.get("size")
    total_elements = page_data.get("totalElements")
    total_pages = page_data.get("totalPages")
    number = page_data.get("number")

    assert response.status_code == 200
    assert size == 2
    assert total_elements == 253
    assert total_pages == 127
    assert number == 50