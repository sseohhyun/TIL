from django.urls import path
from . import views

urlpatterns = [
    # 왜? articles/ 경로에 GET, POST 요청이 왔을 때,
    # 행위 method에 따라 서로 다른 작업을 진행함
    # 경로만 ㅗ면 articles/
    # 행위와 더해서 보면 GET, POST articles/
    path('', views.article_get_or_create),
]