import requests
from endpoints.endpoint import Endpoint
from requests.exceptions import JSONDecodeError


class GetOneMeme(Endpoint):

    def retrieve_meme(self, meme_id=None):
        url = f"{self.BASE_URL}/meme/{meme_id}"
        self.response = requests.get(url, headers=self.headers)
        print(self.response.status_code)
        print(f"Response Text: {self.response.text}")

        try:
            self.json = self.response.json()
            print(f"Received JSON: {self.json}")
        except JSONDecodeError:
            self.json = {'error': 'Response is not in JSON format'}

        if self.response.status_code == 200:
            self.meme_id = self.json.get("id")
            self.info = self.json.get("info")
            self.tags = self.json.get("tags")
            self.text = self.json.get("text")
            self.updated_by = self.json.get("updated_by")
            self.url = self.json.get("url")

        else:
            self.meme_id = None
            self.tags = None
            self.info = None
            self.text = None
            self.updated_by = None
            self.url = None
