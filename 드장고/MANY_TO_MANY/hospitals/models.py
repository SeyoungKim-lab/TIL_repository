from django.db import models
# from django.conf import settings

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()
    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'
    
    
class Patient(models.Model):
    # ManyToManyField 작성
    # through 속성으로 중개테이블에 추가 컬럼 작성 가능
    # related_name 속성으로 역참조 네임 설정가능
    doctors = models.ManyToManyField(Doctor, through='Reservation', related_name='patients')
    name = models.TextField()
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'    
    
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'    

# class Article(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
#     title = models.CharField(max_length=10)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#------------------------------------------------
# class Patient(models.Model):
#     # ManyToManyField 작성
#     doctors = models.ManyToManyField(Doctor)
#     name = models.TextField()
#     def __str__(self):
#         return f'{self.pk}번 환자 {self.name}'
    
    
    
#------------------------------------------------    
# class Patient(models.Model):
#     name = models.TextField()
#     def __str__(self):
#         return f'{self.pk}번 환자 {self.name}'
    
# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     def __str__(self):
#         return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'