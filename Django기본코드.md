# 가상환경 생성
python -m venv venv
source venv/scripts/activate
pip install django 또는 pip install -r requirments.txt
(pip freeze > requirments.txt)
# 가상환경 종료
deactivate
# 프로젝트 생성
django-admin startproject 프로젝트명 .
# 서버실행
python manage.py runserver
# 앱 생성
python manage.py startapp 앱명(복수형권장)
settings.py 에서 앱명 등록하기


# 요청과 응답
- 프로젝트폴더의 urls.py
  - import include
  - path('books/', include('books.urls'))
- 앱폴더의 urls.py만들기
  - from django.urls import path
  - from . import views
  - app_name = 'books'
  - urlpatterns = [
    path('', views.index, name='index'),
    ]
- 앱폴더의 views.py
  redirect 임포트하기.
  from .models import Book
  from .forms import BookForm
  def index(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'books/index.html', context)
- models.py
  class Book(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
- forms.py 생성
  from django import forms
  from .models import Book

  class BookForm(forms.ModelForm):
      #Python의 Inner class라는 문법과 무관.
      class Meta:
          model = Book
          fields = '__all__'
          # exclude = ('title',)
- 앱폴더에 templates/앱이름 폴더생성
  - index.html
    {% extends 'base.html' %}
    {% block content %}
      <h1>글 목록</h1>
      <a href="{% url "books:new" %}">NEW</a>
      <hr>
      {% for book in books %}
        <div>
          <p>글 번호: {{ book.pk }}</p>
          <p>
            글 제목: <a href="{% url "books:detail" book.pk %}">{{ book.title }}</a>
          </p>
        </div>
        <hr>
      {% endfor %}
    {% endblock content %}
- 프젝폴더의 settings.py
  - TEMPLATES의 'DIR'에 BASE_DIR / 'templates' ,이거넣기
- 프젝,앱,venv등 있는 전체 폴더에 templates생성->base,html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
  </head>
  <body>
    <div class="container">
    {% block content %}
    
    {% endblock content %}
    </div>
  </body>
  </html>
- urls.py, views.py까지함.
