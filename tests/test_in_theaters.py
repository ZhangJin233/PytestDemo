import requests
import yaml


def get_test_data(test_data_path):
    case = []  # 存储测试用例名称
    http = []  # 存储请求对象
    expected = []  # 存储预期结果
    with open(test_data_path) as f:
        data = yaml.load(f.read(), Loader=yaml.SafeLoader)
        test = data['tests']
        for td in test:
            case.append(td.get('case', ''))
            http.append(td.get('http', {}))
            expected.append(td.get('expected', {}))
    parameters = zip(case,http,expected)
    return case, parameters

cases,parameters = get_test_data("/Users/zhangjin/Documents/github/PytestDemo/data/test_in_theaters.yaml")
class TestInTheaters(object):
    def test_in_thearter(self):
        host = "https://api.caiyunapp.com"
        path =  "/v2.5/OH0Toat4=ZPjB1OU/121.6544,25.1552/weather.json"
        url = host + path
        r = requests.request("GET",url)
        response = r.json()
        assert response["status"] == 'ok'
