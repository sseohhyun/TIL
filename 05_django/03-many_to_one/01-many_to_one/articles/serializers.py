# articles/serializers.py

from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ('created_at', 'updated_at',)


# 게시글 조회 할 때 해당 게시글의 댓글도 함께 조회
class ArticleSerializer(serializers.ModelSerializer):
    # class CommentDetailSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Comment
    #         fields = ('id', 'content',)   # 댓글의 id와 content만 보여준다.

    # read_only=True 옵션을 통해 해당 필드를 읽기 전용으로 설정할 수 있다.
    # comment_set = CommentDetailSerializer(many=True, read_only=True) # related_name을 통해 역참조
    # 댓글 갯수 표시
    # num_of_comments = serializers.SerializerMethodField()


    class Meta:
        model = Article
        fields = '__all__'
        # # fields = ('id', 'title',)
        # exclude = ('created_at', 'updated_at',)

    # def get_num_of_comments(self, obj):
    #     # 여기서 obj는 Serializer가 처리하는 Article 인스턴스
    #     # view에서 annotate 한 필드를 그대로 사용 가능
    #     return obj.num_of_comments


# 댓글 조회 시 게시글 정보도 함께 조회
class CommentSerializer(serializers.ModelSerializer):
    '''
        serializer에 정의하는 fields는?
        사용자에게 보여줄 데이터를 정하는 곳
        혹은, 사용자가 어떤 데이터를 보내야 하는지를 정하는 곳

        comment의 id, created_at, updated_at, article은
        사용자가 댓글 생성할 때 보내는 데이터가 아님
            
            댓글을 작성하고 나서 정확히 1번 게시글에 작성되었다는 사실을 알고 싶을 때는?

        댓글을 `생성`할 때는 article의 정보를 사용자가 아닌 `서버`가 처리
        단, 댓글을 `조회` 할 때는 article의 정보도 포함해서 반환
            -> article 필드는 읽기 전용이어야 함
        
        이 코멘트 시리얼 라이저의 어떤 특정한 필드를 다른 형태로 재정의
        article 필드에 대해서 재정의 함
            id와 title을 보여주고 싶음
            1. id랑 title만 보여주는 serializer 정의하기
                -> 무엇 만을 위한 시리얼라이저인가
            2. 이미 있는 시리얼라이저 사용하기

    '''
    class ArticleForCommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('id', 'title', )
    
    article = ArticleForCommentSerializer(read_only=True)

    # tuple에 요소 1개 일 때, trailing comma 찍어야 함
    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('article',)

