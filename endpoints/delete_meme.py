import requests
from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):
    def delete_one_meme(self, meme_id=None, headers=None):
        headers = headers if headers else self.headers
        url = f'{self.BASE_URL}/meme/{meme_id}'
        self.response = requests.delete(url, headers=headers)
        return self.response
