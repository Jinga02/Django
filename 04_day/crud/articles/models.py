from django.db import models


# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_ad = models.DateTimeField(auto_now_add=True) # 생성일
    updated_at = models.DateTimeField(auto_now=True) # 수정일 

    def __str__(self) -> str:
        return f'{self.id}번째 글 - {self.title}'
    