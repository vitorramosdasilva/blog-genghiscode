from django import forms
from .models import Category

class Categoryform(forms.ModelForm):
   class Meta:
        model = Category
        fields = ('nome','author')
#         title = models.CharField(max_length=255)
#         created_at