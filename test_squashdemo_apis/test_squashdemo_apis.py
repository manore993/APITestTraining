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
        "Cookie": 'JSESSIONID=9E3A41A9097B18A305EE0120D928B803'
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
    assert total_elements == 248
    assert total_pages == 124
    assert number == 50


def test_get_requirements_by_id():
    
    url1 = "https://demo.squashtest.org/squash/api/rest/latest/requirements/712"
    payload = {}
    headers = {
        "Cookie": 'JSESSIONID=9E3A41A9097B18A305EE0120D928B803'
    }
    response = requests.request("GET", url1, headers=headers, data=payload)
    data = response.json()

    assert response.status_code == 200
    assert data.get("id") == 712
    
def test_get_testcases_by_id():
    
    url1 = "https://demo.squashtest.org/squash/api/rest/latest/test-cases/223"
    payload = {}
    headers = {
        "Cookie": 'JSESSIONID=9E3A41A9097B18A305EE0120D928B803'
    }
    response = requests.request("GET", url1, headers=headers, data=payload)
    data = response.json()

    assert response.status_code == 200
    assert data.get("_type") == "keyword-test-case"
    assert data.get("id") == 223
    assert isinstance(data["steps"], list)