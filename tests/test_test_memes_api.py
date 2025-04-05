import pytest
import allure
import jsonschema


@pytest.mark.smoke
@allure.title('Test retrieve all available memes')
def test_get_all_memes_positive(gel_all_memes, list_meme_schema):
    gel_all_memes.retrieve_memes()
    gel_all_memes.validate_meme_data()
    jsonschema.validate(instance=gel_all_memes.response_payload, schema=list_meme_schema)


TEST_DATA_POSITIVE = [
    {
        "info": {
            "colors": [
                "test"
            ],
            "objects": [
                "picture",
                "text"
            ]
        },
        "tags": [
            "interested",
            "kot cleanup test"
        ],
        "text": "Scary Cat",
        "url": "https://www.friendsoftheanimalvillage.org/single-post/2014/12/18/15-cat-memes-to-brighten-your-day"
    }
]

TEST_DATA_NEGATIVE = [
    {
        "tags": [],
        "text": "",
        "url": ""
    },
    {
        "info": {
            "123": [
                "ppp"
            ]
        },
        "text": "",
        "url": ""
    },
    {
        "info": {
            "123": [
                "ppp"
            ]
        },
        "tags": [],
        "url": ""
    },
    {
        "info": {
            "123": [
                "ppp"
            ]
        },
        "tags": []
    },
    {
        "info": {

        },
        "tags": [

        ],
        "text": "",
        "url": ""
    }
]


@pytest.mark.smoke
@allure.title('Test create one meme with valid data')
@pytest.mark.parametrize('data', TEST_DATA_POSITIVE)
def test_create_one_meme_positive(create_test_meme, cleanup_memes, data, single_meme_schema):
    create_test_meme.create_meme(payload=data)
    create_test_meme.check_that_status_code_is_200()
    create_test_meme.check_that_text_is_correct(expected_text=create_test_meme.meme_text)
    create_test_meme.check_that_info_is_correct(expected_info=create_test_meme.meme_info)
    create_test_meme.check_that_tags_are_correct(expected_tags=create_test_meme.meme_tags)
    create_test_meme.check_that_url_is_correct(expected_url=create_test_meme.meme_url)
    create_test_meme.check_that_updated_by_is_correct(expected_updated_by_name=create_test_meme.authorization_user)
    jsonschema.validate(instance=create_test_meme.response_payload, schema=single_meme_schema)
    cleanup_memes.append(create_test_meme.meme_id)


@pytest.mark.regression
@allure.title('Test attempt to create one meme with invalid data')
@pytest.mark.parametrize('data', TEST_DATA_NEGATIVE)
def test_create_one_meme_negative(create_test_meme, cleanup_memes, data):
    create_test_meme.create_meme(payload=data)
    create_test_meme.check_that_status_code_is_400()
    cleanup_memes.append(create_test_meme.meme_id)


TEST_DATA_UPDATE_POSITIVE = [
    {

        "info": {
            "colors": [
                "test_updated"
            ],
            "objects": [
                "picture_updated",
                "text_updated"
            ]
        },
        "tags": [
            "interested_updated",
            "kot updated"
        ],
        "text": "Updated Cat",
        "url": "https://www.friendsoftheanimalvillage.org/single-post/2014/12/18/15-cat-memes-to-brighten-your-day-upd"
    }
]

TEST_DATA_UPDATE_NEGATIVE = [
    {
        "tags": [
            "interested_updated",
            "kot updated"
        ],
        "text": "Updated Cat",
        "url": "https://www.friendsoftheanimalvillage.org/single-post/2014/12/18/15-cat-memes-to-brighten-your-day-upd"
    },
    {

        "info": {
            "colors": [
                "test_updated"
            ],
            "objects": [
                "picture_updated",
                "text_updated"
            ]
        },
        "text": "Updated Cat",
        "url": "https://www.friendsoftheanimalvillage.org/single-post/2014/12/18/15-cat-memes-to-brighten-your-day-upd"
    },
    {

        "info": {
            "colors": [
                "test_updated"
            ],
            "objects": [
                "picture_updated",
                "text_updated"
            ]
        },
        "tags": [
            "interested_updated",
            "kot updated"
        ],
        "url": "https://www.friendsoftheanimalvillage.org/single-post/2014/12/18/15-cat-memes-to-brighten-your-day-upd"
    },
    {

        "info": {
            "colors": [
                "test_updated"
            ],
            "objects": [
                "picture_updated",
                "text_updated"
            ]
        },
        "tags": [
            "interested_updated",
            "kot updated"
        ],
        "text": "Updated Cat"
    }
]


@pytest.mark.smoke
@allure.title('Test retrieve one meme')
def test_retrieve_one_meme_positive(create_test_meme, get_one_meme, single_meme_schema_get, cleanup_memes):
    create_test_meme.create_meme(payload={
        "info": {
            "colors": [
                "blue"
            ],
            "objects": [
                "picture",
                "text"
            ]
        },
        "tags": [
            "fun",
            "kot blue"
        ],
        "text": "Master Cat",
        "url": "https://www.friendsoftheanimalvillage.org/single-post/2014/12/18/15-cat-memes-to-brighten-your-day"
    })
    jsonschema.validate(instance=create_test_meme.response_payload, schema=single_meme_schema_get)
    get_one_meme.retrieve_meme(create_test_meme.meme_id)
    get_one_meme.check_that_status_code_is_200()
    get_one_meme.check_that_id_is_correct(expected_id=create_test_meme.meme_id)
    get_one_meme.check_that_text_is_correct(create_test_meme.meme_text)
    get_one_meme.check_that_info_is_correct(create_test_meme.meme_info)
    get_one_meme.check_that_tags_are_correct(create_test_meme.meme_tags)
    get_one_meme.check_that_url_is_correct(create_test_meme.meme_url)
    cleanup_memes.append(get_one_meme.meme_id)


@pytest.mark.regression
@allure.title('Test retrieve meme with nonexistent id')
def test_retrieve_one_meme_negative(get_one_meme):
    get_one_meme.retrieve_meme(meme_id=9999999)
    get_one_meme.check_that_status_code_is_404()


@pytest.mark.smoke
@allure.title('Test update meme with valid data')
@pytest.mark.parametrize('data', TEST_DATA_UPDATE_POSITIVE)
def test_update_meme_positive(create_meme_for_test_then_delete, update_meme, data):
    meme_id = create_meme_for_test_then_delete
    data['id'] = meme_id
    update_meme.update_meme(payload=data, meme_id=meme_id)
    update_meme.check_that_status_code_is_200()
    update_meme.check_that_url_is_correct(expected_url=update_meme.meme_url)
    update_meme.check_that_id_is_correct(expected_id=update_meme.meme_id)
    update_meme.check_that_updated_by_is_correct(expected_updated_by_name='tester')
    update_meme.check_that_info_is_correct(expected_info=update_meme.meme_info)
    update_meme.check_that_tags_are_correct(expected_tags=update_meme.meme_tags)


@pytest.mark.regression
@allure.title('Test update meme with invalid data')
@pytest.mark.parametrize('data', TEST_DATA_UPDATE_NEGATIVE)
def test_update_meme_negative(create_meme_for_test_then_delete, update_meme, data):
    meme_id = create_meme_for_test_then_delete
    data['id'] = meme_id
    update_meme.update_meme(payload=data, meme_id=meme_id)
    update_meme.check_that_status_code_is_400()


@pytest.mark.smoke
@allure.title('test delete one meme positive')
def test_delete_one_meme_positive(create_test_meme, delete_test_meme, get_one_meme):
    create_test_meme.create_meme(payload={
        "info": {
            "colors": [
                "blue"
            ],
            "objects": [
                "picture",
                "text"
            ]
        },
        "tags": [
            "fun",
            "kot blue"
        ],
        "text": "Master Cat",
        "url": "https://www.friendsoftheanimalvillage.org/single-post/2014/12/18/15-cat-memes-to-brighten-your-day"
    })
    delete_test_meme.delete_one_meme(meme_id=create_test_meme.meme_id)
    delete_test_meme.check_that_status_code_is_200()
    get_one_meme.retrieve_meme(meme_id=create_test_meme.meme_id)
    get_one_meme.check_that_status_code_is_404()


@pytest.mark.regression
@allure.title('test delete non-existing meme')
def test_delete_meme_negative(delete_test_meme):
    delete_test_meme.delete_one_meme(meme_id=12345678)
    delete_test_meme.check_that_status_code_is_404()
