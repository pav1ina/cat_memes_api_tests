import pytest


def test_authorization_successful(authorize_verification):
    authorize_verification.authorize(name='tester authorized')
    authorize_verification.check_authorization_token(expected_token=authorize_verification.authorization_token)
    authorize_verification.check_authorization_user(expected_user=authorize_verification.authorization_user)
    authorize_verification.validate_token(authorize_verification.authorization_token)
    authorize_verification.check_that_status_code_is_200()


def test_authorization_negative(authorize_verification):
    authorize_verification.authorize(name=None)
    authorize_verification.check_that_status_code_is_400()


def test_validate_token_negative(authorize_verification):
    authorize_verification.validate_token(token=12345678)
    authorize_verification.check_that_status_code_is_404()
