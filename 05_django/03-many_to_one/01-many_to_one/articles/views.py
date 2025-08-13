from rest_framework.decorators import api_view
from .models import Article, Comment
from .serializers import ArticleSerializer, ArticleListSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True) 
        return Response(serializer.data)
    elif request.method == 'POST':
        # class에 인스턴스 생성하기 위한 인자 전달시 키워드 인자를 써야하는 이유?
            # 클래스 정의할 때 인자 순서 때문임 -> 위에는 그냥 첫번째로 정의되어 있어서 위치인자로 전달 가능
            # 그러나 ArticleSerializer는 위치 인자로 전달할 수가 없음 - 키워드 인자로 전달해야지 됨
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    # article = Article.objects.annotate(num_of_comments=Count('comment')).get(
    #     pk=article_pk
    # )
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 댓글 생성
@api_view(['POST'])
def comment_create(request, article_pk):
    # 게시글을 하나 지정해서, 그곳에 댓글을 생성함
    article = Article.objects.get(pk=article_pk)
    # 댓글 생성은 사용자가 보낸 content 정보를 저장함
    serializer = CommentSerializer(data=request.data)
    # 유효성 검사를 함
    if serializer.is_valid(raise_exception=True):
        # 저장하려고 할때, article 정보 누락됨
        serializer.save(article=article)
        # DB에 반영
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 완성된 댓글 정보를 사용자에게 반환함(JSON)
    


# 모든 댓글 조회
@api_view(['GET'])
def comment_list(request):
   pass

# 댓글 pk 값으로 조회, 삭제, 수정
@api_view(['GET'])
def comment_detail(request, comment_pk):
    pass
   

