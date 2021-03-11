from django import forms
from blog.models import Category

class CategoryForm(forms.ModelForm):
   class Meta:
        model = Category
        fields = ('nome',)
#         title = models.CharField(max_length=255)
#         created_at