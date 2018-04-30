from rest_framework import serializers

from users.models import PhotoEnroll


class PhotoEnrollSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhotoEnroll
        exclude = ('user', )

    def create(self, validated_data):
        user = self.context.get('request').user
        document = PhotoEnroll.objects.create(user=user, file=validated_data.get('file'), created=validated_data)
        response = user.enroll_user(self.context.get('request').build_absolute_uri(document.file.url))
        # response = user.enroll_user(document.file)
        if response.get('Errors'):
            document.delete()
            raise serializers.ValidationError(response.get('Errors')[0].get('Message'))
        return document



