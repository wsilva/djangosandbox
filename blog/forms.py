from django import forms

class FormArtigo(forms.Form):
    titulo = forms.CharField(max_length=150)
    # conteudo = forms.CharField(widget=form.Textarea())
    conteudo = forms.CharField()
    publicado = forms.BooleanField()