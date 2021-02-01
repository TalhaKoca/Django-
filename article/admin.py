from django.contrib import admin
from .models import Article,Comment
# .models şu anki klasördeki models e git anlamına geliyor...
# Register your models here.

# admin panelinde göstermek için:
# admin.site.register(Article)

admin.site.register(Comment)

# python manage.py makemigrations 
# modelimdeki değişikliği database e göstermek gerekiyor.
# yani Django ya söyleyeceğiz
# python manage.py migrate  veritabanında comment tablomuz oluştu...

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    
    # şimdi sırada ArticleAdmin ile Article birleştirmemiz gerekiyor...
    # ArticleAdmin class ının Article modelini özelleştireceğini söylememiz gerekiyor...
    
    list_display = ["title","author","created_date"]
    # Başlığın yanında yazar bloğunu ekledik...
    
    list_display_links = ["title","created_date"]
    # Tarihe Link eklendi... 

    search_fields = ["title"]
    # sadece başlığa göre arama özelliği kazandırdık..

    list_filter = ["created_date"]
    # created_date verirsek tarihe göre süzgeç oluşturulmuş oldu.

    class Meta:
        # ArticleAdmin ile Article ı bağlamamız için:
        model = Article # yazmamız gerekiyor... Django daki özel bir class