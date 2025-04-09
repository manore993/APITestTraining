import requests

def test_get_all_requirements():

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
