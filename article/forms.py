from django import forms
from .models import Article
class ArticleForm(forms.ModelForm): # alternatif bir form yöntemi kullandık..
    class Meta:
        model = Article # ArticleForm ve Article modelini bağlantılı haline getirmiş oluyoruz...
        fields = ["title","content","article_image"] # Bu alanlardan üç tane input oluştur dedik...
        