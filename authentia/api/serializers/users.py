from rest_framework import serializers
from django.contrib.auth import authenticate


class UserAuthTokenSerializer(serializers.Serializer):
    """Returns a token for authenticating requests of corresponding user instance.
    """
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            client = self.authenticate(email=email, password=password)

            if not client:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg)

        data['user'] = client
        return data

    def authenticate(self, email, password):
        client = authenticate(username=email, password=password)
        return client


class UserRecognitionSerializer(serializers.Serializer):
    """
    """
    file = serializers.FileField()
