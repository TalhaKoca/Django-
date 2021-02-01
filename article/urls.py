from django.contrib import admin
from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path('dashboard/',views.dashboard,name = "dashboard"),
    # bunu yaparak büyük çaptaki projelerde URL karmaşıklığını gidermek için bu şekilde bölümlere ayırabiliriz.
    path('addarticle/',views.addArticle,name = "addarticle"),
    path('article/<int:id>',views.detail,name = "detail"),
    path('update/<int:id>',views.updateArticle,name = "update"),
    path('delete/<int:id>',views.deleteArticle,name = "delete"), 
    path('',views.articles,name = "articles"), 
    path('comment/<int:id>',views.addComment,name = "comment"), 


]