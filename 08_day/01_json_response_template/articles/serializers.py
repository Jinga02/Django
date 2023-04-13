from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    # ModelSerializer 클래스는 모델 필드에 해당하는 필드가 있는
    # Serializer클래스를 자동으로 만들 수 있는 shortcut을 제공한다.
    # Model정보에 맞춰 필드를 생성해주고, 유효성 검사기도 생성해주고
    # .create() 및 .update()의 간단한 기본 구현이 포함되어있다.
    class Meta:
        model = Article
        # fields = '__all__'
        fields = ('id', 'title', 'content')

