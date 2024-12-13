import pytest
import json
from utils.session_manager import SessionManager
from endpoints.get_all_memes import GetAllMemes
from endpoints.get_one_meme import GetOneMeme
from endpoints.create_meme import CreateMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.update_meme import UpdateMeme
from endpoints.authorization import AuthorizationService


@pytest.fixture(scope="session")
def token():
    response = SessionManager.authorize('testuser')
    return response.json().get('token')


@pytest.fixture()
def authorize_verification():
    return AuthorizationService()


@pytest.fixture()
def gel_all_memes():
    return GetAllMemes()


@pytest.fixture()
def create_test_meme():
    return CreateMeme()


@pytest.fixture()
def delete_test_meme():
    return DeleteMeme()


@pytest.fixture()
def get_one_meme():
    return GetOneMeme()


@pytest.fixture()
def update_meme():
    return UpdateMeme()


@pytest.fixture()
def cleanup_memes(delete_test_meme):
    created_meme_ids = []
    yield created_meme_ids
    for meme_id in created_meme_ids:
        if meme_id is not None:
            delete_test_meme.delete_one_meme(meme_id)


@pytest.fixture()
def single_meme_schema():
    with open('schemas/single_meme_schema_create.json', 'r') as file:
        schema = json.load(file)
        return schema


@pytest.fixture()
def single_meme_schema_get():
    with open('schemas/single_meme_schema_get.json', 'r') as file:
        schema = json.load(file)
        return schema


@pytest.fixture()
def list_meme_schema():
    with open('schemas/list_of_memes_schema.json', 'r') as file:
        schema = json.load(file)
        return schema


@pytest.fixture()
def create_meme_for_test_then_delete(create_test_meme, delete_test_meme):
    payload = {
        "info": {
            "colors": [
                "whiteTest"
            ],
            "objects": [
                "picture",
                "text"
            ]
        },
        "tags": [
            "fun",
            "kot white"
        ],
        "text": "White Cat",
        "url": "https://www.friendsoftheanimalvillage.org/single-post/2014/12/18/15-cat-memes-to-brighten-your-day"
    }
    create_test_meme.create_meme(payload=payload)
    yield create_test_meme.meme_id
    delete_test_meme.delete_one_meme(meme_id=create_test_meme.meme_id)
