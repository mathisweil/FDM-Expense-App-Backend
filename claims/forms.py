from django import ModelForm
from .models import Claim

class ClaimForm(ModelForm):
    class Meta:
        model = Claim
        fields = ['claim_date', 'claim_type', 'claim_amount', 'claim_description']