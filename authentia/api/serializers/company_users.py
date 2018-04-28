from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.db import transaction


from users.models import CompanyUser, TokenUserModel


class CompanyUserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyUser
        exclude = ('is_admin', 'is_superuser', 'groups', 'user_permissions', 'password')
        read_only_fields = ('token', 'email', )


class CompanyUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CompanyUser
        exclude = ('is_admin', 'is_superuser', 'groups', 'user_permissions', )
        read_only_fields = ('token', )

    def validate(self, data):
        confirm_password = data.get('confirm_password')
        password = data.get('password')

        if confirm_password != password:
            raise serializers.ValidationError('Password and confirm password does not match.')

        return data

    def create(self, validated_data):

        with transaction.atomic():
            validated_data.pop('confirm_password')
            company_user = CompanyUser.objects.create_user(**validated_data)
            token, created = TokenUserModel.objects.get_or_create(company_user_token=company_user)
            company_user.token = token
            company_user.save()
            return company_user
