from rest_framework import serializers
from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        # 읽기 전용 필드는 데이터를 전송하는 시점에 
        # 해당 필드를 유효성 검사에서 제외시키고 데이터 조회시에는 출력 하도록 한다.
        read_only_fields = ('article',)

    # article 값 None 처리
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop('article', None)
        return rep
    
# 댓글 전체를 조회 할때는
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # id, title, content 출력
        fields = ('id', 'title', 'content')

class ArticleDetailSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    # ArticleListSerializer의 Meta를 상속받고
    class Meta(ArticleListSerializer.Meta):
        # + comment_set 와 comment_count를 사용하겠다.
        fields = ArticleListSerializer.Meta.fields + (
            'comment_set',
            'comment_count'
        )
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['comments'] = rep.pop('comment_set', []) # 값이 없다면 [] 빈 값
        return rep

# class ArticleListSerializer(serializers.ModelSerializer):
#     # Nested relationships
#     # 모델 관계 상으로 참조 된 대상은 참조하는 대상의 표현에 포함되거나 중첩(nested)될 수 있다.
#     # 이러한 중첩된 관계를 serializers를 필드로 사용하여 표현 할 수 있다.
#     comment_set = CommentSerializer(many=True, read_only=True)
#     # source는 필드를 채우는데 사용 할 속성을 탐색해준다.
#     comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
#     class Meta:
#         model = Article
#         # fields = ('id', 'title', 'content')
#         fields = '__all__'

    
#     # ModelSerializer의 메서드
#     # super(ModelSerializer)의 to_representation(instance)이 나가는게 기본값
#     # rep는 키 - 벨류 형태
#     # 가지고 있는 데이터 중에 comment_set으로 가지고 있는 데이터 pop해서 comments에 할당
#     def to_representation(self, instance):
#         rep = super().to_representation(instance)
#         rep['comments'] = rep.pop('comment_set', []) # 값이 없다면 [] 빈 값
#         return rep