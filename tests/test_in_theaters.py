import requests

class TestInTheaters(object):
    def test_in_thearter(self):
        host = "https://api.caiyunapp.com"
        path =  "/v2.5/OH0Toat4=ZPjB1OU/121.6544,25.1552/weather.json"
        url = host + path
        r = requests.request("GET",url)
        response = r.json()
        assert response["status"] == 'ok'
