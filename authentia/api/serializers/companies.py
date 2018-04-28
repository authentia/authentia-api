from rest_framework import serializers

from companies.models import Company


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ('is_active',)

    def create(self, validated_data):
        company = Company.objects.create(**validated_data)
        user_company = self.context.get('request').user
        user_company.company = company
        user_company.save()
        return company
