from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
# login_required
from django.contrib.auth.decorators import login_required


def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    # 댓글 빈폼
    comment_form = CommentForm()
    # 현재 게시글을 참조중인 댓글을 모두 조회
    comments = article.comment_set.all()    # 역참조
    
    context = {
        'article' : article,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'articles/detail.html',context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)

@login_required
def delete(request, pk):
    # DB에 저장되어있는 글을 가져온다 => 지운다.
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        article.delete()
    return redirect('articles:index')

@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 로그인사용자 == 게시글작성자 일때만 수정기능
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:   # GET요청이면
        # 다른말로하면 detail페이지에서 수정하기 버튼을 눌렀을때의 요청
            form = ArticleForm(instance=article)
    # 로그인사용자 != 게시글작성자 이면, 그냥 인덱스페이지로
    else:
        return redirect('articles:index')
    context = {
        'article' : article,
        'form' : form,
    }
    return render(request, 'articles/update.html', context)


# 댓글작성함수
# (detail.html에서 사용자입력하고 제출버튼을 눌렀을때 실행)
@login_required
def comments_create(request, pk):
    # 게시글을 DB에서 가져오기(조회)
    article = Article.objects.get(pk=pk)
    # 사용자입력(request.POST)을 폼에 넣기
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid(): # 유효성검사
        # 폼객체인 comment_form을 
        # commit=False 즉, DB에는 저장하지 않고
        # 댓글 객체로 저장해두기
        comment = comment_form.save(commit=False)
        # 그 댓글객체에 아티클 외래키를 추가하고
        comment.article = article
        # 댓글객체에 유저 외래키도 추가하고
        comment.user = request.user
        # 댓글객체를 DB에 저장하기
        comment.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article':article,
        'comment_form':comment_form,
    }
    return render(request, 'articles:detail.html', context)


@login_required
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article_pk)


@login_required
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    
    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    
    return redirect('articles:index')