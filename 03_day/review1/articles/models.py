from django.db import models

# articles/models.py
class Article(models.Model): #article app에서 사용할 게시글 Article
    title = models.CharField(max_length=20) # models에서 title은 문자열 형태, 글자수 지정
    content = models.TextField() # 글자수 지정없이 사용 가능

 