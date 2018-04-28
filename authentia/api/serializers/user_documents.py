from rest_framework import serializers

from users.models import UserDocument


class UserDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserDocument
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        document = UserDocument.objects.create(user=user, **validated_data)
        return document
