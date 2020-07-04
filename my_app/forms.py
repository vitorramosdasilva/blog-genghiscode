from django import forms


class PesquisaForm(forms.Form):
    pesquisa = forms.CharField(
        label='Pesquisa',
        min_length=3,
        max_length=50,
        help_text="Campo de Pesquisa é Obrigatório",
        widget=forms.TextInput(attrs={'placeholder': 'Pesquisa por...'})
        # required=True
    )
