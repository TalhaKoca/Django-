from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE, verbose_name="Yazar")
    # user a ait olan verilerin silinmesi(makalenin) için kullandık....
    title = models.CharField(max_length=300,verbose_name="Başlık")
    content = RichTextField() # ESKİSİ: models.TextField(verbose_name="İçerik") 
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    article_image = models.FileField(blank = True, null = True, verbose_name="Makaleye fotoğraf ekleyin")
    # değiştirilen modeli django ya söylemek için  ve veritanındaki tablo yapısını değiştirmek için
    # python manage.py makemigrations
    # veritanında işlemek için
    # python manage.py migrate
     
    def __str__(self):
        return self.title
        # Bu metot self.title dersek Article.object yazan yer makale başlığı olacak.
# verbose_name ile başlıkları değiştirdik...
    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Makale",related_name="comments")
    # her bir Article in birden çok commenti olabilir. Foreignkey yardımıyla
    # commetleri article lara bağlayacagız... 
    # article commentlerini alabilmek için related... article.comment
    comment_author = models.CharField(max_length=50, verbose_name="İsim")
    comment_content= models.CharField(max_length=200,verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']
        # model değişlikliğini django söylememiz gerekiyor...python manage.py makemigrations
        # veritabanına yansıtmak için python manage.py migrate