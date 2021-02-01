"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#from article.views import index
from article import views
# view buraya dahil edildi ve boş sayfa döndüğünde anasayfa yazdırılacak...

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name = "index"), # buraya URL geldiğinde çalışması için gerekli olan fonksiyonu views yazacagız....
    # name yaparak ilerden redirect yaptıgımızda bu URL ye gitmiş olacagız...
    path('about/', views.about,name = "about"),
    # path('detail/<int:id>', views.detail,name = "detail"),
    # <int:id> dinamik URL yapısını tanımladık.
    # def detail(request,id):
    # return HttpResponse("Detail:"+str(id)) {views}
    path('articles/',include("article.urls")),
    path('user/',include("user.urls")),

]   
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Bu yapıyla media URL ve media Root python dosyaları üzerinden ulaşabileceğiz...
