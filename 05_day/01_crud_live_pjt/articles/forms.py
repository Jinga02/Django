from django import forms    # 상속 받기
from .models import Article
class ArticleForm(forms.ModelForm):
    # title = forms.CharField(max_length=30)
    # content = forms.CharField(widget=forms.Textarea)

    # title = forms.CharField(    # widget 활용
    #     labe = '제목',
    #     widget=forms.TextInput(
    #         attrs={
    #             'class':'my-title',
    #             'placeholder':'Enter the title'
    #         }
    #     )
    # )
    class Meta:
        model = Article
        fields = '__all__'  # 모델의 모든 필드를 포함
        # exclude = ('title',) # 포함하지 않을 필드 지정

    # class clean_title(self): # title 유효성을 검사하는 class    class_필드명
    #     title = self.cleaned.data('title')  # title 데이터를 가져옴
    #     if 'django' in title:
    #         return True
    #     return False
        