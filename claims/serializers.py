from .models import Claim
from rest_framework.serializers import ModelSerializer
from datetime import date


class ClaimSerializer(ModelSerializer):
    class Meta:
        model = Claim
        fields = '__all__'

    def create(self, validated_data):
        validated_data['claimed_by'] = validated_data['employee_id'].first_name + " " + validated_data['employee_id'].last_name
        return Claim.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.status = validated_data['status'].upper()
        instance.save()
        return instance
