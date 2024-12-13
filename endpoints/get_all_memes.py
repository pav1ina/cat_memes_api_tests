import requests
from endpoints.endpoint import Endpoint


class GetAllMemes(Endpoint):

    def retrieve_memes(self):
        url = f"{self.BASE_URL}/meme"
        self.response = requests.get(url, headers=self.headers)
        return self.response

    def validate_meme_data(self):
        if self.response.status_code == 200:
            memes = self.response.json().get('data', [])
            for meme in memes:
                assert isinstance(meme['id'], int), "ID should be an integer"
                assert isinstance(meme['text'], str), "Text should be a string"
                assert isinstance(meme['tags'], list), "Tags should be a list"
                assert 'url' in meme, "URL key is missing in meme data"
        else:
            raise Exception("Failed to retrieve memes with status code: {}".format(self.response.status_code))
