import requests
from endpoints.endpoint import Endpoint
from requests.exceptions import JSONDecodeError


class CreateMeme(Endpoint):
    meme_id = None
    response_payload = None

    def create_meme(self, payload, headers=None):
        headers = headers if headers else self.headers
        url = f'{self.BASE_URL}/meme'
        self.response = requests.post(url, headers=headers, json=payload)
        try:
            self.json = self.response.json()
            print(self.json)
        except JSONDecodeError:
            self.json = {'error': 'Response is not in JSON format'}

        if self.response.status_code == 200 and 'id' in self.json:
            self.meme_id = self.json['id']
            self.response_payload = self.json
        else:
            self.meme_id = None
