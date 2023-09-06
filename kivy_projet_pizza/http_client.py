import json

from kivy.network.urlrequest import UrlRequest


class HttpClient:

    def get_pizza(self, on_complete, on_error):
        url = "https://mathieuvdn.pythonanywhere.com/api/getpizza"

        def got_json(req, result):
            datas = json.loads(result)
            formatted_data = []
            for data in datas:
                formatted_data.append(data['fields'])
            if on_complete:
                on_complete(formatted_data)

        def data_error(req, error):
            if on_error:
                on_error(str(error))

        def data_failure(req, error):
            if on_error:
                on_error(str(req.resp_status))

        req = UrlRequest(url, on_success=got_json, on_error=data_error, on_failure=data_failure)
