from rest_framework import serializers

from users.models import PhotoEnroll


class PhotoEnrollSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhotoEnroll
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        document = PhotoEnroll.objects.create(user=user, **validated_data)
        return document
