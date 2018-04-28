from rest_framework import serializers

from companies.models import CompanyDocument


class CompanyDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyDocument
        fields = '__all__'

    def create(self, validated_data):
        company = self.request.get('context').user.company
        document = CompanyDocument.objects.create(company=company, **validated_data)
        return document
