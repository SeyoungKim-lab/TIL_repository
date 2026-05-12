from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # 사용자이미지 업로드 부분
    # blank=True는 이미지 첨부안해도 되도록
    image = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)