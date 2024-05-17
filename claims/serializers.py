from .models import Claim
from rest_framework.serializers import ModelSerializer
from datetime import date


class ClaimSerializer(ModelSerializer):
    class Meta:
        model = Claim
        fields = '__all__'
