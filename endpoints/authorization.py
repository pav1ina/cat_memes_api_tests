import requests
from endpoints.endpoint import Endpoint
from requests.exceptions import JSONDecodeError


class AuthorizationService(Endpoint):

    def authorize(self, name):
        url = f"{self.BASE_URL}/authorize"
        self.response = requests.post(url, json={'name': name})
        try:
            self.json = self.response.json()
            print(f"Received JSON: {self.json}")
        except JSONDecodeError:
            self.json = {'error': 'Response is not in JSON format'}

        if self.response.status_code == 200:
            self.authorization_token = self.json.get('token')
            self.authorization_user = self.json.get('user')

        else:
            self.authorization_token = None
            self.authorization_user = None

    def validate_token(self, token):
        url = f"{self.BASE_URL}/authorize/{token}"
        self.response = requests.get(url)
