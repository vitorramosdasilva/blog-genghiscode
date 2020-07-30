from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post


class PesquisaForm(forms.Form):
    pesquisa = forms.CharField(
        label='Pesquisa',
        min_length=3,
        max_length=50,
        help_text="Campo de Pesquisa é Obrigatório",
        widget=forms.TextInput(attrs={'placeholder': 'Pesquisa por...'})
        # required=True
    )

class Postform(forms.ModelForm):
    conteudo = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = ('title','summary','content','author','category','imagem')
#         title = models.CharField(max_length=255)
#         created_at

