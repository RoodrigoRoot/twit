import pytest
from tweets.services import tweet_create
from tweets.models import Tweet


@pytest.mark.django_db
def test_function_tweet_create(user_factory):
    """Tests to create tweet succesful"""
    user = user_factory.create()
    payload = {"body": "Probando twitt4er", 'user': user.id}
    res = tweet_create(payload['body'], payload['user'])
    tweet = Tweet.objects.last()

    assert res is not None
    assert tweet is not None
    assert tweet.body == payload['body']


@pytest.mark.django_db
def test_function_tweet_create_missing_body(user_factory):
    user = user_factory.create()
    payload = {"body": "", 'user': user.id}
    res = tweet_create(payload['body'], payload['user'])
    assert res["message"] == "The field body doesn't can't blank"
    assert res["results"] is False
