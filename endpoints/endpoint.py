from utils.session_manager import SessionManager


class Endpoint:
    BASE_URL = 'http://167.172.172.115:52355/'
    response = None
    json = None
    meme_id = None
    meme_text = None
    meme_info = None
    meme_tags = None
    meme_url = None
    meme_updated_by = None
    authorization_token = None
    authorization_user = None

    @property
    def headers(self):
        return {
            'Content-type': 'application/json',
            'Authorization': f"{SessionManager.get_token()}"
        }

    def check_that_status_code_is_200(self):
        assert self.response.status_code == 200, 'Status code is incorrect for valid data'

    def check_that_status_code_is_400(self):
        assert self.response.status_code == 400, 'Status code is incorrect for invalid data'

    def check_that_status_code_is_404(self):
        assert self.response.status_code == 404, 'Status code is incorrect for not present data'

    def check_that_id_is_correct(self, expected_id):
        assert isinstance(self.meme_id, int), "ID should be an integer"
        assert self.meme_id == expected_id, 'Id is incorrect'

    def check_that_text_is_correct(self, expected_text):
        assert self.meme_text == expected_text, (f"Meme text is incorrect: expected '{expected_text}', "
                                                 f"got '{self.meme_text}'")

    def check_that_info_is_correct(self, expected_info):
        assert self.meme_info == expected_info, 'Meme info is incorrect'

    def check_that_tags_are_correct(self, expected_tags):
        assert self.meme_tags == expected_tags, 'Meme tags are incorrect'

    def check_that_url_is_correct(self, expected_url):
        assert self.meme_url == expected_url, 'Meme info is incorrect'

    def check_that_updated_by_is_correct(self, expected_updated_by_name):
        assert self.meme_updated_by == expected_updated_by_name, 'Updated by name is incorrect'

    def check_authorization_token(self, expected_token):
        assert self.authorization_token == expected_token, "Token should be present after successful authorization"

    def check_authorization_user(self, expected_user):
        assert self.authorization_user == expected_user, "User should be present after successful authorization"
