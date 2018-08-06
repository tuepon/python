from django import forms
from .models import Deposit


class DepositCreateForm(forms.ModelForm):

    class Meta:
        model = Deposit
#        fields = '__all__'
        fields = ('date')