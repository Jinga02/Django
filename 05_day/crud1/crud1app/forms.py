from django import forms
from .models import Crud
class CrudForm(forms.ModelForm):
    # title = forms.CharField(max_length=20)
    # content = forms.CharField()
    class Meta:
        model = Crud
        fields = '__all__'