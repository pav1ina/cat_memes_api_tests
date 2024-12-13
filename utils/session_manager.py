import requests


class SessionManager:
    token = None
    BASE_URL = 'http://167.172.172.115:52355/'

    @staticmethod
    def get_token():
        print("Trying to Get Token...")
        if SessionManager.token is None or not SessionManager.validate_token(SessionManager.token):
            print("Token is missing or invalid, refreshing...")
            SessionManager.refresh_token()
        return SessionManager.token

    @staticmethod
    def refresh_token():
        print("Refreshing token...")
        response = SessionManager.authorize('tester')
        if response.status_code == 200:
            SessionManager.token = response.json().get('token')
            print(f"Token refreshed: {SessionManager.token}")
        else:
            print(f"Failed to refresh token, status code: {response.status_code}, response: {response.text}")

    @staticmethod
    def authorize(name):
        url = f"{SessionManager.BASE_URL}/authorize"
        response = requests.post(url, json={'name': name})
        print(f"Authorization Response: {response.status_code}, {response.text}")
        return response

    @staticmethod
    def validate_token(token):
        url = f"{SessionManager.BASE_URL}/authorize/{token}"
        response = requests.get(url)
        print(f"Validate Token Response: {response.status_code}, {response.text}")
        return response.status_code == 200
