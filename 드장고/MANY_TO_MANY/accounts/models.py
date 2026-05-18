from django.db import models
# AbstractUser 클래스를 상속받는 커스텀 User 클래스 작성
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # 팔로잉기능
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    pass
