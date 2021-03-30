from django.db import models

# Create your models here.
class Guser(models.Model):
    username = models.CharField(max_length=64,verbose_name="사용자명")
    useremail = models.EmailField(max_length=128,verbose_name="사용자이메일")
    password = models.CharField(max_length=64,verbose_name="비밀번호")

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name_plural="GSM사용자"
