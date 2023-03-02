from django import forms
from api.models import HR

class PostForm(forms.ModelForm):
    class Meta:
        model = HR
        fields = '__all__'
        exclude = ['is_activate']