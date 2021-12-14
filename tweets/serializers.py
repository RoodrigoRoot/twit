from tweets.models import Tweet
from rest_framework import serializers


class TweetCreateSerializer(serializers.Serializer):

    body = serializers.CharField(allow_blank=True)
    user = serializers.IntegerField()

    def validate(self, attrs):
        body = attrs.get('body', '')
        if body == '':
            raise serializers.ValidationError({'message': "The field body doesn't can't blank"})
        return attrs


class TweetReadSerializer(serializers.Serializer):

    body = serializers.CharField()
    user = serializers.CharField()
    created_at = serializers.DateTimeField()
