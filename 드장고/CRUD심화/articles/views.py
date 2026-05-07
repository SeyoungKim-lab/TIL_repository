from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html',context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)

def delete(request, pk):
    # DB에 저장되어있는 글을 가져온다 => 지운다.
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:   # GET요청이면
    # 다른말로하면 detail페이지에서 수정하기 버튼을 눌렀을때의 요청
        form = ArticleForm(instance=article)
    context = {
        'article' : article,
        'form' : form,
    }
    return render(request, 'articles/update.html', context)
