from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.db import transaction

from users.models import AuthentiaUser, TokenUserModel


class AuthentiaUserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthentiaUser
        exclude = ('is_admin', 'is_superuser', 'groups', 'user_permissions', 'password')
        read_only_fields = ('token', 'email', )


class AuthentiaUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = AuthentiaUser
        exclude = ('is_admin', 'is_superuser', 'groups', 'user_permissions')
        read_only_fields = ('token', )

    def validate(self, data):
        confirm_password = data.get('confirm_password')
        password = data.get('password')

        if confirm_password != password:
            raise serializers.ValidationError('Password and confirm password does not match.')

        # try:
        #     validate_password(password)
        # except serializers.ValidationError as e:
        #     raise serializers.ValidationError(e)

        return data

    def create(self, validated_data):

        with transaction.atomic():
            validated_data.pop('confirm_password')
            authentia_user = AuthentiaUser.objects.create_user(**validated_data)
            token, created = TokenUserModel.objects.get_or_create(user_token=authentia_user)
            authentia_user.token = token
            authentia_user.save()
            return authentia_user
