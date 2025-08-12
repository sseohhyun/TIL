from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):
    # 모델에 대한 정보를 토대로 직렬화를 함 = 메타데이터
     class Meta:
        model = Article
        # fields = "__all__"
        fields = ('id', 'title')

# 위에는 오로지 전체 목록만을 위한 시리얼라이저가 있다면, 
# 이번에는 범용적으로 게시글에 대한 전반적인 처리가 가능한 시리얼 라이저
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        