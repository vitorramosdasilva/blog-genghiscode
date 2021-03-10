# from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import Post, Comment


class PesquisaForm(forms.Form):
    pesquisa = forms.CharField(
        label='Pesquisa',
        min_length=3,
        max_length=50,
        help_text="Campo de Pesquisa é Obrigatório",
        widget=forms.TextInput(attrs={'placeholder': 'Pesquisa por...'})
        # required=True
    )

class PostForm(forms.ModelForm):
#     conteudo = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post#
        fields = 'title', 'content', 'summary', 'imagem', 'category'
        labels = {
            "title": "Título",
            "summary": "Resumo",
            "content": "Conteúdo",
            "category": "Categoria",
            "imagem": "Imagem"
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Título'}),
            'summary': forms.Textarea(attrs={'placeholder': 'Resumo'}),
            'content': forms.Textarea(attrs={'placeholder': 'Conteúdo'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('texto',)
        labels = {
            "texto":"Comentário"

        }
        widgets = {
            'texto': forms.TextInput(attrs={'placeholder': 'Comente ...'})
        }
#         title = models.CharField(max_length=255)
#         created_at


