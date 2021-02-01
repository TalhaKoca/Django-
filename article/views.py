from django.shortcuts import render, HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from django.contrib import messages
from .models import Article,Comment
from django.contrib.auth.decorators import login_required
# Create your views here.
# anlamı URL geldiğinde çalışacak fonksiyonları buraya yazabilirsin....

def index(request):
    # her view fonksiyonunda ilk parametre mutlaka bulunması gerekiyor...
    # return HttpResponse("Burası Malatya")
    context = {
        "numbers": [1,2,3,4]
    }
    return render(request,"index.html",context)
    # return render(request,"index.html",{"number":7})
def about(request):
    return render(request,"about.html")

@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request,"dashboard.html",context)

@login_required(login_url="user:login")  
def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False) # yaptığımızda save işlemini bize bırakıyor.
        # article objesi 
        # article.save() objeyi oluşturup sonra kaydediyor.

        article.author = request.user
        article.save()
        messages.success(request,"Makale Başarıyla Oluşturuldu..")
        return redirect("article:dashboard")

    return render(request,"addarticle.html",{"form":form})

def detail(request,id):
    #article = Article.objects.filter(id=id).first() # gördüğü ilk article dön dedik.
    article = get_object_or_404(Article,id=id)

    comments = article.comments.all()

    return render(request,"detail.html",{"article":article,"comments":comments})

@login_required(login_url="user:login")
def updateArticle(request,id):
    article = get_object_or_404(Article,id=id)
    form = ArticleForm(request.POST or None, request.FILES or None,instance = article)
    if article.author == request.user:
        if form.is_valid():
            article = form.save(commit=False) 
            article.author = request.user
            article.save()
            messages.success(request,"Makale Başarıyla Güncellendi..")
            return redirect("article:dashboard")
        else:
            return render(request,"update.html",{"form":form})

    else:
        messages.info(request,"Yazarı Olduğunuz Makaleyi Güncelleyebilirsiniz..")
        return redirect("article:dashboard")
        


@login_required(login_url="user:login")
def deleteArticle(request,id = id):
    article = get_object_or_404(Article,id = id)
    if article.author.id == request.user.id:

        article.delete()
        messages.info(request,"Makale Başarıyla Silindi")
        return redirect("article:dashboard")
    else:
        messages.warning(request,"Yazarı Olduğunuz Makaleyi Silebilirsiniz..")
        return redirect("article:dashboard")

def articles(request):

    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request,"articles.html",{"articles":articles})
    
    articles = Article.objects.all()
    return render(request,"articles.html",{"articles": articles})

def addComment(request,id):
    article = get_object_or_404(Article, id=id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        
        newComment = Comment(comment_author=comment_author, comment_content=comment_content)
        newComment.article = article
        newComment.save()

    return redirect(reverse("article:detail",kwargs={"id":id}))
    # "/articles/article/" + str(id)
    # dinamik bir URL yi redirect ederken reverse kullanmak zorundayız..